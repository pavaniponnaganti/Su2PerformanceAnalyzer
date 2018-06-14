import os
import subprocess
out=subprocess.getoutput("cd locate SU2-6.0.0 | grep /SU2-6.0.0$")
os.system("./configre --prefix="+out)
os.system("make")
os.system("make install")
os.system("make -j 4 install")
