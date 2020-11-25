# Declare Factory
from ROOT import TMVA, TFile, TTree, TCut, TString

# Declare Variables in DataLoader
TMVA.Tools.Instance()

inputFile = TFile.Open("https://github.com/iml-wg/tmvatutorials/raw/master/inputdata.root")
outputFile = TFile.Open("TMVAOutputDNN.root", "RECREATE")

factory = TMVA.Factory("TMVAClassification", outputFile,
                       "!V:!Silent:Color:!DrawProgressBar:AnalysisType=Classification" )

# Declare Variables in DataLoader
loader = TMVA.DataLoader("dataset_dnn")

loader.AddVariable("var1")
loader.AddVariable("var2")
loader.AddVariable("var3")
loader.AddVariable("var4")
loader.AddVariable("var5 := var1-var3")
loader.AddVariable("var6 := var1+var2")

# Setup Dataset(s)
tsignal = inputFile.Get("Sig")
tbackground = inputFile.Get("Bkg")

loader.AddSignalTree(tsignal)
loader.AddBackgroundTree(tbackground) 
loader.PrepareTrainingAndTestTree(TCut(""),
                                  "nTrain_Signal=1000:nTrain_Background=1000:SplitMode=Random:NormMode=NumEvents:!V")

# Configure Network Layout

# General layout
layoutString = TString("Layout=TANH|128,TANH|128,TANH|128,LINEAR");

# Training strategies
training0 = TString("LearningRate=1e-1,Momentum=0.9,Repetitions=1,"
                        "ConvergenceSteps=2,BatchSize=256,TestRepetitions=10,"
                        "WeightDecay=1e-4,Regularization=L2,"
                        "DropConfig=0.0+0.5+0.5+0.5, Multithreading=True")

training1 = TString("LearningRate=1e-2,Momentum=0.9,Repetitions=1,"
                        "ConvergenceSteps=2,BatchSize=256,TestRepetitions=10,"
                        "WeightDecay=1e-4,Regularization=L2,"
                        "DropConfig=0.0+0.0+0.0+0.0, Multithreading=True")

trainingStrategyString = TString("TrainingStrategy=")
trainingStrategyString += training0 + TString("|") + training1

# General Options
dnnOptions = TString("!H:!V:ErrorStrategy=CROSSENTROPY:VarTransform=N:"
        "WeightInitialization=XAVIERUNIFORM")
dnnOptions.Append(":")
dnnOptions.Append(layoutString)
dnnOptions.Append(":")
dnnOptions.Append(trainingStrategyString)

# Booking Methods
# Standard implementation, no dependencies.
stdOptions =  dnnOptions + ":Architecture=STANDARD"
factory.BookMethod(loader, TMVA.Types.kDNN, "DNN", stdOptions)


# Train Methods
factory.TrainAllMethods()

# Test and Evaluate Methods
factory.TestAllMethods()
factory.EvaluateAllMethods()

# Plot ROC Curve
# %jsroot on
c = factory.GetROCCurve(loader)
c.Draw()
c.Print("result.png") # added 
