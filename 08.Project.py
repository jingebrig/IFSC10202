filename = "constitution.txt"
file = open(filename, "r")

text = file.readlines()
file.close()

for i in range(len(text)):
    text[i] = text[i].rstrip("\n")

while True:
    search = input("Enter search term: ")
    if search == "":
        break

    line_number = 0

    while line_number < len(text):
        line = text[line_number]

        if search.lower() in line.lower():
            start = line_number
            while start > 0 and text[start - 1].strip() != "":
                start -= 1

            end = line_number
            while end < len(text) and text[end].strip() != "":
                end += 1

            for i in range(start, end):
                print(f"Line {i + 1}: {text[i]}")
            print()

            line_number = end
        else:
            line_number += 1