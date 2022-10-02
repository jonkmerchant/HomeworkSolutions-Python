# #Author: Jon Merchant
# #Title: Sentence Parsing & Capitalization.
# #Further Comments:
# # The purpose of this script is simply to parse a string input into sentences (' ' delimited)
# # and to capitalize the first word of each.

#Take input
inputString = input("Enter sentence to be capitalized:")

#Parse based on delimiter
inputStringArr = inputString.split(' ')

#Loop through array and find where sentences end; change next word's first letter to uppercase
for i in range (0, len(inputStringArr)):

    #Case: First word in entire string input
    if(i == 0):
        temp = list(inputStringArr[i])
        temp[0] = temp[0].upper()
        inputStringArr[i] = "".join(temp)

    #Case: All words afterward which follow a '.'
    if(i != len(inputStringArr)-1):
        if '.' in inputStringArr[i]:
            temp = list(inputStringArr[i+1])
            temp[0] = temp[0].upper()
            inputStringArr[i+1] = "".join(temp)

#Print
toPrint = ""

for k in range(0, len(inputStringArr)):
    if(k != len(inputStringArr) - 1):
        toPrint += inputStringArr[k]
        toPrint += " "
    else:
        toPrint += inputStringArr[k]

print(toPrint)
