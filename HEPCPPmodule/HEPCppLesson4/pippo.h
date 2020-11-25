//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Mon Dec  9 18:02:17 2019 by ROOT version 6.08/00
// from TTree tree/A tree
// found on file: testWithObj.root
//////////////////////////////////////////////////////////

#ifndef pippo_h
#define pippo_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

class pippo {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.
   const Int_t kMaxmyParticles = 100;

   // Declaration of leaf types
   Int_t           myParticles_;
   Float_t         myParticles_m_px[kMaxmyParticles];   //[myParticles_]
   Float_t         myParticles_m_py[kMaxmyParticles];   //[myParticles_]
   Float_t         myParticles_m_pz[kMaxmyParticles];   //[myParticles_]
   Float_t         myParticles_m_e[kMaxmyParticles];   //[myParticles_]

   // List of branches
   TBranch        *b_myParticles_;   //!
   TBranch        *b_myParticles_m_px;   //!
   TBranch        *b_myParticles_m_py;   //!
   TBranch        *b_myParticles_m_pz;   //!
   TBranch        *b_myParticles_m_e;   //!

   pippo(TTree *tree=0);
   virtual ~pippo();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef pippo_cxx
pippo::pippo(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("testWithObj.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("testWithObj.root");
      }
      f->GetObject("tree",tree);

   }
   Init(tree);
}

pippo::~pippo()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t pippo::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t pippo::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void pippo::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("myParticles", &myParticles_, &b_myParticles_);
   fChain->SetBranchAddress("myParticles.m_px", myParticles_m_px, &b_myParticles_m_px);
   fChain->SetBranchAddress("myParticles.m_py", myParticles_m_py, &b_myParticles_m_py);
   fChain->SetBranchAddress("myParticles.m_pz", myParticles_m_pz, &b_myParticles_m_pz);
   fChain->SetBranchAddress("myParticles.m_e", myParticles_m_e, &b_myParticles_m_e);
   Notify();
}

Bool_t pippo::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void pippo::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t pippo::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef pippo_cxx
