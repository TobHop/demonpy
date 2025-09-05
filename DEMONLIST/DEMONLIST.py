import datetime
import webbrowser
import colorama
import os
import sys

from colorama import Fore, Back, Style

from colorama import just_fix_windows_console

just_fix_windows_console()

colorama.init(autoreset=True)

demonascii = r"""
     @            @@                     @@            @     
    @-@          @-@                     @-@          @-@    
    @-@         @---=@        @        @=---@         @-@    
   @---=@      @-====#@@@###########@@@*====-@      @=---@   
   @-----@     @==@@#####################@@==@     @-----@   
   @-------@@  @@###########################@@  @@-------@   
   @------===*@###############################@+===------@   
   @----====@##################################%@====----@   
    @--====@#####################################@====--@    
    @-====@###@###############################@###@====-@    
     @===@#%***@#############################@***%#@===@     
      @@@#@*+++=-@#########################@-=+++*@#@@@      
@@@     @#@++====---@###################@---====++@#@     @@@
@----==@%###@=-----====@@###########@@====-----=@###@@==----@
@----==@%#%#####%@@@@**#@@@#%%%%%#@@@#**@@@@%#####%#%@==----@
 @---==@%%%%%%%@@@@####%%%@%%%%%%%@%%%####@@@@%%%%%%%@==---@ 
  @--==@%%%%@@-----@--=@@@%%%%%%%%%@@@---@-----@@%%%%@==--@  
   @@-=%@%%@@@@----@----------@----------@----@@@@%%@*=-@@   
      @#@%%@@@@@---@---@@-----@-----@@---@---@@@@@%%@#@      
        @@@@@@@@@@@@@@@@@@@#@@@@@#@@@@@@@@@@@@@@@@@@@        
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         
          @@@@@--@@@%--@@@---@@@---@@@--%@@@--@@@@@          
           @@%----@-----@@%**@@@**%@@-----@----%@@           
           @@-----@@@@@@@%%%%%%%%%%%@@@@@@@-----@@           
            @@@@@@@@%%%%%%%%%%%%%%%%%%%%%@@@@@@@             
                @@@@@@@@@@%%%%%%%%%@@@@@@@@@                 
                   @@@@@@@@@@@@@@@@@@@@@@@                   
                        @@@@@@@@@@@@@         """

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def mainline():
    clear_console()
    print("---PYDEMON POINTERCRATE DEMON LIST v2.0---")
    print(Fore.CYAN + "1 - Fetch Lists (Main, Extended, Legacy)...")
    print(Fore.CYAN + "2 - Get Info On A Demon (Main, Extended, Legacy)...")
    print(Fore.CYAN + "3 - CREDITS!...")

    choice = int(input("What Would You Like Me To Do?... "))
    if choice == 1:
     clear_console()
     print("---LISTS---")
     print(Fore.CYAN + "1 - Main List (1-75)...")
     print(Fore.CYAN + "2 - Extended List (76-150)...")
     print(Fore.CYAN + "3 - Legacy List (151-600)...")
     listchoice = int(input("What List Would You Like To Fetch?... "))
     if listchoice == 1:
         print(Fore.YELLOW + "Fetching From Pointercrate API... May Take A While If Pointercrate Is Experiencing High Traffic...")
         fetchmainlist()
         print(Fore.RED + "(Scoll To Top For Top 1!)")
         input("Press Enter To Return To The Main Menu...")
         mainline()
     if listchoice == 2:
         print(Fore.YELLOW + "Fetching From Pointercrate API... May Take A While If Pointercrate Is Experiencing High Traffic...")
         fetchextendedlist()
         print(Fore.RED + "(Scoll To Top For Top 76!)")
         input("Press Enter To Return To The Main Menu...")
         mainline()
     if listchoice == 3:
         print(Fore.YELLOW + "Fetching From Pointercrate API... May Take A While If Pointercrate Is Experiencing High Traffic...")
         print(Fore.RED + "This takes longer because it fetches the demons in multiple requests...")
         fetchlegacylist()
         print(Fore.RED + "(Scoll To Top For Top 151!)")
         input("Press Enter To Return To The Main Menu...")
         mainline()
     else:
         print(Fore.RED + "Please Enter A Valid List Option... ")
         input(Fore.CYAN + "Press Enter To Return To The Main Menu.. ")
         mainline()

    if choice == 2:
     clear_console()
     print("---LISTS---")
     print(Fore.CYAN + "1 - Main List (1-75)...")
     print(Fore.CYAN + "2 - Extended List (76-150)...")
     print(Fore.CYAN + "3 - Legacy List (151+)...")
     listchoice = int(input("Which List Would You Like To Search?... "))
     if listchoice == 1:
         print(Fore.YELLOW + "Fetching From Pointercrate API... May Take A While If Pointercrate Is Experiencing High Traffic...")
         infofetch()
     if listchoice == 2:
         print(Fore.YELLOW + "Fetching From Pointercrate API... May Take A While If Pointercrate Is Experiencing High Traffic...")
         extendedinfofetch()
     if listchoice == 3:
         print(Fore.YELLOW + "Fetching From Pointercrate API... May Take A While If Pointercrate Is Experiencing High Traffic...")
         legacyfetch()
     else:
         print(Fore.RED + "Please Enter A Valid List Option... ")
         input(Fore.CYAN + "Press Enter To Return To The Main Menu.. ")
         mainline()
    if choice == 3:
         clear_console()
         print(Fore.RED + demonascii)
         print("CREDITS!:")
         print(Fore.CYAN + "TobHop - Fetcher Program:")
         print("LIBRARIES!:")
         print(Fore.BLUE + "pointercratepy - https://pypi.org/project/pointercratepy/")
         print(Fore.BLUE + "colorama - https://pypi.org/project/colorama/")
         print("       *******                                                                           ")
         print(Fore.GREEN + "###### ********### ##   ## ####### ###### ######  ######  ######    ###  ###### #######         ")
         print(Fore.GREEN + "##  ##*********=## ###  ##   ##    ##     ##  ### ##  ##* ##  ##   ####    ##   ###                ")
         print(Fore.GREEN + "## *##******** =##:#### ##   ##    #####  ##  ### ##      ##  ##   ## ##   ##   ######  ***** ** ** ")
         print(Fore.GREEN + "######*::::::::=##:## ####   ##    ##     ######  ##   #  ######  ##  ##   ##   ###     ** **  ***  ")
         print(Fore.GREEN + "##  ***::::::::=## ##  ###   ##    ##     ##  ##  ##  ##* ##  ##  #######  ##   ###     ****    **  ")
         print(Fore.GREEN + "##     ::::::::### ##   ##   ##    ###### ##  ###  #####  ##  ## ##    ##  ##   ######* **      **  ")
         print(Fore.GREEN + "       :::::::                    ")
         input(Fore.CYAN + "Press Enter To Return To The Main Menu.. ")
         mainline()






def infofetch():
    clear_console()
    listno = int(input("Enter A List Number. 1-75... ")) - 1

    if listno < 0 or listno > 74:
        print(Fore.RED + "Please enter a valid MAIN list position, choose 1 in the search menu to search the extended list.")
        input("Press Enter To Return To The Main Menu...")
        mainline()
    else:
         print(Fore.YELLOW + "Fetching From Pointercrate API... May Take A While If Pointercrate Is Experiencing High Traffic...")
         from pointercratepy import Client

         client = Client()

         demons = client.get_demons(limit=100)

         clear_console()
         print(f"---{demons[listno].get('name')} Info---")
         print(Fore.CYAN + "Name: " + demons[listno].get("name"))
         print(Fore.YELLOW + "Publisher: " +  demons[listno].get("publisher", {}).get("name"))
         print(Fore.CYAN + "Verifier: " +  demons[listno].get("verifier", {}).get("name"))
         print(Fore.GREEN + "Showcase: " +  demons[listno].get("video"))
         openshow = input("Would you like to open the showcase in your preferred browser? (Y/N) ")
         if openshow == "y":
           webbrowser.open(demons[listno].get("video"))
         elif openshow == "n":
           input("Press Enter To Return To The Menu... ")
           mainline()

def extendedinfofetch():
    clear_console()
    listno = int(input("Enter An EXTENDED List Number. 76-150... ")) - 101

    if listno < 0 or listno > 74:
        print(Fore.RED + "Please enter a valid EXTENDED list position, choose 2 in the search menu to search the main list.")
        input("Press Enter to return to the main menu...")
        mainline()
    else:
         print(Fore.YELLOW + "Fetching From Pointercrate API... May Take A While If Pointercrate Is Experiencing High Traffic...")

         from pointercratepy import Client

         client = Client()

         demons = client.get_demons(limit=50, after=100)

         clear_console()

         print(f"---{demons[listno].get('name')} Info---")
         print(Fore.CYAN + "Name: " + demons[listno].get("name"))
         print(Fore.YELLOW + "Publisher: " +  demons[listno].get("publisher", {}).get("name"))
         print(Fore.CYAN + "Verifier: " +  demons[listno].get("verifier", {}).get("name"))
         print(Fore.CYAN + "Position: " + str(demons[listno].get("position")))
         print(Fore.GREEN + "Showcase: " +  demons[listno].get("video"))
         openshow = input("Would you like to open the showcase in your preferred browser? (Y/N) ")
         if openshow == "y":
            webbrowser.open(demons[listno].get("video"))
         elif openshow == "n":
            input("Press Enter To Return To The Menu... ")
            mainline()

def legacyfetch():
    clear_console()
    listno = int(input("Enter An LEGACY List Number. 151+... ")) - 151
    if listno < 0 or listno > 600:
        print(Fore.RED + "Please enter a valid LEGACY list position.")
        input("Press Enter to return to the main menu...")

        mainline()
    else:
         print(Fore.YELLOW + "Fetching From Pointercrate API... May Take A While If Pointercrate Is Experiencing High Traffic...")
         print(Fore.RED + "This takes longer because it fetches the demons in multiple requests...")

         from pointercratepy import Client

         client = Client()

         legacybatch1 = client.get_demons(limit=100, after=150)

         demons = legacybatch1

         legacybatch2 = client.get_demons(limit=100, after=250)

         demons = legacybatch1 + legacybatch2

         legacybatch3 = client.get_demons(limit=100, after=350)

         demons = legacybatch1 + legacybatch2 + legacybatch3

         legacybatch4 = client.get_demons(limit=100, after=450)

         demons = legacybatch1 + legacybatch2 + legacybatch3 + legacybatch4

         legacybatch5 = client.get_demons(limit=50, after=550)

         demons = legacybatch1 + legacybatch2 + legacybatch3 + legacybatch4 + legacybatch5


         clear_console()

         print(f"---{demons[listno].get('name')} Info---")
         print(Fore.CYAN + "Name: " + demons[listno].get("name"))
         print(Fore.YELLOW + "Publisher: " +  demons[listno].get("publisher", {}).get("name"))
         print(Fore.CYAN + "Verifier: " +  demons[listno].get("verifier", {}).get("name"))
         print(Fore.CYAN + "Position: " + str(demons[listno].get("position")))
         print(Fore.GREEN + "Showcase: " +  demons[listno].get("video"))
         openshow = input("Would you like to open the showcase in your preferred browser? (Y/N) ")
         if openshow == "y":
            webbrowser.open(demons[listno].get("video"))
         elif openshow == "n":
            input("Press Enter To Return To The Menu... ")
            mainline()





def fetchmainlist():
 from pointercratepy import Client

 client = Client()

 demons = client.get_demons(limit=75)

 clear_console()
 print("---The Main List As Of " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S---")))

 for i, demons in enumerate(demons, start=1):
     print(Fore.WHITE + f"{i}. {demons.get('name')}" + Fore.CYAN + " - Published By: " + Fore.CYAN + demons.get("publisher", {}).get("name"))

def fetchextendedlist():
 from pointercratepy import Client

 client = Client()

 demons = client.get_demons(limit=75, after=75)

 clear_console()
 print("---The Extended List As Of " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S---")))

 for i, demons in enumerate(demons, start=76):
     print(Fore.WHITE + f"{i}. {demons.get('name')}" + Fore.CYAN + " - Published By: " + Fore.CYAN + demons.get("publisher", {}).get("name"))

def fetchlegacylist():
 from pointercratepy import Client

 client = Client()

 legacybatch1 = client.get_demons(limit=100, after=150)

 demons = legacybatch1

 legacybatch2 = client.get_demons(limit=100, after=250)

 demons = legacybatch1 + legacybatch2

 legacybatch3 = client.get_demons(limit=100, after=350)

 demons = legacybatch1 + legacybatch2 + legacybatch3

 legacybatch4 = client.get_demons(limit=100, after=450)

 demons = legacybatch1 + legacybatch2 + legacybatch3 + legacybatch4

 legacybatch5 = client.get_demons(limit=50, after=550)

 demons = legacybatch1 + legacybatch2 + legacybatch3 + legacybatch4 + legacybatch5

 clear_console()

 print("---The Legacy List As Of " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S---")))

 for i, demons in enumerate(demons, start=151):
     print(Fore.WHITE + f"{i}. {demons.get('name')}" + Fore.CYAN + " - Published By: " + Fore.CYAN + demons.get("publisher", {}).get("name"))


mainline()