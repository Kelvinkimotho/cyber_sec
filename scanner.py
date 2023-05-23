#This python script takes a list of password hashes ,
#Using the rockyou.txt file. we crack the hashes 
#Using Hashcat tool for password hacking . 
# This program works
import os
#path to the text file containing the hashes
hashes_txt_file='/home/user/Desktop/hash.txt'
#path to  the rockyou.txt wordlist
wordlist="/usr/share/wordlists/rockyou.txt"
#After cracking a hash we will save the outcome in "cracked.txt" file
outcome="cracked.txt"
#after extracting  the  hashes from the text file we save them in a hashes list
hashes_list=[]
#opening the text file containing  the hashes to be cracked
with open(hashes_txt_file,'r') as myfile:
      lines=myfile.readlines()
      #looping through the lines
      for line in lines:
         #After looping through the lines , we will the hashes in  the hashes list , but we have to strip the 'new line ' ie "\n" at the end of every hash
         hash_to_save=line.strip("\n")
         #appending  the hash_to_save in the hashes list
         hashes_list.append(hash_to_save)
#After saving  the hashes  , lets loop through the list  and use hashcat together with the rockyou.txt file   to crack  the hashes
for target_hash in hashes_list:
     for i in range(len(hashes_list)):
           os.system(f"hashcat -m 0 -a 0 -o {outcome} {target_hash} {wordlist}")
           print("mission is over!!")
