from tracker import track_phone
import time
import os
import sys

Wh = '\033[1;37m'
Gr = '\033[1;32m'
Re = '\033[1;31m'

def clear():
    """Limpia la pantalla del terminal"""
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def show_banner():
    """Muestra el banner de la herramienta"""
    clear()
    time.sleep(1)
    print(f"""{Wh}
        ____  __                    __                     __            
       / __ \\/ /_  ____  ____  ___  / /   ____  _________ _/ /_____  _____
      / /_/ / __ \\/ __ \\/ __ \\/ _ \\/ /   / __ \\/ ___/ __ `/ __/ __ \\/ ___/
     / ____/ / / / /_/ / / / /  __/ /___/ /_/ / /__/ /_/ / /_/ /_/ / /    
    /_/   /_/ /_/\\____/_/ /_/\\___/_____/\\____/\\___/\\__,_/\\__/\\____/_/     

          {Wh}[ + ]  {Gr}MODIFIED BY JMEIRACORBAL{Wh}  [ + ]
          {Wh}[ + ]  {Gr}ORIGINAL BY HUNXBYTS{Wh}      [ + ]
    """)
    time.sleep(0.5)

def main():
    show_banner()
    
    try:
        track_phone()
        input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr} Press enter to exit')
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        sys.exit(0)
    except Exception as e:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Error: {e}')
        time.sleep(2)
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        sys.exit(0)
