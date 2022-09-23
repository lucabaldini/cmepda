import ROOT
rdf = ROOT.RDataFrame("Events",
                      "DataSet_highstat.root")

h=rdf.Histo1D("Dimuon_mass")
h.Draw()
input()

