import os, operator

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

array_style_list = {}

dirName = '/home/theo546/Musique'
listOfFiles = getListOfFiles(dirName)
for file in listOfFiles:
    filename, file_extension = os.path.splitext(file)
    if file_extension == ".mp3" or file_extension == ".flac":
        result = os.popen('ffprobe "' + file + '" 2>&1 | grep "GENRE" | sed "s/ //g"').read()
        if result != '':
            result = result.split(':')
            result = result[1].strip('\n')
            if result not in array_style_list:
                array_style_list[result] = 0
            array_style_list[result] = array_style_list[result] + 1

sorted_array = sorted(array_style_list.items(), key=operator.itemgetter(1))
sorted_array.reverse()
print(sorted_array)