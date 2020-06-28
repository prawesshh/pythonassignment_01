# Write a Python program to insert a given string at the beginning of all items in
# a list.
# Sample list: [1, 2, 3, 4], string: emp
# Expected output: ['emp1', 'emp2', 'emp3', 'emp4']


def insertInBegin(myList, myString):
    result = []
    for i in myList:
        result.append(myString+str(i))
    return result


myList = [1, 2, 3, 4]
myString = 'emp'
print(insertInBegin(myList, myString))
