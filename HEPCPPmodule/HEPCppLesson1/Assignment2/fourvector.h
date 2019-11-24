#ifndef FOURVECTOR_H
#define FOURVECTOR_H
#include <math.h>

template <class T>
class VectorXYZT {
    public:
      VectorXYZT() {}
      VectorXYZT(T  px, T  py, T  pz, T  e) :
	      m_px(px),m_py(py), m_pz(pz), m_e(e) {}
      //getters
      T px() const { return m_px;}
      T py() const { return m_py;}
      T pz() const { return m_pz;}
      T e() const { return m_e;}
      T pt() const { return sqrt(m_px*m_px+m_py*m_py);}
      T m() const { return sqrt(m_e*m_e-(m_px*m_px+m_py*m_py+m_pz*m_pz));}
      
      template <class T2>
      VectorXYZT<T> operator+(const T2 & other) const {
	      VectorXYZT ret(m_px+other.px(), m_py+other.py(),m_pz+other.pz(),m_e+other.e());
	      return ret;
      }
      //setters
      void setPx(T px) {m_px=px;}
      void setPy(T py) {m_py=py;}
      void setPz(T pz) {m_pz=pz;}
      void setE(T e) {m_e=e;}

    private:
      T m_px;
      T m_py;
      T m_pz;
      T m_e;

};

template <class T>
class VectorPtEtaPhiMass {
    public:
      VectorPtEtaPhiMass() {}
      VectorPtEtaPhiMass(T  pt, T  eta, T  phi, T  m) :
              m_pt(pt),m_eta(eta), m_phi(phi), m_m(m) {}
      //getters
      T pt() const { return m_pt;}
      T eta() const { return m_eta;}
      T phi() const { return m_phi;}
      T m() const { return m_m;}
      T px() const { return m_pt*cos(m_phi);}
      T py() const { return m_pt*sin(m_phi);}
      T pz() const { return m_pt/tan(theta());}
      T e() const { return sqrt(m_m*m_m+(pt()*pt()+pz()*pz()));}
      T theta() const { return T(2.)*atan(exp(-m_eta)); }
      template <class T2>
      VectorXYZT<T> operator+(const T2 & other) const {
              VectorXYZT<T>  ret(px()+other.px(), py()+other.py(),pz()+other.pz(),e()+other.e());
              return ret;
      }
      //setters
      void setPt(T pt) {m_pt=pt;}
      void setEta(T eta) {m_eta=eta;}
      void setPhi(T phi) {m_phi=phi;}
      void setM(T m) {m_m=m;}

    private:
      T m_pt;
      T m_eta;
      T m_phi;
      T m_m;

};


#endif
