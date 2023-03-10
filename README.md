# Animated FBX Exporter
A Blender plugin to quickly export your selected rigged character using three different export presets

![image](https://user-images.githubusercontent.com/13683581/224740878-6bb9028b-bf9c-4f8a-91fe-a669d5139b7a.png)

## Installation:
Download `animated_fbx_exporter.py` and install it via Blender Preferences

## Usage:
1. Set a target directory
2. Select your Meshes, then lastly the rig to make it the active object. 
3. Run the export using one of the buttons (There will be no popup window or confirmation dialog)


## Export Options:
### A: Export without animations: 

Useful where you just want to export a blank rigged character, maybe because you want to link the animations externally.

            
### B: Export with Active Animation:

Exports the rig only with the currently active action/animation. Useful if you want to export animations as seperate FBX files.

### C: Export with All Animations

The default export behavior. All actions are included in the exported file.
