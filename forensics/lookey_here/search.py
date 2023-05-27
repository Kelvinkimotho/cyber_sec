import os
search_item=input("Enter item you wanna search....\n")
#Bellow is the path to the host folder
path='/home/user/Desktop/.forensics'
#list comprehension
files=[file for file in os.listdir(path)]
#looping through each file in the host folder
for file in files:
    #looking for a text file among the files in that folder
    if ".txt" in file:
             #opening the found text file with read mode
              with open(file,'r') as  myfile:
                      #storing the lines as a list of lines
                      lines=myfile.readlines()
                     # print(len(lines))
                     #looping through all the lines
                      for  line in lines:
                            #print(line)
                            if f"{search_item}" in line:
                                  segments=line.split(" ")
                                  for segment in segments:
                                        if "pico" in segment:
                                              print(segment)
print("Mission complete!!!!!")
