
with open('day4_input.txt') as txt:
    data = txt.readlines()

count = 0

for ele in data :

    list1 = 0
    list2 = 0

    string1 = ele
    lower1 = int(string1.split('-')[0])  # Convert the first number before '-' to an integer
    upper1 = int(string1.split('-')[1].split(',')[0])  # Convert the first number after '-' to an integer
    lower2 = int(string1.split(',')[1].split('-')[0])  # Convert the first number after ',' to an integer
    upper2 = int(string1.split(',')[1].split('-')[1])  # Convert the first number after ',' to an integer

    # if (lower1 <= lower2 and upper1 >= upper2):
    #     count += 1
    # elif (lower2 <= lower1 and upper2 >= upper1):
    #     count += 1
    
    list1 = list(range(lower1, upper1 + 1))     #Make a list of the range
    list2 = list(range(lower2, upper2 + 1))

    for ele in list1:       #If there is a shared element of the list increment count and break the loop
        if ele in list2:
            count += 1
            break


print(count)