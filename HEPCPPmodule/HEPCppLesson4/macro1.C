TGraphErrors * macro1(){
   // The number of points in the data set
   const int n_points = 10;
   // The values along X and Y axis
   double x_vals[n_points] = {1,2,3,4,5,6,7,8,9,10};
   double y_vals[n_points] = {6,12,14,20,22,24,35,45,44,53};
   // The errors on the Y axis
   double y_errs[n_points] = {5,5,4.7,4.5,4.2,5.1,2.9,4.1,4.8,5.43};

   // Instance of the graph
   auto graph = new TGraphErrors(n_points,x_vals,y_vals,nullptr,y_errs);
   graph->SetMarkerStyle(kOpenCircle);
   graph->SetMarkerColor(kRed);
   graph->Draw("APE");
   auto f = new TF1("Linear law","[0]+x*[1]",.5,10.5);
   // Let's make the function line nicer
   f->SetLineColor(kRed); 
   f->SetLineStyle(2);
   // Set parameters
   f->SetParameters(-1,5);
   graph->GetXaxis()->SetNdivisions(3, 0, 0);
   f->Draw("Same");
   graph->SetTitle("Measurement XYZ;length [#mu m];Arb.Units");
   auto legend = new TLegend(.1,.7,.3,.9,"Lab. Lesson 1");
   legend->AddEntry(graph,"Exp. Points","PE");
   legend->AddEntry(f,"Th. Law","L");
   legend->Draw();
  
   return graph;
}

