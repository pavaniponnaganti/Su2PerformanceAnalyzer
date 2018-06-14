from mayavi import mlab
from tvtk.api import tvtk
from tvtk.common import * 
import matplotlib.pyplot as plt

# Make a figure with a black background
fig = mlab.figure(bgcolor=(0,0,0))
fig.scene.camera.azimuth(215)

source = mlab.pipeline.open('flow.vtk')

# Show the surface, colored by the scalars
surf = mlab.pipeline.surface(source)

# Draw contours of the scalars on the surface
lines = mlab.pipeline.contour_surface(source)

#TESTING #1
#lines = mlab.plot3d(source)

#mlab.savefig(filename='test.ps',size=(300,300), magnification=2)
#plt.colorbar()  # draw colorbar

mlab.show()
