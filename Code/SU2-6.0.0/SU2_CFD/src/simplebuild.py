import os
os.system("cd /home/pavani/Downloads/SU2-6.0.0")
os.system("./configre --prefix=/home/pavani/Downloads/SU2-6.0.0/hello")
os.system("make")
os.system("make install")
os.system("make -j 4 install")
