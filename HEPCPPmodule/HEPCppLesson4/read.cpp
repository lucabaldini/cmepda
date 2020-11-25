#include "fourvector.h"
#include <iostream>
#include <TFile.h>
#include <TTree.h>
#include <vector>
#include <TSystem.h>
int main()
{
 std::vector<FourVector> * particles= new  std::vector<FourVector>;
 gSystem->Load("AutoDict_FourVector_cxx.so");
 gSystem->Load("AutoDict_FourVectors_cxx.so");
 TFile f("testWithObj.root");
 TTree *t=(TTree *)f.Get("tree");
 

 t->GetBranch("myParticles")->SetAddress(& particles);

 auto nevent = t->GetEntries();
   for (int i=0;i<nevent;i++) {
      t->GetEvent(i);
      std::cout << particles->size() << std::endl;
  } 
 f.Close();
}
