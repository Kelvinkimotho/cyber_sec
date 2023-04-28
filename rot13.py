import os

alphabets="abcdefghijklmnopqrstuvwxyz"
message=input("What is you message??\n")
remaider=0;
#print(f"Here is what you entered: {message}")
encrypted=''
for ch in message:
    lower_ch=ch.lower()
    if lower_ch in alphabets:
           index=alphabets.index(lower_ch)
           _13stal=index+13
           remaider=_13stal-25
           if _13stal<=25:
              #print(alphabets[_13stal])
              #encrypted.append(alphabets[_13stal])
              encrypted=encrypted+f"{alphabets[_13stal]}"
           else :
                continuation=-1+remaider
                #print(alphabets[continuation])
                #encrypted.append(alphabets[continuation])
                encrypted=encrypted+f"{alphabets[continuation]}"          

print(encrypted)
