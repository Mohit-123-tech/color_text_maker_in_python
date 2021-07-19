import os

for i in range(1,999999999):
    txt = input('text --> ')
    if txt == "exit":
        exit()
    else:
        os.system('clear')
        os.system(f'figlet -f mono9 {txt} | lolcat')