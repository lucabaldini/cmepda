#Import the ROOT libraries
import ROOT

#The observable
mass = ROOT.RooRealVar("Dimuon_mass","#mu^{+}#mu^{-} invariant mass",2.6,4.5,"GeV")
mass.setBins(100)

import os
if not os.path.exists('DataSet_highstat.root'):
    os.system('wget -O DataSet_highstat.root cern.ch/arizzi/out.root')

fInput = ROOT.TFile("DataSet_highstat.root")
tree = fInput.Get("Events")
dataset_unbinned = ROOT.RooDataSet("data_unbinned", "", tree, ROOT.RooArgSet(mass) )
dataset = ROOT.RooDataHist("data", "", ROOT.RooArgSet(mass), dataset_unbinned )

#The Jpsi signal parametrization: we'll use a Crystal Ball
meanJpsi = ROOT.RooRealVar("meanJpsi","The mean of the Jpsi Gaussian",3.1,2.8,3.2)
sigmaJpsi = ROOT.RooRealVar("sigmaJpsi","The width of the Jpsi Gaussian",0.3,0.0001,1.)
alphaJpsi = ROOT.RooRealVar("alphaJpsi","The alpha of the Jpsi Gaussian",1.5,-5.,5.)
nJpsi = ROOT.RooRealVar("nJpsi","The alpha of the Jpsi Gaussian",1.5,0.5,10.)

CBJpsi = ROOT.RooCBShape("CBJpsi","The Jpsi Crystall Ball",mass,meanJpsi,sigmaJpsi,alphaJpsi,nJpsi)

#The psi(2S) signal parametrization: width will be similar to Jpsi core of the CB (almost Gaussian)
meanpsi2S = ROOT.RooRealVar("meanpsi2S","The mean of the psi(2S) Gaussian",3.7,3.65,3.75)
#sigmapsi2S = ROOT.RooRealVar("sigmapsi2S","The width of the Jpsi Gaussian",0.3,0.0001,1.)
gausspsi2S = ROOT.RooGaussian("gausspsi2S","The psi(2S) Gaussian",mass,meanpsi2S,sigmaJpsi)
#alphapsi2S = ROOT.RooRealVar("alphapsi2S","The alpha of the Jpsi Gaussian",-1.5,-5.,1.)
#npsi2S =  ROOT.RooRealVar("npsi2S","The alpha of the Jpsi Gaussian",5.5,0.1,10.)
#gausspsi2S  = ROOT.RooCBShape("gausspsi2S", "", mass, meanpsi2S, sigmapsi2S, alphapsi2S,npsi2S)


#Background parametrization: just a polynomial
a1 = ROOT.RooRealVar("a1","The a1 of background",-0.7,-2.,2.)
a2 = ROOT.RooRealVar("a2","The a2 of background",0.3,-2.,2.)
a3 = ROOT.RooRealVar("a3","The a3 of background",-0.03,-2.,2.)
a4 = ROOT.RooRealVar("a4","The a4 of background",-0.0,-10.,10.)
a5 = ROOT.RooRealVar("a5","The a4 of background",-0.0,-10.,10.)
a6 = ROOT.RooRealVar("a6","The a4 of background",-0.0,-10.,10.)
backgroundPDF = ROOT.RooChebychev("backgroundPDF","The background PDF",mass,ROOT.RooArgList(a1,a2,a3,a4,a5,a6))

#Define the yields
NJpsi = ROOT.RooRealVar("NJpsi","The Jpsi signal events",1000000.,0.1,3000000.)
Nbkg = ROOT.RooRealVar("Nbkg","The bkg events",500000.,0.1,2000000.)

#Now define the number of psi(2S) events as a product of crss section*efficiency*luminosity (in pb)
#Let's assume we measured the trigger, reconstruction and identification efficiency for dimuons and found it to be 95%
#Lowstat sample has 0.64 pb-1
#Fullstat sample has 37 pb-1
eff_psi = ROOT.RooRealVar("eff_psi","The psi efficiency",0.75,0.00001,1.)
lumi_psi  = ROOT.RooRealVar("lumi_psi","The CMS luminosity",11600, 0.00001,12000.,"pb-1")
cross_psi = ROOT.RooRealVar("cross_psi","The psi xsec",10.,0.,4000.,"pb")

#Now define the number of psi events
Npsi = ROOT.RooFormulaVar("Npsi","@0*@1*@2",ROOT.RooArgList(eff_psi,lumi_psi,cross_psi))

#Important! We cannot fit simultaneously the efficiency, the luminosity and the cross section (our total PDF is only sensitive on the product of the three)
#We need to fix two of them, so we'll keep our POI floating
#One can also add an additional PDF to give predictive power on the other two parameters (later)
eff_psi.setConstant(1)
lumi_psi.setConstant(1)

#Compose the total PDF
totPDF = ROOT.RooAddPdf("totPDF","The total PDF",ROOT.RooArgList(CBJpsi,gausspsi2S,backgroundPDF),ROOT.RooArgList(NJpsi,Npsi,Nbkg))

#Do the actual fit
totPDF.fitTo(dataset, ROOT.RooFit.Extended(1))

#Print values of the parameters (that now reflect fitted values and errors)
print "##############"
meanpsi2S.Print()
NJpsi.Print()
Npsi.Print()
cross_psi.Print()
print "##############"

#Now plot the data and the fit result
xframe = mass.frame()
dataset.plotOn(xframe)
totPDF.plotOn(xframe)

#One can also plot the single components of the total PDF, like the background component
totPDF.plotOn(xframe, ROOT.RooFit.Components("backgroundPDF"), ROOT.RooFit.LineStyle(ROOT.kDashed), ROOT.RooFit.LineColor(ROOT.kRed))


#Draw the results
c1 = ROOT.TCanvas()
xframe.Draw()
c1.SaveAs("exercise_0.png")

#Now save the data and the PDF into a Workspace, for later use for statistical analysis
fOutput = ROOT.TFile("Workspace_mumufit_highstat.root","RECREATE")
fInput.cd()
ws = ROOT.RooWorkspace("ws") 
getattr(ws,'import')(totPDF)
getattr(ws,'import')(dataset)
ws.writeToFile("Workspace_mumufit_highstat.root")
del ws

#ws.Write()
fOutput.Write()
fOutput.Close()

input()
