import json
  
with open("info.txt") as f:
    data = f.read()
info = json.loads(data)

def start():
  print("╔════════════════════════════════════════╗")
  print("║  Would you like to sign-up or log-in?  ║ ")
  ques = input("║               (S or L)                 ║ ")
  print("╚════════════════════════════════════════╝")
  if ques.lower() == "s":
    signup()
  elif ques.lower() == "l":
    login()
  else:
    print("╔════════════════════════════════════════╗")
    print(f"║            Incorrect input             ║")
    print("╚════════════════════════════════════════╝")

def signup():
  print("╔════════════════════════════════════════╗")
  username = input("║            Create Username:            ║ ")
  print("╚════════════════════════════════════════╝")
  if username in info:
    print("╔════════════════════════════════════════╗")
    print("║             Username Taken             ║")
    print("╚════════════════════════════════════════╝")
  else:
    print("╔════════════════════════════════════════╗")
    password = input("║            Create Password:            ║ ")
    print("╚════════════════════════════════════════╝")
    f = open("info.txt", "r+")
    lines = f.readlines()
    f.seek(0)
    f.truncate()
    f.writelines(lines[:-1])
    f.write(f',"{username.lower()}" : "{password}"\n')
    f.write("}")
    print("╔════════════════════════════════════════╗")
    print("║         successfully signed up         ║")
    print("║    please restart program to log-in    ║")
    print("╚════════════════════════════════════════╝")
    
def login():
  print("╔════════════════════════════════════════╗")
  username = input("║               Username:                ║ ")
  password = input("║               Password:                ║ ")
  print("╚════════════════════════════════════════╝")
  i = 3
  for i in range(3,-1,-1):
    if username.lower() in info and info[username.lower()] == password:
      print("╔════════════════════════════════════════╗")
      print("║         Logged in successfully         ║")
      print("╚════════════════════════════════════════╝")
      break
    else:
      if i > 0:
        print("╔════════════════════════════════════════╗")
        print("║        Invalid login, try again        ║")
        print(f"║            {i} tries left                ║")
        print("╚════════════════════════════════════════╝")
        print("╔════════════════════════════════════════╗")
        username = input("║               Username:                ║ ")
        password = input("║               Password:                ║ ")
        print("╚════════════════════════════════════════╝")
      else:
        print("╔════════════════════════════════════════╗")
        print(f"║           Ran out of tries             ║")
        print(f"║      Restart program to try again      ║")
        print("╚════════════════════════════════════════╝")
      
      
#██   ██ ██ 
#██   ██ ██
#███████ ██
#██   ██ ██
#██   ██ ██
      
#╔═══════╗
#║       ║
#╚═══════╝

start()