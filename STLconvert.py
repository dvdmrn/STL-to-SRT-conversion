"""
	Converts a .stl subtitle file into a .srt file
	HOW TO USE:
		Open a terminal window and type: `python STLconvert.py <YOUR_FILE_NAME>`
			>Example: python STLconvert.py myClosedCaptioningFile.srt
		Be sure to include the file extension!
"""


import sys
import io

if len(sys.argv)==2:
	filename = sys.argv[1]
else:
	print("please supply a filename as a command line argument")
	exit()
inputList = []
outputList = []

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
	        inputList.append(line.strip().split(','))

	for line in inputList:
		if ';' in line[0]:
			lineNumber += 1
			line[0].replace(";",":")
			TCin = line[0][:11]
			TCout = line[0][12:23]
			TCin = formatTC(TCin,fps)
			TCout = formatTC(TCout,fps)
			TCline = TCin+" --> "+TCout

			outputList.append([lineNumber])
			outputList.append([TCline])
			print("formatted: "+line[0]+" =>> "+TCline)
		else:
			outputList.append(line)

	with open(filename[:-4]+'_converted.srt','w') as outputFile:
		print("outputting file as: "+filename[:-4]+'_converted.srt')
		for e in outputList:
			outputFile.write("%s\n" % e[0])

def main(filename):
	if(".stl" not in filename):
		print("Invalid filename. Remember to include the .stl extension!")
		return
	fps = raw_input('enter framerate: ')
	try:
		float(fps)
	except Exception as e:
		print("Invalid framerate.")
		return
	print("opening: "+filename+"\n")
	parsefile(filename,fps)
	print("\nComplete! Always remember to have fun.")

main(filename)