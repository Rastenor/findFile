import os
import argparse

myParser = argparse.ArgumentParser(description = "Searches for targetDir for files ending in suffix")
myParser.add_argument(
    "sfx",
    metavar="suffix",
    type=str,
    help="the suffix to search for")
myParser.add_argument(
    "-td", 
    default="C",
    metavar="targetDir",
    type=str,
    required=False,
    help="which drive or directory to search through, defaults to C:\\")
args = myParser.parse_args()

sfx = args.sfx
rootDir = "C:\\"
if (os.path.isdir(args.td+":\\")):
    rootDir = args.td+":\\"
elif (os.path.isdir(args.td)):
    rootDir = args.td

def AllFilesInDir(dir):
    outputList =[]
    for root, _, files in os.walk(dir):
        for file in files:
            output=root+"\\"+file
            outputList.append(output)
    return outputList
def SearchBySuffix(sfx):
    paths = AllFilesInDir(rootDir)
    outputList = []
    for path in paths:
        if(path.endswith(sfx)):
            outputList.append(path)
    for output in outputList:
        print(output)

SearchBySuffix(sfx)