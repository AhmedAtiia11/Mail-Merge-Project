#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Letters/starting_letter.txt") as file:
    starting_letter=file.readlines()
with open("./Input/Names/invited_names.txt")as file:
    invited_names=file.readlines()

     

for name in invited_names:
    name=name.strip()
    with open(f"./Output/invite_for_{name}.txt",mode="w")as output:
        for line in starting_letter:
            if line.startswith("Dear"):
                output.write(line.replace("[name]",name))
                continue
            output.write(line)

