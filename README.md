# STL-to-SRT-conversion
### Converts an .stl closed captioning file to .srt format
*This hasn't been robustly tested, let me know if there are any errors!*

# How to use:
### If you already have Python installed:
- Open a terminal window, navigate to where STLconvert.py is located, and type `python STLconvert.py`
- Enter the filepath of your .stl file. For example, if it's named 'myClosedCaptioningFile.stl', and if it is located in the same folder as STLconvert.py, you can just type `myClosedCaptioningFile.stl`
- STLconvert will output your file in the same folder that it lives in.

### If you are on Windows and do not want to install Python:
- Go into windows_exe>dist and open STLconvert.exe
- Enter the filepath to your .stl file. For example, if it is located in the same folder that STLconvert.exe is located, you can just type `myClosedCaptioningFile.stl`. If you like to keep everything somewhere specific, you can type: `C:\<THE_PATH_TO_YOUR_FILE>\myClosedCaptioningFile.stl`
- STLconvert.exe will output your new .srt file in the same folder that STLconvert.exe is living in, and will name it `<NAME_OF_YOUR_OLD_STL_FILE>_converted.srt`

### Troubleshooting:
- If you are using a windows computer you will need python in your path.
