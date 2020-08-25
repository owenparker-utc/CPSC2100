## Charles Parker - CPSC2100 - Week 1 Programming Assignment
## Display presidents with a specified first name.

presNameEndsWith = input("Enter a name ending: ")
foundMatch = False
inPresList = open("USPres.txt", 'r')
for line in inPresList:
    if line.rstrip().endswith(presNameEndsWith):
        print(line.rstrip())
        foundMatch = True
if not foundMatch:
    print("No president had a name ending with", presNameEndsWith + '.')
inPresList.close()