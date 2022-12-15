
with open("input.txt") as file:
    nums = [i for i in file.read().strip().split("\n")]

chunkSum = 0 
maxCals = 0
sumList = []

for ele in nums:
    if ele == "":
        sumList.append(chunkSum)
        chunkSum = 0
    else:
        num = int(ele)
        chunkSum += num
    
    if chunkSum > maxCals:
        maxCals = chunkSum

sumList.sort()

print("Top Sum:", maxCals)
print("Sum of Top 3: ", sumList[-1] + sumList[-2] +sumList[-3])


