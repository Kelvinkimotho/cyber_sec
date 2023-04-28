alphabets="abcdefghijklmnopqrstuvwxyz"
message=input("Enter message...\n")
remaider=0;
#new_message=''
for  ch in message:
     lower_ch=ch.lower()
     if lower_ch in alphabets:
         char_index=alphabets.index(lower_ch)
         new_char_index=char_index+13
#         new_char=alphabets[new_char_index]
         remaider=new_char_index-25
         if new_char_index<=25:
              new_char=alphabets[new_char_index]
              #print(new_char)
              message= message.replace(ch,new_char)
         else:
             continuation=-1+remaider
             new_char=alphabets[continuation]
             #print(new_char)
             message=message.replace(ch,new_char)

print(message)
