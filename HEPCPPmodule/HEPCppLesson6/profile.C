{
  TFile* f = TFile::Open("Workspace_mumufit.root");
  RooWorkspace* w = (RooWorkspace*)f->Get("ws");
  w->Print();
  double xL = w->var("meanJpsi")->getVal() - 2.2* w->var("meanJpsi")->getError();
  double xU = w->var("meanJpsi")->getVal() + 2.2* w->var("meanJpsi")->getError();
  cout << xL << "," << xU << endl;
  w->var("meanJpsi")->setRange(xL, xU);
  RooNLLVar nll("nll","nll",*(w->pdf("totPDF")),*(w->data("data"))) ;
  RooProfileLL pll("pll","pll", nll,*w->var("meanJpsi"));
  RooPlot* frame = w->var("meanJpsi")->frame(xL, xU) ;
  pll.plotOn(frame) ;
  frame->Draw();
  frame->GetYaxis()->SetRangeUser(0.0, 3.0);
  TLine* lineNLL = new TLine(xL, 0.5, xU, 0.5);
  lineNLL->SetLineColor(kRed);
  lineNLL->SetLineStyle(kDashed);
  TLine* lineL = new TLine(w->var("meanJpsi")->getVal()-w->var("meanJpsi")->getError(), 0,  
			   w->var("meanJpsi")->getVal()-w->var("meanJpsi")->getError(), 3);
  lineL->SetLineColor(kBlack);
  lineL->SetLineStyle(kDashed);
  TLine* lineU = new TLine(w->var("meanJpsi")->getVal()+w->var("meanJpsi")->getError(), 0,  
			   w->var("meanJpsi")->getVal()+w->var("meanJpsi")->getError(), 3);
  lineU->SetLineColor(kBlack);
  lineU->SetLineStyle(kDashed);
  lineNLL->Draw("same");
  lineL->Draw("same");
  lineU->Draw("same");
}
