#include <iostream>
#include <TFile.h>
#include <TTree.h>
#include <vector>
#include <TSystem.h>
int main()
{
 TFile f("test.root","RECREATE");
 TTree t("tree","A tree");

 float x[100];
 int n;
 t.Branch("n",&n,"n/I");
 t.Branch("myFloats",x,"x[n]/F");

 for(int i=0;i<100; i++) { // loop on events
    n=i;
    for(int j=0;j<n; j++) { // loop on particles per event
        x[j]=i*j;
    }
    t.Fill();
 } 
 t.Write();
 f.Close();
}
