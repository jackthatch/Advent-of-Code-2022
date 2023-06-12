with open ('day5_input.txt') as txt:
    data = txt.readlines()[10:]

l1 = ['B', 'W', 'N']
l2 = ['L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B']
l3 = ['Q', 'H', 'Z', 'W', 'R']
l4 = ['W', 'D', 'V', 'J', 'Z', 'R']
l5 = ['S', 'H', 'M', 'B']
l6 = ['L', 'G', 'N', 'J', 'H', 'V', 'P', 'B']
l7 = ['J', 'Q', 'Z', 'F', 'H', 'D', 'L', 'S']
l8 = ['W', 'S', 'F', 'J', 'G', 'Q', 'B']
l9 = ['Z', 'W', 'M', 'S', 'C', 'D', 'J']

list_mapping = {
    1: l1,
    2: l2,
    3: l3,
    4: l4,
    5: l5,
    6: l6,
    7: l7,
    8: l8,
    9: l9
}

for ele in data:

    new_list = []
    num = int(ele[5:7].strip())
    to = int(ele[17:19].strip())
    fro = int(ele[12:14].strip())

    for i in range(num):
        curr = list_mapping[fro].pop()
        new_list.append(curr)

    for ele in reversed(new_list):
        list_mapping[to].append(ele)
        # print(ele, ' appended to ', list_mapping[to])


res = l1.pop() + l2.pop() + l3.pop() + l4.pop() + l5.pop() + l6.pop() + l7.pop() + l8.pop() + l9.pop() 
print(res)

