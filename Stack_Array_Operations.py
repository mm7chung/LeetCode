array = []



    def buildArray(self, target, n):
        list = range(1,target[-1])
        commandList = []
        i = 0
        
        # myList = [2, 34, 56]
        # for element in myList:
        #     print(element)
        
        for element in list:
            if list[i] == target[i]:
                commandList.append("Push")
                i += 1
            else:
                commandList.append("Push")
                commandList.append("Pop")
                i += 1
                
        return commandList