import os
from mayavi.core.api import Engine
from mayavi.sources.vtk_file_reader import VTKFileReader
from mayavi.modules.surface import Surface

vtkFile = 'flow.vtk'

# Create the MayaVi engine and start it.
engine = Engine()
engine.start()
scene = engine.new_scene()

# Read in VTK file and add as source
reader = VTKFileReader()
reader.initialize(vtkFile)
engine.add_source(reader)

# Add Surface Module
surface = Surface()
engine.add_module(surface)

# Move the camera
scene.scene.camera.elevation(-70)

# Save scene to image file
scene.scene.save_png('image.png')

# Create a GUI instance and start the event loop.
# This stops the window from closing
from enthought.pyface.api import GUI
gui = GUI()
gui.start_event_loop()

#(text processing)
