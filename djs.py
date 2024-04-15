import os,platform
os.system('git pull')
os.system("clear")
print('\033[92;1m Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/GrMaqHEYlbOJJZzc1h2VVU')
djs=platform.architecture()[0]
if djs=="32bit":
    __import__("p32")
elif djs=="64bit":
    __import__("p64")
