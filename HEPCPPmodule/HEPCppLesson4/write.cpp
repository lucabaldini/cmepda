#include "fourvector.h"
#include <iostream>
#include <TFile.h>
#include <TTree.h>
#include <vector>
#include <TSystem.h>
int main()
{
 std::vector<FourVector> particles;
 TFile f("testWithObj.root","RECREATE");
 TTree t("tree","A tree");
 gInterpreter->GenerateDictionary("FourVector","fourvector.h");
 gInterpreter->GenerateDictionary("FourVectors","fourvector.h");
 t.Branch("myParticles",&particles);
 for(int i=0;i<100; i++) { // loop on events
    particles.clear();
    for(int j=0;j<100; j++) { // loop on particles per event
	particles.emplace_back(i,j/2.,0,0);
    }
    t.Fill();
 } 
 t.Write();
 f.Close();
}
