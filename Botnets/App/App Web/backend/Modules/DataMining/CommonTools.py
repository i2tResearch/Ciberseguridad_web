from os import walk

def getFilesOfSpecificLocation(location):
    f = []
    for (dirpath, dirnames, filenames) in walk(location):
            f.extend(filenames)
            break
    return f
