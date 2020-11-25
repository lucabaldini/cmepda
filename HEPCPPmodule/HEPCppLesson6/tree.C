#include "TFile.h"
#include "TTree.h"
#include "TH2.h"
#include "TRandom.h"
#include <chrono> 
#include <iostream> 

using namespace std::chrono; 
using namespace std; 

void make_tree(Int_t nevents=100)
{

  auto start = high_resolution_clock::now(); 

  TFile* file = new TFile("tree_C.root","RECREATE", "");
  TTree* tree = new TTree("tree","A simple Tree with simple variables");
  Float_t px, py, pz;
  Double_t random;
  Int_t ev;
  tree->Branch("px",&px,"px/F");
  tree->Branch("py",&py,"py/F");
  tree->Branch("pz",&pz,"pz/F");
  tree->Branch("random",&random,"random/D");
  tree->Branch("ev",&ev,"ev/I");

  //fill the tree
  for (Int_t i = 0 ; i<nevents ; i++) {
    if(i%5000==0) std::cout << "Processing event number " << i << std::endl;
    gRandom->Rannor(px,py);
    pz = px*px + py*py;
    random = gRandom->Rndm();
    ev = i;
    tree->Fill();
  }

  //save the Tree header. The file will be automatically closed
  //when going out of the function scope
  tree->Write();

  auto stop = high_resolution_clock::now(); 
  auto duration = duration_cast<milliseconds>(stop - start);  
  std::cout << tree->GetEntries() << " events done in " << duration.count()/1000. << " seconds" << std::endl; 

}


void read_tree()
{

  TFile *infile = new TFile("tree_C.root", "READ");
  if(infile->IsZombie()){
    std::cout << "No file named tree_C.root could be opened. Return." << std::endl;
    return;
  }
  TTree *tree = (TTree*)infile->Get("tree");
  Float_t px, py, pz;
  Double_t random;
  Int_t ev;
  tree->SetBranchAddress("px",&px);
  tree->SetBranchAddress("py",&py);
  tree->SetBranchAddress("pz",&pz);
  tree->SetBranchAddress("random",&random);
  tree->SetBranchAddress("ev",&ev);
  //create two histograms
  TH1F *hpx   = new TH1F("hpx","px distribution",100,-3,3);
  TH2F *hpxpy = new TH2F("hpxpy","py vs px",30,-3,3,30,-3,3);
  //read all entries and fill the histograms
  Long64_t nentries = tree->GetEntries();

  auto start = high_resolution_clock::now(); 
  for (Long64_t i = 0; i < nentries; i++) {
    tree->GetEntry(i);
    hpx->Fill(px);
    hpxpy->Fill(px,py);
  }

  auto stop = high_resolution_clock::now(); 
  auto duration = duration_cast<milliseconds>(stop - start);
  std::cout << tree->GetEntries() << " read in " << duration.count()/1000. << " seconds" << std::endl;

  hpx->Draw("HISTE");
  TFile* outfile = new TFile("histos.root", "RECREATE");
  hpx->Write();
  outfile->Close();

}
