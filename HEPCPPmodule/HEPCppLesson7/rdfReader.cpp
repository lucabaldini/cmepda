#include <ROOT/RDataFrame.hxx>
#include <TH1D.h>

auto rdfReader(){

   auto rdf = ROOT::RDataFrame("ntuple","/home/arizzi/root/tutorials/hsimple.root");
   auto h= rdf.Filter("px>py").Histo1D({"pz","titolo",10,-2,2},"pz");
   h->Draw();
   return h;


}
