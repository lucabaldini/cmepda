{
  ROOT::EnableImplicitMT();   
  ROOT::RDataFrame df("tree", "tree_py.root", {"px", "py"});
  auto df2 = df.Filter("px > 0")
    .Define("pT2", "px*px + py*py");
  auto rHist = df2.Histo1D("pT2");
  rHist->Draw();
  df2.Snapshot("newtree", "out.root");
}
