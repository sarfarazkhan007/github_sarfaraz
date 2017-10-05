import os
import tkinter

# clear the screen
os.system("clear") 

#tkMessageBox.showinfo( "NTAL EXP 1", "Enter your choice from the menu: \n1) dig \n2) whois \n3) ping \n")
inp = input("Enter your choice from the menu: \n1) dig \n2) whois \n3) ping \n")

#if (inp == "3"):
	#target = raw_input("Enter the url or ip address:\n")


target = "stackoverflow.com"
response = os.system("ping %s -c 3" % target)

if response is not 0:
    print("failed")
else:
    print("success")