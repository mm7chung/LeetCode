from collections import defaultdict

paths = [
    "root/a 1.txt(abcd) 2.txt(efgh)",
    "root/c 3.txt(abcd)",
    "root/c/d 4.txt(efgh)",
    "root 4.txt(efgh)"
]

def findContent(fileAndContentString):
    return fileAndContentString[fileAndContentString.find("(") + 1:fileAndContentString.find(")")]


def findFilesAndContentStrings(directoryString):
    tokens = directoryString.split(" ")
    results = []
    for token in tokens[1:]:
        fileAndContentString = tokens[0] + "/" + token
        results.append(fileAndContentString)
    return results


def parseFileAndContentsFromString(string):
    tuples = []
    for fileAndContent in findFilesAndContentStrings(string):
        tuples.append((fileAndContent, findContent(fileAndContent)))
    return tuples


fileContentTuples = []
for path in paths:
    fileContentTuples.extend(parseFileAndContentsFromString(path))

print(fileContentTuples)
multimap = defaultdict(list)

for fileName, content in fileContentTuples:
    multimap[content].append(fileName)

print(multimap)


# pathsDictionary = {
#     "root/a/1.txt(abcd)" : "abcd",
#     "root/a/2.txt(efgh)" : "efgh",
#     "root/c/3.txt(abcd)" : "abcd",
#     "root/c/d/4.txt(efgh)" : "efgh",
#     "root/4.txt(efgh)" : "efgh"
# }


# myString = "this is a string"
# print(myString)
# print(myString[1:])
# print(myString[:-3])
# print(myString[1:4])
# print(myString.split(" "))
# print(myString.find("s"))
# print(myString.strip())
# print(myString + " and another string")
# print(myString * 4)


def deduplicateFiles(mapPathToContent):
    multimap = defaultdict(list)

    for fileName, content in pathsDictionary.items():
        multimap[content].append(fileName)

    return multimap

def findDuplicate(paths):
    for path in paths:
        break
        # print(path)
    return


if __name__ == "__main__":
    findDuplicate(paths)