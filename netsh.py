import os

print("finding wifi networks and their passwords!")
os.system("netsh wlan show profile")

name=input("Enter the name of the wifi ..")

os.system(f"netsh wlan show profile {name} key=clear")