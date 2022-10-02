# #Author: Jon Merchant
# #Title: Telephone Decipher
# #Further Comments:
# # The purpose of this script is to take a telephone number (in form ABC-ABC-ABCD)
# # and return the actual number (i.e., in form xxx-xxx-xxxx). At this time I *have not* optimized this script.

#Create a dictionary for the 'translation'
cipherDict = {
            'A': 2, 'B': 2, 'C': 2,
            'D': 3, 'E': 3, 'F': 3,
            'G': 4, 'H': 4, 'I': 4,
            'J': 5, 'K': 5, 'L': 5,
            'M': 6, 'N': 6, 'O': 6,
            'P': 7, 'Q': 7, 'R': 7, 'S': 7,
            'T': 8, 'U': 8, 'V': 8,
            'W': 9, 'X': 9, 'Y': 9, 'Z': 9
            }

#Prompt user for input and parse
inNumbers = input("Enter a phone number to be translated: ")
splitNumbers = inNumbers.split("-")
castNumbers = []

#Check which components of splitNumbers are ints, and which are strings; typecast those that aren't strings
for i in range(0, len(splitNumbers)):
    try:
        castNumbers.append(int(splitNumbers[i]))
    except ValueError:
        castNumbers.append(splitNumbers[i])

#For those that are still strings, translate
finalNumber = 0
addToFinal = 0

for j in range(0, len(castNumbers)):
    if(isinstance(castNumbers[j], str)):
        for k in castNumbers[j]:
            addToFinal = cipherDict.get(k)
            finalNumber = (finalNumber * 10) + addToFinal
        
        castNumbers[j] = finalNumber

    finalNumber = 0
    addToFinal = 0

#Print
toPrint = ''

for l in range(0, len(castNumbers)):
    if(l != len(castNumbers)-1):
        toPrint += str(castNumbers[l])
        toPrint += '-'
    else:
        toPrint += str(castNumbers[l])

print(toPrint)