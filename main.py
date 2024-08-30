#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# turn all the invited names into a list
PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()  #tp read txt file
    # print(names)

with open("./input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        #to remove extra spaces
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)

#to export all letters into output folder as txt files. file name as 'letter for'person's name'
        with open(f"./output/ReadyToSend/letter_for_{stripped_name}.txt", mode = "w") as completed_letter:
            completed_letter.write(new_letter)
