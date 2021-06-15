class SubrectangleQueries(object):
    def __init__(self, rectangle):
        self.rectangle = rectangle


    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.rectangle[row][col] = newValue
        
        
    def getValue(self, row, col):
        rowValue = self.rectangle[row]
        colValue = rowValue[col]
        #return self.rectangle[row][col]

        return colValue
        

# ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
# [[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
sub = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
returnList = [None]

returnList.append(sub.getValue(0, 2))
returnList.append(sub.updateSubrectangle(0, 0, 3, 2, 5))
returnList.append(sub.getValue(0, 2))
returnList.append(sub.getValue(3, 1))
returnList.append(sub.updateSubrectangle(3, 0, 3, 2, 10))
returnList.append(sub.getValue(3, 1))
returnList.append(sub.getValue(0, 2))

print(returnList)

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)


# class Example:
#   classVariable = 0

#   def __init__(self, arg1, arg2):
#     self.arg1 = arg1
#     self.arg2 = arg2
#     Example.classVariable += 1

#   def printVariables(self):
#     print("Class variable: " + str(Example.classVariable))
#     print("arg1: " + str(self.arg1))
#     print("arg2: " + str(self.arg2))


# myFirstExampleObject = Example(12, "Hello")
# myFirstExampleObject.printVariables()

# anotherExampleObject = Example("test", 323)
# anotherExampleObject.printVariables()

# aThirdExample = Example("abc", "fsdfsd")
# aThirdExample.printVariables()

# myFirstExampleObject.printVariables()
# anotherExampleObject.printVariables()
# aThirdExample.printVariables()
