#include "TCanvas.h"
#include <chrono>

using namespace std::chrono;

void read_Draw(){

  auto start = high_resolution_clock::now();
  TFile* f = TFile::Open("tree_C.root", "READ");
  TTree* tree = (TTree*)f->Get("tree");

  TH1D* h0 = new TH1D("h0", "", 100,-3,3);
  TH1D* h1 = new TH1D("h1", "", 100,-3,3);
  TH1D* h2 = new TH1D("h2", "", 100,-3,3);
  TH1D* h3 = new TH1D("h3", "", 100,-3,3);
  TH1D* h4 = new TH1D("h4", "", 100,-3,3);
  TH1D* h5 = new TH1D("h5", "", 100,-3,3);
  auto stop = high_resolution_clock::now();  
  auto duration = duration_cast<milliseconds>(stop - start); 
  std::cout << "ROOT definitions done in " << duration.count()/1000. << " seconds" << std::endl; 

  start =  high_resolution_clock::now();
  std::cout << "h0" << std::endl;
  tree->Draw("px>>h0", "(px+py)>0 && random<pz" );
  std::cout << "h1" << std::endl;
  tree->Draw("px>>h1", "(px+py)>0 && random<pz*0.1" );
  std::cout << "h2" << std::endl;
  tree->Draw("px>>h2", "(px+py)>0 && random<pz*0.2" );
  std::cout << "h3" << std::endl;
  tree->Draw("px>>h3", "(px+py)>0 && random<pz*0.3" );
  std::cout << "h4" << std::endl;
  tree->Draw("px>>h4", "(px+py)>0 && random<pz*0.4" );
  std::cout << "h5" << std::endl;
  tree->Draw("px>>h5", "(px+py)>0 && random<pz*0.5" );
  auto c1 = new TCanvas();   

  h0->DrawClone(); 
  h1->DrawClone("SAME");
  h2->DrawClone("SAME");
  h3->DrawClone("SAME");
  h4->DrawClone("SAME");
  h5->DrawClone("SAME");
  stop = high_resolution_clock::now();
  duration = duration_cast<milliseconds>(stop - start);
  std::cout << "Draws done in " << duration.count()/1000. << " seconds" << std::endl; 
}
