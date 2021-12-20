import ROOT
ROOT.gInterpreter.ProcessLine('#include "../HEPCppLesson1/Assignment2/fourvector.h"')
rdf = ROOT.RDataFrame("Events",
                      "root://eospublic.cern.ch//eos/root-eos/cms_opendata_2012_nanoaod/Run2012B_DoubleMuParked.root");

#list available columns
print(rdf.GetColumnNames())
mass=rdf.Range(1000).Define("Muon_p4","ROOT::VecOps::Construct<VectorPtEtaPhiMass<float>>(Muon_pt,Muon_eta,Muon_phi,Muon_mass)")\
    .Define("goodmu","Muon_pt > 20 && abs(Muon_eta) < 2.0  ")\
    .Filter("Sum(goodmu)>=2")\
    .Define("mu0","Nonzero(goodmu)[0]")\
    .Define("oppositeCharge","goodmu && Muon_charge[mu0]*Muon_charge<0")\
    .Filter("Sum(oppositeCharge)>0")\
    .Define("mu1","Nonzero(oppositeCharge)[0]")\
    .Define("Dimuon_mass","(Muon_p4[mu0]+Muon_p4[mu1]).m()")

mass.Display("").Print()

#outCols=ROOT.vector("std::string")() #this creates a c++ std::vector<std::string> and wrap it in python
#outCols.push_back("Dimuon_mass") 

#mass.Snapshot("Events","out.root",outCols)

import pandas
print(pandas.DataFrame(mass.AsNumpy(["Dimuon_mass","mu0","mu1","event","run"])))


