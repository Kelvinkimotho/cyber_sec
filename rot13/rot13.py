import os
#Taking  user message to 
message=input("Enter message....\n")

alphabets="abcdefghijklmnopqrstuvwxyz"
#converting user input to lowercase
message_in_lower=message.lower()
final_message=""
#looping through user name getting  each character
for ch in message_in_lower:
      #if message character is in alphabets. print("yes"), else no
      if ch in alphabets:
          #print("Yes")
          index=alphabets.index(ch)
         # print(index)
         #Indexof the replacing character
          replacing_index=index+13 
         #After adding i3 to the index  of the  character in  the alphabets, it might exceed 25 which is the index of the last character in the  alphabet list, 
         #We have to minus it from the sum  of the  of index+13 to get the remaider
          remaider=replacing_index-25
          if replacing_index<=25:
             rep_ch=alphabets[replacing_index]
            
            # print(rep_ch.strip(" "))
             final_message+=rep_ch
          else:
             rep_ch_index=-1+remaider
             rep_ch=alphabets[rep_ch_index]
             final_message+=rep_ch
             #print(rep_ch.strip(" "))
      else:pass
          # print("No")
print(f"Here is the final message after converting {message.upper()} using rot13::: {final_message.upper()}")
#lets save  the outcome in a text file , 
#creating a text file
with open("outcomes.txt",'a') as  myfile:
     #writing  to  the file
      myfile.write(f"Here is the final message after converting {message.upper()} using rot13::: {final_message.upper()}\n")
      myfile.close()
