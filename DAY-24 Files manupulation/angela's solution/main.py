#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER="[name]"
with open("./angela's solution/Input/Names/invited_names.txt",'r') as names_file:
    names=names_file.readlines()


with open("./angela's solution/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents=letter_file.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_contents.replace(PLACEHOLDER,stripped_name)
        with open(f"./angela's solution/Output/ReadyToSend/Letter_for_{stripped_name}.docx","w") as output_file:
            output_file.write(new_letter)