import random

def randomizingAnswers(listOfAnswers):
    i = 0
    changedList = []
    numberOfElements = len(listOfAnswers)
    randomNumberList = []

    while True:
        randomNumber = random.randint(0, numberOfElements - 1)
        if randomNumber in randomNumberList:
            continue
        else:
            randomNumberList.append(randomNumber)

        if len(randomNumberList) == numberOfElements:
            break
    print(str(randomNumberList) + " muj randomik")

    for i in range(numberOfElements):
        print(str(i) + " elemntik")

        checkingString = listOfAnswers[randomNumberList[i]]

        if checkingString[0] == "*":
            checkingString = checkingString[1:]

        if checkingString in changedList:
            print("zopakovano" + str(changedList))
            i = 0
        else:
            changedList.append(checkingString)
            print("pridan novej prvek do randomu" + (str(changedList)))
            i += 1

    #print(changedList)
    return changedList


file = open("questions.txt", "r")
file_editing = open("questions-editing.txt", "w")

fileLength = 0
lineLength = 0
maxLineLength = 0
doubleLineQuestion = False
sameQuestion = False
linesList = []

for line in file:
    file_editing.write(line)
file.close()
file_editing.close()

file_editing = open("questions-editing.txt", "r")
file_result = open("result.txt", "w")


# for line in file_editing:
#     fileLength += 1
#     if line[0].isupper():
#         lineLength = len(line)
#         if lineLength > maxLineLength:
#             maxLineLength = lineLength
#             print("Line: " + str(fileLength) + "Has characters: " + str(maxLineLength) + "\t\t" + line)
# print("file length: " + str(fileLength))



for line in file_editing:
    if line[0].isupper() and (line[-2] == "?" or line[-2] == ":" or line[-2] == "…"):

        file_result.write(line)

        linesList.clear()
        counter = 0
        questionFile = open("questions.txt", "r")

        while True:
            print("jsem na radku" + str(counter))
            questionLines = questionFile.readline()

            if (counter == fileLength + 1 or sameQuestion) and questionLines != "":
                print("podminka splnena, jsem na radku " + str(counter))
                print(questionLines)
                if questionLines[-2] != "?" and questionLines[-2] != ":" and questionLines[-2] != "…":
                    print("jdu appendovat")
                    linesList.append(questionLines)
                    print("muj list" + str(linesList))
                    counter += 1
                    sameQuestion = True
                    continue
                else:
                    print("jdu randomovat")
                    questionLinesChanged = randomizingAnswers(linesList)
                    print("zrandomovano " + str(questionLinesChanged))
                    for element in questionLinesChanged:
                        file_result.write(element)
                    sameQuestion = False
                    break
            if questionLines == "":
                break
            else:
                print("opakuju sa v elsu")
                counter += 1
                print(counter)
        questionFile.close()

    #tohle prepsat na elif
    elif line[0].isupper() and (line[-2] != "?" and line[-2] != ":" and line[-2] != "…"):
        doubleLine = True
    else:
        #print("Error: " + line + " on line:" + str(fileLength))
        kek = 5
    fileLength += 1


file_editing.close()
file_result.close()
