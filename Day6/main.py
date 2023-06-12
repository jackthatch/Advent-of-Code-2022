
with open('day_6_input.txt') as file:
    data = file.read()

myList = []
count = 0

def findKey(data: str, count: int, myList: list):

    for ele in data:

        if len(myList) == 14:        ## return count if we found the 
            print(myList)
            return count
        
        if ele not in myList:
            myList.append(ele)

        else:
            index = myList.index(ele) 
            myList = myList[index + 1:]

            myList.append(ele)      ## append the new instance of the letter

        count += 1

x = findKey(data, count, myList)

print(x)


