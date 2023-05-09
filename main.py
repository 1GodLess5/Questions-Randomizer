import random

def randomizingAnswers(listOfAnswers, usualNumberOfAnswers):
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

    for i in range(numberOfElements):
        checkingString = listOfAnswers[randomNumberList[i]]

        if checkingString[0] == "*":
            checkingString = checkingString[1:]

        if checkingString in changedList:
            continue
        else:
            changedList.append(checkingString)

    if numberOfElements > usualNumberOfAnswers:
        unusualNumberOfAnswers = True
        return changedList, unusualNumberOfAnswers
    else:
        unusualNumberOfAnswers = False
        return changedList, unusualNumberOfAnswers


file = open("questions.txt", "r")
file_editing = open("questions-editing.txt", "w")

fileLength = 0
lineLength = 0
maxLineLength = 0
doubleLineQuestion = False
sameQuestion = False
linesList = []
numberOfQuestions = 0
doneLines = []

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
    # correctly formated (one line) question
    if line[0].isupper() and (line[-2] == "?" or line[-2] == ":" or line[-2] == "…"):
        file_result.write(str(numberOfQuestions + 1) + ". " + line)
        numberOfQuestions += 1
        linesList.clear()
        counter = 0
        moreLineAnswer = False
        questionFile = open("questions.txt", "r")

        while True:
            questionLines = questionFile.readline()

            # checking if im on right line in file
            if (counter == fileLength + 1 or sameQuestion) and questionLines != "":
                # checking if im not on new question
                if questionLines[-2] != "?" and questionLines[-2] != ":" and questionLines[-2] != "…":
                    linesList.append(questionLines)
                    counter += 1
                    sameQuestion = True
                    continue
                # if i get to new question im randomizing the answers and writing them to the result file
                elif questionLines[-2] != "?" or questionLines[-2] != ":" or questionLines[-2] != "…" or "":
                    questionLinesChanged, moreLineAnswer = randomizingAnswers(linesList, 4)

                    if moreLineAnswer:
                        print("Inspect question number: " + str(fileLength + 1))

                    for element in questionLinesChanged:
                        file_result.write("\t" + element)

                    file_result.write("\n")
                    sameQuestion = False
                    break
                else:
                    print("Check this shit on line: " + str(counter + 1))

            counter += 1
        questionFile.close()

    # upravit podminku a vytvorit doneLines[] pro liny ktere uz jsou opracovane a neni treba se s nema prcat znova
    elif line[0].isupper() and (line[-2] != "?" and line[-2] != ":" and line[-2] != "…"):
        counter = 0
        doubleLine = True

        questionFile = open("questions.txt", "r")

        while True:
            # first line, third line
            if counter % 2 == 0:
                firstLine = questionFile.readline()
            # second, fourth line
            else:
                secondLine = questionFile.readline()

            if counter + 1 == fileLength:
                if secondLine[-2] == "?" or secondLine[-2] == ":" or secondLine[-2] == "…":
                    makingOneLine = firstLine[0:-2] + " " + secondLine
                    print(makingOneLine)
                else:
                    print("Check if the line is question: " + str(fileLength + 1))

            if firstLine == "":
                break


            counter += 1
    else:
        #print("Error: " + line + " on line:" + str(fileLength))
        kek =5
    fileLength += 1


file_editing.close()
file_result.close()
