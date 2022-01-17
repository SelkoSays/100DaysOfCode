with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
print(names)
n = []
for i in names:
    n.append(i.replace("\n",""))
names = n
print(names)

with open("./Input/Letters/starting_letter.txt") as f:
    contents = f.read()
    print(contents)

for i in names:
    with open(f"./Output/ReadyToSend/letter_for_{i}.txt","w+") as new_file:
        new_file.write(contents.replace("[name]",i))