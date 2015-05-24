import os, re, pdb, codecs

readFilePath = "Unicode"
writeFilePath = "Unicode2"
reprogram = re.compile("([0-9a-f]+),")

readFileHandle = open (readFilePath)
writeFileHandle = codecs.open (writeFilePath, 'w+', encoding='utf-16')

readFileList = readFileHandle.readlines()
for readFileLine in readFileList:
	result = reprogram.search(readFileLine)
	unicodeString = result.group(1)
	unicodeResult = unicodeString.decode('hex').decode('utf-16')

	print unicodeResult
	writeFileHandle.write(unicodeResult)

readFileHandle.close()
writeFileHandle.close()

