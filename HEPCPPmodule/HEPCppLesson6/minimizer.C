#include "Math/Minimizer.h"
#include "Math/Factory.h"
#include "Math/Functor.h"
#include "TString.h"
#include <iostream>
#include "TRandom3.h"
#include "Math/IntegratorMultiDim.h"

/*
  const double elements[16] = 
  {1.0, 0.1, -0.1, 0.2, 
  0.1, 1., 0., 0.0,
  -0.1, 0., 1., 0.4,
  0.2, 0., 0.4, 1.
  };
  TMatrixDSym B(4, elements);
  const double grad[4] = {-0.3, -2., -0.5, 2.0};
*/

const int NDIM = 4;

TMatrixD B = THilbertMatrixD(NDIM,NDIM);

double grad[NDIM] = {};
TVectorD g(NDIM, grad);  
const double f0 = 1.0;

double Quadratic(const double *xx)
{
  TVectorD x(NDIM, xx);
  return f0 + g*x + 0.5*(x*(B*x));
}

double Rosenbrock(const double *xx)
{
  if(NDIM%2==1) return 1.0;
  const double alpha = 100.0;
  double ret = 0.;
  for(unsigned int i=0 ; i<NDIM/2; ++i){
    ret += alpha*(xx[2*i+1] - xx[2*i]*xx[2*i])*(xx[2*i+1] - xx[2*i]*xx[2*i])  + (1-xx[2*i])*(1-xx[2*i]);
  }
  return ret;
}

void minimizer(const char * minName = "Minuit", const char *algoName = "Migrad", const char *funcName="Quadratic"){

  TRandom3 ran(1234);
  double gmin = -1.;
  double gmax = +1.;
  for(unsigned int i=0 ; i<NDIM; ++i){
    double r = ran.Rndm();
    g[i] = gmin*r + gmax*(1-r);
  }

  if(TString(funcName)=="Quadratic"){
    TVectorD eig(NDIM);
    TMatrixD eigs = B.EigenVectors(eig);
    Double_t det = B.Determinant();
    std::cout << "Determinant of B: " << det << std::endl;
    eig.Print();
    eigs.Print();
    if(det==0.){
      std::cout << "Matrix is singular" << std::endl;
    }
    else if(eig.Min()>0.){
      std::cout << "Matrix is positive definite" << std::endl;
    }
    else if(eig.Min()<0.){
      std::cout << "Matrix is undefinite" << std::endl;
    }
    std::cout << "Condition number is: " << eig.Max()/eig.Min() << std::endl;
  }

  ROOT::Math::Minimizer* minimum = ROOT::Math::Factory::CreateMinimizer(minName, algoName);
  minimum->SetMaxFunctionCalls(1000000); 
  minimum->SetTolerance(0.001);
  minimum->SetPrintLevel(1);

  double (*func)(const double *) = nullptr;
  if(TString(funcName)=="Quadratic") func = Quadratic;
  else func = Rosenbrock;

  ROOT::Math::Functor f( func, NDIM);

  double step[NDIM] = {};
  for(unsigned int i=0 ; i<NDIM; ++i) step[i] += 0.01;
  double start[NDIM] = {};
  
  minimum->SetFunction(f);

  for(unsigned int i=0 ; i<NDIM; ++i){
    minimum->SetVariable(i, Form("x%d",i), start[i]-1.0, step[i]);
  }

  minimum->Minimize();

  const double *xs = minimum->X();
  std::cout <<  std::endl;
  std::cout << "NUMERICAL:  f(";
  for(unsigned int i=0 ; i<NDIM; ++i) std::cout << xs[i] << ",";
  std::cout <<  "): " << minimum->MinValue()  << std::endl;
  if(TString(funcName)=="Quadratic"){
    TVectorD x0(NDIM, start);
    TMatrixD Binv(B);
    TVectorD xs_ana = x0 - Binv.InvertFast()*(B*x0 + g);
    std::cout << "ANALYTICAL: f(";
    for(unsigned int i=0 ; i<NDIM; ++i) std::cout << xs_ana[i] << ",";
    std::cout <<  "): " << Quadratic(xs_ana.GetMatrixArray()) << std::endl;
  }

  double xL[NDIM] = {};
  double xU[NDIM] = {};
  for(unsigned int i=0 ; i<NDIM; ++i) xL[i] = -1.0;
  for(unsigned int i=0 ; i<NDIM; ++i) xU[i] = +1.0;
  double val = 0.;
  ROOT::Math::IntegratorMultiDim ig1(ROOT::Math::IntegrationMultiDim::kVEGAS); 
  ig1.SetFunction(f);
  val = ig1.Integral(xL,xU);
  std::cout << "VEGAS: integral result is: " << val << std::endl;
  ROOT::Math::IntegratorMultiDim ig2(ROOT::Math::IntegrationMultiDim::kADAPTIVE); 
  ig2.SetFunction(f);
  val = ig2.Integral(xL,xU);
  std::cout << "ADAPTIVE: integral result is: " << val << std::endl;
  ROOT::Math::IntegratorMultiDim ig3(ROOT::Math::IntegrationMultiDim::kPLAIN); 
  ig3.SetFunction(f);
  val = ig3.Integral(xL,xU);
  std::cout << "PLAIN: integral result is: " << val << std::endl;
  

  return;
}
