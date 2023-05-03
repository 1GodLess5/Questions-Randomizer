file = open("questions.txt", "r")
file_editing = open("questions-editing.txt", "w")

fileLength = 0
lineLength = 0
maxLineLength = 0
doubleLineQuestion = False

for line in file:
    file_editing.write(line)
file.close()
file_editing.close()

file_editing = open("questions-editing.txt", "r")

# for line in file_editing:
#     fileLength += 1
#     if line[0].isupper():
#         lineLength = len(line)
#         if lineLength > maxLineLength:
#             maxLineLength = lineLength
#             print("Line: " + str(fileLength) + "Has characters: " + str(maxLineLength) + "\t\t" + line)
# print("file length: " + str(fileLength))

for line in file_editing:
    if line[0] # podminka pokud lajna = Velke pismeno + konec = otaznik, ... tak vymyslet co s tym

    #tohle prepsat na elif
    if line[0].isupper() and (line[-2] != "?" and line[-2] != ":" and line[-2] != "…"):
        doubleLine = True


file_editing.close()
