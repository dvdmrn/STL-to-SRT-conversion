"""
    Converts a .stl subtitle file into a .srt file
    HOW TO USE:
        1. Open a terminal window and type: `python STLconvert.py``
        2. Enter the file path
        3. Enter the project's framerate
        4. The converted file will be outputted in this folder.
"""


import sys
# import io

inputList = []
outputList = []

ignoreList = [
             "@ This file written",
             "<begin subtitles>",
             "<end subtitles>",
             ]
title = "    ____ _____ _        __   ____  ____ _____ \n   / ___|_   _| |       \ \ / ___||  _ \_   _|\n   \___ \ | | | |   _____\  \___ \| |_) || |  \n  _ ___) || | | |__|_____/ / ___) |  _ < | |  \n (_)____/ |_| |_____|   /_(_)____/|_| \_\|_|  \n_________                               _____             \n__  ____/_______________   _______________  /_____________\n_  /    _  __ \_  __ \_ | / /  _ \_  ___/  __/  _ \_  ___/\n/ /___  / /_/ /  / / /_ |/ //  __/  /   / /_ /  __/  /    \n\____/  \____//_/ /_/_____/ \___//_/    \__/ \___//_/     \n\n"
def formatTC(timecode,fps):
    timecode = timecode.replace(';',':')
    frames = timecode[-2:]
    if(float(frames)>=float(fps)):
        print("\n    --warning--\n    timecode `"+timecode+"` frame index exceeds or is equal to framerate.\n")
    framesToMs = "{0:.3f}".format(float(frames)/float(fps))[-3:]
    timecode = timecode[:-2]+framesToMs
    Slist = list(timecode)
    Slist[8] = ","
    timecode = "".join(Slist)
    return timecode

def parsefile(filename,fps):
    lineNumber = 0
    with open(filename) as inputfile:
        for line in inputfile:
            inputList.append(line.strip())

    for line in inputList:
        if ';' in line:
            lineNumber += 1
            TCin = line[:11]
            TCout = line[12:23]
            TCin = formatTC(TCin,fps)
            TCout = formatTC(TCout,fps)
            TCline = TCin+" --> "+TCout

            outputList.append(lineNumber)
            outputList.append(TCline)
            print("formatted: "+line+" =>> "+TCline)
        else:
            outputList.append(line)

    with open(filename[:-4]+'_converted.srt','w') as outputFile:
        print("\n........................................\noutputting file as: "+filename[:-4]+'_converted.srt\n........................................')
        for e in outputList:
            write = True
            for item in ignoreList:
                if item in str(e):
                    write=False
            if(write):
                outputFile.write("%s\n" % e)

def main():
    print(title)
    filename = raw_input('enter file path: ')
    if(".stl" not in filename):
        print("Invalid filename. Remember to include the .stl extension!")
        return
    fps = raw_input('enter framerate: ')
    try:
        float(fps)
    except Exception as e:
        print("Invalid framerate.")
        return
    print("\n========================================\nopening: "+filename+"\n")
    parsefile(filename,fps)
    raw_input("\n========================================\nComplete! Always remember to have fun.")

main()