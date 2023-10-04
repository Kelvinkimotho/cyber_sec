#a list of digits i will be using when generating passwords for my wordlists
digits=[0,1,2,3,4,5,6,7,8,9]
def four_ch_passwords(digits):
     for a in digits:
         for b in digits:
             for c in digits:
                 for d in digits:
                     with open("four_numbers_pwrd_wordlist.txt",'a') as myfile:
                              myfile.write(f"{a}{b}{c}{d}\n")
                              myfile.close())  
def five_ch_passwords(digits):
     for a in digits:
         for b in digits:
             for c in digits:
                 for d in digits:
                     for e in digits:
                         with open("five_numbers_pwrd_wordlist.txt",'a') as myfile:
                              myfile.write(f"{a}{b}{c}{d}{e}\n")
                              myfile.close())  
def six_ch_passwords(digits):
     for a in digits:
         for b in digits:
             for c in digits:
                 for d in digits:
                     for e in digits:
                         for f in digits:
                              with open("six_numbers_pwrd_wordlist.txt",'a') as myfile:
                              myfile.write(f"{a}{b}{c}{d}{e}{f}\n")
                              myfile.close())  
#calling the functions                             
four_ch_passwords(digits)
five_ch_passwords(digits)
six_ch_passwords(digits)
