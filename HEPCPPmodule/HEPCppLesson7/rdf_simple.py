import ROOT
rdf=ROOT.RDataFrame("ntuple","/home/arizzi/root/tutorials/hsimple.root")
h=rdf.Filter("px>py").Define("somma","px+py").Histo1D(("somma","titolo",10,-2,+2),"somma")
h.Draw()

input()
