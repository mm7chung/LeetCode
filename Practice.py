from collections import defaultdict

paths = [
    "root/a 1.txt(abcd) 2.txt(efgh)",
    "root/c 3.txt(abcd)",
    "root/c/d 4.txt(efgh)",
    "root 4.txt(efgh)",
    "root/2342 aaa.txt(fsefsefes)",
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

def filePathAndContent(vector):
    for vector < 50:
        


class Solution(object):
    def findDuplicate(self, paths):
        fileContentTuples = []
        for path in paths:
            fileContentTuples.extend(parseFileAndContentsFromString(path))


        multimap = defaultdict(list)

        for fileName, content in fileContentTuples:
            multimap[content].append(fileName[:fileName.find("(")])


        listofLists = []

        for content, listOfPaths in multimap.items():
            if len(listOfPaths) == 1:
                continue
            listofLists.append(listOfPaths)
    
        return listofLists





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


if __name__ == "__main__":
    print(Solution().findDuplicate(paths))