# physics_simulator
A hobby project designed to test my software development skills and develop them, while at the same time teaching me more about how the world and space work.

# Feature Implementation 1.0

## Design Implementation Status
<UL>
<LI>[ ] Be able to display a single point in space inside a rendering window.
<LI>[ ] Be able to display a line with points on either end inside a rendering window.
<LI>[ ] Be able to display a 2D polygon with points on each vertex inside a rendering window.
<LI>[ ] Be able to display a 3D polygon with points on each vertex inside a rendering window.
<LI>[ ] Be able to display a 4D object with points on each vertex inside a rendering window.
<LI>[ ] Application Window
<LI>[ ] Title Bar with window controls
<UL>[ ] Menu Bar
    <LI>[ ] File
    <LI>[ ] Edit
    <LI>[ ] Help
    <LI>[ ] About
</UL>
<LI>[ ] Rendering Window
<LI>[ ] Status Bar
<LI>[ ] Toolbar and/or Toolbox
<UL>[ ] Properties Window
    <LI>[ ] Properties Bar
    <LI>[ ] Properties Panel
</UL>
<LI>[ ] Rendering Window Controls
<LI>[ ] Realtime calculation peephole, also displaying the cursor's coordinates in the 3D space in real-time
<LI>[ ] implement requirements.txt for the items in the list.
<LI>[ ] PyQt6 - Python bindings for the Qt cross-platform application framework.
<LI>[ ] PyOpenGL - Python bindings for the OpenGL graphics library.
<LI>[ ] PyOpenGL-accelerate - Python bindings for the OpenGL graphics library.
<LI>[ ] NumPy - Python library for numerical computing.
<LI>[ ] SciPy - Python library for scientific computing.
<LI>[ ] GLFW - Python bindings for the GLFW library.
<LI>[ ] PyInstaller - Python library for creating standalone executables from Python scripts.
<LI>[ ] SCons - CONSIDERATION ONLY
</UL>

## requirements.txt
Implemented requirements.txt for the baseline design with the following dependencies:
<UL>
<LI>PyQt6=6.7.1</LI>
<LI>PyOpenGL=3.1.7</LI>
<LI>Numpy=2.1.1</LI>
<LI>SciPy=1.14.1</LI>
<LI>GLFW=2.7.0</LI>
<LI>PyInstaller=6.10.0</LI>
</UL>

Since I'm building from scratch, I decided I might as well use the cutting edge versions as the base specs. Note that in this version, PyOpenGL_accelerate is downloaded as a built distribution to reduce other dependencies. This version only supports Windows amd64 architectures. Support for other architectures will be added in the future.