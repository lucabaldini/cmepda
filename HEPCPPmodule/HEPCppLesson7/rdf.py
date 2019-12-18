import ROOT
rdf = ROOT.RDataFrame("Events",
                      "root://eospublic.cern.ch//eos/root-eos/cms_opendata_2012_nanoaod/Run2012B_DoubleMuParked.root");

#list available columns
print rdf.GetColumnNames()

sel0=rdf.Filter("nMuon>=2","two muons").Range(10000) #restrict to first 10k events with at least two muons
sel1=sel0.Filter("Muon_pt[0]>20","leading mu pt") 
sel2=sel1.Filter("Muon_charge[0]*Muon_charge[1]<0","opposite charge")

#create a C++ function to compute the mass
cppcode='''
float mass(float pt1, float eta1, float phi1, float pt2,float eta2, float phi2)
{
 TLorentzVector mu1,mu2;
 mu1.SetPtEtaPhiM(pt1,eta1,phi1,0.106);
 mu2.SetPtEtaPhiM(pt2,eta2,phi2,0.106);
 return (mu1+mu2).M();
}
'''
ROOT.gInterpreter.ProcessLine(cppcode)

#add mass
mass=sel2.Define("Dimuon_mass","mass(Muon_pt[0],Muon_eta[0],Muon_phi[0],Muon_pt[1],Muon_eta[1],Muon_phi[1])")

outCols=ROOT.vector("std::string")() #this creates a c++ std::vector<std::string> and wrap it in python
outCols.push_back("Dimuon_mass") 

mass.Snapshot("Events","out.root",outCols)


