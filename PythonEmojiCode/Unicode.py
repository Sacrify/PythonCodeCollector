import os, sys, getopt, re, pdb, codecs

readFilePath = "Unicode"
writeFilePath = "Unicode2"
reprogram = re.compile("([0-9a-f]+),")

# main
opts, args = getopt.getopt(sys.argv[1:], "f:")

# Handle input
for op, value in opts:
	if op == "-f":
		readFilePath = value + ".csv"
		writeFilePath = value + "2" + ".csv"


readFileHandle = open (readFilePath)
writeFileHandle = codecs.open (writeFilePath, 'w+', encoding='utf-16')

readFileList = readFileHandle.readlines()
for readFileLine in readFileList:
	result = reprogram.search(readFileLine)
	unicodeString = result.group(1)
	unicodeResult = unicodeString.decode('hex').decode('utf-16')

	print unicodeResult
	writeFileHandle.write(unicodeResult)
	writeFileHandle.write("," + readFileLine)

readFileHandle.close()
writeFileHandle.close()

