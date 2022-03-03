# 3D Rendering in Pygame
![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Issues Open Badge](https://img.shields.io/github/issues/jweir136/PyGame-3D-Rendering.svg)

![Wireframe Cube Image](https://dm0qx8t0i9gc9.cloudfront.net/thumbnails/video/YWAdzU2/videoblocks-cubic-013-a-wireframe-cube-element-rotates-loop_srm1ncqwym_thumbnail-1080_01.png)

Pygame 3D Rendering is a 3D graphics rendering program build for Pygame. The app renders a shape from a custom wireframe file and projects the object onto the screen. The user can then use the keyboard controls to move the object around, and change the orientation.

## Installation

This project requires Python version 3.9.10, and two dependencies:

- pygame=="2.1.2"
- numpy=="1.22.2"

You can install these dependencies directly using the commnand `pip install -r requirements.txt`.

You can then run the program using the command `python3 main.py` while in the main project directory. This should run Pygame, and display a simple wireframe cube on the screen. Once the object has been rendered, you can move the camera around using the <i>left, right, up, and down arrows</i>. You can zoom in and out using the <i>plus and equals keys</i>. Finally, you can rotate the camera using the <i>q, w, a, and s keys</i>.