from util.plugins.update import search_for_updates
from util.plugins.commun import *

def main():
    clear()
    setTitle(f"Aria Tool v{THIS_VERSION}")
    astraahometitle()
    print(f"""        
\n                                      |                           Discord                                  
\n               {y}[{b}+{y}]{w} Grabber Options:   |       {y}[{b}+{y}]{w} Token Options:            {y}[{b}+{y}]{w} Discord Options:
\n               {y}[{w}1{y}]{w} File               |       {y}[{w}4{y}]{w} Account Nuker             {y}[{w}10{y}]{w} Tokens Checker
\n               {y}[{w}2{y}]{w} Image              |       {y}[{w}5{y}]{w} Account Disabler          {y}[{w}11{y}]{w} Clear DM
\n               {y}[{w}3{y}]{w} QrCode             |       {y}[{w}6{y}]{w} Account Generator         {y}[{w}12{y}]{w} House Changer
\n                                      |       {y}[{w}7{y}]{w} Settings Cycler           {y}[{w}13{y}]{w} Server Lookup
\n                                      |       {y}[{w}8{y}]{w} Token Informations        {y}[{w}14{y}]{w} Mass DM
\n                                      |       {y}[{w}9{y}]{w} AutoLogin                 {y}[{w}15{y}]{w} Group Spammer          
\t\t\t\t\t\t\t\t\t\t\t\t\t{y}[{b}>{y}]{w} Next Page""")
    global choice
    choice = input(f"""{y}[{b}+{y}]{w} system32$ """).lstrip("0")
    
    
    if choice == '1':
        transition()
        exec(open('util/6_FileGrab/filegrabber.py').read())
        main()
    elif choice == '2':
        transition()
        imagegrabbertitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool is under development, so it is not yet usable.")
        main()
    elif choice == '3':
        transition()
        fakeqrtitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool don't work anymore.")
        main()
    elif choice == '4':
        transition()
        exec(open('util/9_AccountNuker/accountnuker.py').read())
        main()
    elif choice == '5':
        transition()
        accountdisablertitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool don't work anymore.")
    elif choice == '6':
        transition()
        accountgentitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool is under development, so it is not yet usable.")
    elif choice == '7':
        transition()
        exec(open('util/12_SettingsCycler/settingscycler.py').read())
        main()
    elif choice == '8':
        transition()
        exec(open('util/13_TokenInfo/tokeninfo.py').read())
        main()
    elif choice == '9':
        transition()
        exec(open('util/14_AutoLogin/autologin.py').read())
    elif choice == '10':
        transition()
        exec(open('util/15_TokensChecker/tokenschecker.py').read()) 
        main()
    elif choice == '11':
        transition()
        cleardmtitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool don't work anymore.")
        main()
    elif choice == '12':
        transition()      
        exec(open('util/17_HouseChanger/housechanger.py').read())
    elif choice == '13':
        transition()
        exec(open('util/18_ServerLookup/serverlookup.py').read())
    elif choice == '14':
        transition()
        exec(open('util/19_MassDM/massdm.py').read())
    elif choice == '15':
        transition()
        groupspamtitle()
        input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} This tool don't work anymore.")
        main()
    elif choice == '>':
        clear()
        astraahometitle()
        print(f"""    
\n      {y}[{b}+{y}]{w} Nitro Options:          {y}[{b}+{y}]{w} WebHooks Options:        {y}[{b}+{y}]{w} Other Options:
\n      {y}[{w}16{y}]{w} Generator              {y}[{w}17{y}]{w} Spammer                 {y}[{w}19{y}]{w} Credits
\n                                  {y}[{w}19{y}]{w} Remover                 {y}[{w}20{y}]{w} Exit\n\n\n\n\n\n\n\n\n\n                                                                                                     {y}[{b}<{y}]{w} Previous Page""")
        choice = input(f"""{y}[{b}+{y}]{w} system32$: """)

        if choice == '16':
            transition()
            exec(open('util/21_NitroGen/nitrogen.py').read())
        elif choice == '17':
            transition()
            exec(open('util/22_WebHSpam/webhspam.py').read())
        elif choice == '18':
            transition()
            exec(open('util/23_WebHRemover/webhremover.py').read())
        elif choice == '19':
            transition()
            astraahometitle()
            print(f"""                                            {y}[{b}+{y}]{w} Development Networks:\n\n                                                {y}[{w}#{y}]{w} GitHub:    @Tap1337\n                                                {y}[{w}#{y}]{w} Server:    discord.gg/ariacc\n\n\n""")
            input(f"""{y}[{b}#{y}]{w} Press ENTER to exit""")
            main()
        elif choice == '20':
            transition()
            sys.exit()
        elif choice == '<':
            clear()
            main()    
        else:
            clear()
            main()
    else:
        clear()
        main()


if __name__ == "__main__":
    import sys
    setTitle("Aria Tool Loading...")
    System.Size(120, 30)
    Anime.Fade(Center.Center(banner), Colors.purple_to_blue, Colorate.Vertical, time=1)
    if not os.path.exists("output"):
        os.makedirs("output", exist_ok=True)
    if os.path.exists("output/QR-Code"):
        shutil.rmtree(f"output/QR-Code")
    if os.path.basename(sys.argv[0]).endswith("exe"):
        search_for_updates()
        clear()
        main()
    try:
        assert sys.version_info >= (3,9)
    except AssertionError:
        input(f"{y}[{Fore.RED}#{y}]{w} Sorry but, your python version ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) is not compatible with @TIO, please download python 3.9 or higher.")
        sys.exit()
    else:
        #search_for_updates()
        clear()
        main()
