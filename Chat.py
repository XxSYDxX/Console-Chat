# Rock On !!!

from threading import Thread
from time import sleep
import sys, subprocess

print(" === STARTING REQUIRED MODULES === ")
subprocess.call([sys.executable, "-m", "pip", "install", "discord.py"])
subprocess.call([sys.executable, "-m", "pip", "install", "readchar"])
print(" === INITIATION COMPLETE === \n\n\n")

import readchar
from discord.ext import commands 
from discord import Client

bot = Client()
to = "NDkyMjUwNDY5NjEyMjU3Mjgw.XcjfpQ."
k = "s"
en = "2ZF3mQrLzn885L7Dv3LU2EQstg"


def clr():
    print(chr(27) + "[2J")


class bcolors:                                  
    HEADER = '\033[95m'                         
    OKBLUE = '\033[94m'                         
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'                
    FAIL = '\033[91m'
    ENDC = '\033[0m'                            
    BOLD = '\033[1m'                        
    UNDERLINE = '\033[4m'


if len(sys.argv) >= 2:
    secret = sys.argv[1]

else:
    secret = "0"

user = secret[:10]


text = ""
newtext = ""
quit = False
typing = False


@bot.event
async def on_ready():
    global text
    global quit
    print("\r\r\rConnecting to Server...")
    while not quit:
        while not typing:
            global newtext
            msg = await bot.get_channel(642959441917902902).fetch_message(642988009112862740)
            text = msg.content
            print(text + bcolors.BOLD + bcolors.WARNING + "\n\r\r\rHit ENTER to reply" + bcolors.ENDC)
            if len(newtext) == 0:
                await msg.edit(content=text)
            else:
                await msg.edit(content=newtext)


def pussy():
    global typing
    global quit
    global text
    global newtext
    while True:
        if repr(readchar.readkey()) == "'\\r'":
            typing = True
            clr()
            msg = input(bcolors.OKGREEN + "Type your text and hit ENTER" + bcolors.WARNING + " (sometimes this green message may not appear, but if you hit enter once, keep typing and hit enter again to send your message): \n\n" + bcolors.ENDC).strip()
            temptext = text + "\n" + "\r"*5 + bcolors.BOLD + bcolors.OKBLUE + user + ": " + bcolors.ENDC + msg
            if len(msg) != 0:
                if len(temptext) < 1950:
                    newtext = '.' + ' '*(1950-len(temptext)-10) + temptext
                else:
                    newtext = '.' + temptext[len(temptext)-1940:len(temptext)]
            typing = False
        elif repr(readchar.readkey()) == "'q'":
            typing = True
            quit = True
            break


def start():    
    Thread(target=pussy).start()
    print('Type thread up and running...\r\r\r\r\r\r\r\nInitiating server connection...')
    bot.run(to + k + en)
    

if secret == '0':
    print("You need to put a username to log in with. e.g. \n\n" + bcolors.BOLD + bcolors.WARNING + "python3 Chat.py MyUsername" + bcolors.ENDC + "\n\nUsername must have no space and within 10 characters.")

else:
    start()
