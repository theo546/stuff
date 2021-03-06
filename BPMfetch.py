import os

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles

array = []

dirName = '/home/theo546/Musique'
listOfFiles = getListOfFiles(dirName)
for file in listOfFiles:
    filename, file_extension = os.path.splitext(file)
    if file_extension == ".mp3" or file_extension == ".flac":
        result = os.popen('ffprobe "' + file + '" 2>&1 | grep "BPM" | sed "s/ //g"').read()
        if result != '':
            result = result.split(':')
            result = result[1].strip('\n')
            array.append([result, file])

for file in sorted(array):
    print(file)