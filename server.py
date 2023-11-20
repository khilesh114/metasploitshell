import time
import os
def simple():
    print("simple web server")
    user = input("enter ip :-")
    port = input("enter port :-")
    os.system(f"php -S {user}:{port}")
def user():
    print("simple web server")
    ip = input("enter ip :-")
    port1 = input("enter port no :-")
    path = input("enter a path start server :-")
    os.chdir(f"{path}")
    os.system(f"php -S {ip}:{port1}")
    
def main():
    print("start simple web server")
    print("\n\t defalt webserver        [1]")
    print("\n\t user defaind web server [2]")
    userm = input("enter your choics")
    if userm == "1":
       simple()
    elif userm == "2":
       user()
       
main()    