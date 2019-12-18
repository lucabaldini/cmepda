#include <TFile.h>
#include <TTree.h>
#include <TRandom.h>
#include <vector>
int main(){
TFile f("SimpleTree.root","RECREATE"); // Create file first. The TTree will be associated to it
TTree data("tree","Example TTree");    // No need to specify column names
double x, y, z, t; 
data.Branch("x",&x,"x/D");      // Associate variable pointer to column and specify its type, double
data.Branch("y",&y,"y/D");
data.Branch("z",&z,"z/D");
data.Branch("t",&t,"t/D");

std::vector<float> myFloats;
data.Branch("manyfloats",&myFloats);

for (int i = 0; i<128; ++i) { //Loop on 128 events
   x = gRandom->Uniform(-10,10); 
   y = gRandom->Gaus(0,5);
   z = gRandom->Exp(10);
   t = gRandom->Landau(0,2);      
   myFloats.clear();
   for(int j=0; j<i;j++) myFloats.push_back(j*t);

   data.Fill();                 // Make sure the values of the variables are recorded 
} 
data.Write();                   // Dump on the file
f.Close();
}
