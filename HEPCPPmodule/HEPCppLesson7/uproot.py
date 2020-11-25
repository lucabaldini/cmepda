import uproot
import os
if not os.path.exists('DataSet_highstat.root'):
    os.system('wget -O DataSet_highstat.root cern.ch/arizzi/out.root')


tree = uproot.open("DataSet_highstat.root")["Events"]

massdata=tree.array("Dimuon_mass")
print(massdata)

#Draw with matplot lib
import matplotlib.pyplot as plt
n, bins, patches = plt.hist(massdata, 50, (0,5) )
plt.show()




