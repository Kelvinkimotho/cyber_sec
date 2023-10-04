import os
#path to the working folder
path='C:/Users/kelvin/Desktop/CS50CYBER'
#finding all files in the working folder and append the to a "files" list
files=[file for file in os.listdir(path)]
#looping through the files list finding the "txt" files which are the wordlist we are about to merge to one large wordlist
for file in files:
     if ".txt" in file:
          #opening the files found
          with open(file,'r') as target_file:
             #reading line by line of all the wordlists
             passwords=target_file.readlines()#the read passwords are stored in a list 
             #looping through the passwords list and get  individual passwords
             for password in passwords:
                 password=password.strip("\n")# The strip function removes the new line after every passwrod
                 #saving the passwords in one large wordlists named "456digitpasses.txt"
                 with open("456digitpasses.txt",'a') as final_list: #using the 'a' append mode 
                     final_list.write(f"{password}\n")
                     final_list.close() #closing the file after the append operation
                 
             