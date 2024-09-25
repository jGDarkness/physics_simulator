# Ticket Requirements
Feature Design: Design a list of features to include in the application, along with their basic interface layout and elements. Determine the Python Libraries/Modules/APIs to use in order to achieve the desired results. The initial Feature Design should be limited to a total of 5 features for Iteration 1.0

## List of Basic Features to Include in the Application (Limited to 5 features)
1. Be able to display a single point in space inside a rendering window.
2. Be able to display a line with points on either end inside a rendering window.
3. Be able to display a 2D polygon with points on each vertex inside a rendering window.
4. Be able to display a 3D polygon with points on each vertex inside a rendering window.
5. Be able to display a 4D object with points on each vertex inside a rendering window.

## Basic Interface Layout and Elements
Note: The elements listed below don't need to be complete for the feature design 1.0, but at least functional placeholders need to be implemented so that future features can be implemented and integrated as needed.

- Application Window
- Title Bar with window controls
- Menu Bar
    - File
    - Edit
    - Help
    - About
- Rendering Window
- Status Bar
- Toolbar and/or Toolbox
- Properties Window
    - Properties Bar
    - Properties Panel
- Rendering Window Controls
- Realtime calculation peephole, also displaying the cursor's coordinates in the 3D space in real-time

## Python Libraries/Modules/APIs to Use
- implement requirements.txt for the items in the list.
- PyQt6 - Python bindings for the Qt cross-platform application framework.
- PyOpenGL - Python bindings for the OpenGL graphics library.
- PyOpenGL-accelerate - Python bindings for the OpenGL graphics library.
- NumPy - Python library for numerical computing.
- SciPy - Python library for scientific computing.
- GLFW - Python bindings for the GLFW library.
- PyInstaller - Python library for creating standalone executables from Python scripts.
- SCons - CONSIDERATION ONLY

## Related follow-on requirements
- Update Readme.md to include the features to be in the next release.
- Document the hardware supported, including the operating system, CPU, and GPU.

## Additional Notes
- These feature design requirements are not expected to be exhaustive detailed documents, but a framework to work from. The individual elements are allowed to have separate more detailed design/requirement documents as they are developed. For example, the Menu Bar will have only placeholders in in Feature Implementation 1.0, but will have a more detailed design/requirement document when it's time to add the actual contents and functionality for each item.

- Remember to include documentation updates in all tickets going forward.