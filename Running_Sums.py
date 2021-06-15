nums = [1,2,3,4]
nums2 = [3,1,2,10,1]

def runningSum(listOfNums):
    runSum = [None] * len(listOfNums)
    runSum[0] = listOfNums[0]
    i = 1
    while len(listOfNums) > i:
        runSum[i] = listOfNums[i] + runSum[i-1]
        i += 1
    
    return runSum

print(runningSum(nums))
print(runningSum(nums2))