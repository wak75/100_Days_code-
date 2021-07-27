#TODO: Create a letter using starting_letter.txt 

with open("mail-merge-project-start/Input/Names/invited_names.txt", mode="r") as names:
    x=names.read()
    txt=x.split("\n")
        
for i in txt:
    with open("mail-merge-project-start/Input/Letters/starting_letter.txt","r") as file1, open(f"mail-merge-project-start/Output\ReadyToSend/Letter_for_{i}.docx","w") as file2:
        for line in file1: 
            file2.write(line.replace("[name]",i))
        


        


#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp