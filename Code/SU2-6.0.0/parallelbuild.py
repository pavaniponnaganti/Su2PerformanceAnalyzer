import os
import subprocess
out=subprocess.getoutput("locate SU2-6.0.0 | grep /SU2-6.0.0$")
#os.system("cd locate SU2-6.0.0 | grep /SU2-6.0.0$")
os.system("./configure --prefix="+out+" CXXFLAGS=\"-03\" --enable-mpi --with-cc=/usr/local/etc/alternatives/mpicc --with-cxx=/usr/local/etc/alternatives/mpicxx")
os.system("make")
os.system("make install")
os.system("make -j 4 install")
os.system("CXXFLAGS=\"-03\"")
os.system("--enable-mpi --with-cc=/usr/local/etc/alternatives/mpicc --with-cxx=/usr/local/etc/alternatives/mpicxx")
