import ROOT

from sys import exit, argv

import time

try:
    import numpy as np
except:
    print("Failed to import numpy.")
    exit()

# Helper function to create an example tree
def make_tree(nevents):
    outfile = ROOT.TFile("tree_py.root", "RECREATE")
    tree = ROOT.TTree("tree", "A simple Tree with simple variables")
    px = np.empty((1), dtype="float32")
    py = np.empty((1), dtype="float32")
    pz = np.empty((1), dtype="float32")
    random = np.empty((1), dtype="float64")
    ev = np.empty((1), dtype="int32")
    tree.Branch("px", px, "px/F")
    tree.Branch("py", py, "py/F")
    tree.Branch("pz", pz, "pz/F")
    tree.Branch("random", random, "random/D")
    tree.Branch("ev", ev, "ev/I")
    for i in range(nevents):
        px[0] = np.random.normal()
        py[0] = np.random.normal()
        pz[0] =  px[0]**2 + py[0]**2
        random[0] = np.random.random_sample()
        ev[0] = i
        tree.Fill()
    outfile.Write()
    return (outfile), tree

if __name__ == '__main__':
    clock = time.time()
    _, tree = make_tree(int(argv[1]))
    clock -= time.time()
    print(('%s events done in ' % tree.GetEntries())+'{}'.format(-clock)+' seconds')

    if tree.GetEntries()<=10:
        ROOT.ROOT.EnableImplicitMT()    
        array, labels = tree.AsMatrix(return_labels=True)
        print(array.shape)
        print("Return numpy array and labels:\n{}\n{}\n".format(labels, array))
