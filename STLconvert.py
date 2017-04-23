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

def formatTC(timecode):
	timecode = timecode.replace(';',':')
	timecode = timecode+"0"
	Slist = list(timecode)
	Slist[8] = ","
	timecode = "".join(Slist)
	return timecode

def parsefile(filename):
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
			TCin = formatTC(TCin)
			TCout = formatTC(TCout)
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
	print("opening: "+filename+"\n")
	parsefile(filename)
	print("\nComplete! Always remember to have fun.")

main(filename)