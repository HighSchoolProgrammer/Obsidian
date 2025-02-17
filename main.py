import colorama
from colorama import *
import json
import shutil
import os
import time

# Initialize Program
colorama.init()
print(Style.RESET_ALL)

# Load Configuration
with open('config/info.json') as info_raw:
    info = json.load(info_raw)

with open('config/settings.json') as settings_raw:
    settings = json.load(settings_raw)

with open('config/user.json') as user_raw:
    user = json.load(user_raw)

# Define Variables
columns, rows = shutil.get_terminal_size()
command = ""
location = ""
version_info = ""
if info["version-type"] == "beta":
    version_info = Fore.CYAN + "v" + info["version"] + "-" + info["version-type"]
elif info["version-type"] == "indev":
    version_info = Fore.YELLOW + "v" + info["version"] + "-" + info["version-type"]
elif info["version-type"] == "stable":
    version_info = Fore.GREEN + "v" + info["version"] + "-" + info["version-type"]

# Define Functions
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        print(f"Continuing in {i}...", end="\r")
        time.sleep(1)
        print(" " * columns, end="\r") 

def splash():
    print("")
    print("")
    logo = """
 ██████╗ ██████╗ ███████╗██╗██████╗ ██╗ █████╗ ███╗   ██╗
██╔═══██╗██╔══██╗██╔════╝██║██╔══██╗██║██╔══██╗████╗  ██║
██║   ██║██████╔╝███████╗██║██║  ██║██║███████║██╔██╗ ██║
██║   ██║██╔══██╗╚════██║██║██║  ██║██║██╔══██║██║╚██╗██║
╚██████╔╝██████╔╝███████║██║██████╔╝██║██║  ██║██║ ╚████║
 ╚═════╝ ╚═════╝ ╚══════╝╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
"""
    centered_logo = "\n".join([line.center(int(columns)) for line in logo.split("\n")])

    print(Fore.WHITE + centered_logo)
    print(version_info.center(columns))
    print("")

def startupscreen():
    print(("                 " + Fore.WHITE + "Created by " + Fore.GREEN + info["author"] + Fore.WHITE + " on " + Fore.GREEN + "GitHub").center(columns))
    print("")
    print(("       " + Fore.WHITE + "This program is licensed under " + Fore.LIGHTMAGENTA_EX + info["license"]).center(columns))
    print("") 

    if info["version-type"] == "indev":
        print(("        " + Fore.RED + "WARNING: This version is in development. It may be unstable." + Fore.WHITE).center(columns))

# ----------------------------------------------
# Define Main Program

def main():
    clear()
    splash()
    print("")
    location = "obsidian"
    command = input(f"{user["name"]}@obsidian:~/{location}$ ")

# ----------------------------------------------

# Startup Screen
clear()
splash()
startupscreen()
countdown_timer(5)

# Main Program
main()



# break before quitting program
# input(Fore.WHITE + "Press Enter to Continue...")