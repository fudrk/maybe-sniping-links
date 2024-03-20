import requests
import time
import sys
print("\n")
print_red("                               > fudrk sniper                                            \n")
print_red("                               > https://github.com/fudrk                             \n")

def ask(question):
    return input(f"\033[36m> {question}:\033[0m ")

token = ask("Your Account Token")  #ur acc token, not bot
guild_id = ask("Your Server ID")
webhook_url = ask("Discord webhook URL")
vanity_url = ask("Vanity URL")

headers = {
    "authorization": token,
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

def check_vanity():
    while True:
        try:
            if vanity_url == "":
                print('\033[36m> Vanity URL is empty, waiting for a new URL...\033[0m')
            else:
                response = requests.get(f"https://discord.com/api/v9/invites/{vanity_url}?with_counts=true&with_expiration=true", headers=headers)
                if response.status_code == 404:
                    print('\033[36m> Changing Vanity URL:', vanity_url, '\033[0m')
                    change_vanity()
                else:
                    print('\033[36m> Vanity URL still active:', vanity_url, '\033[0m')
            time.sleep(0.2)
        except Exception as error:
            print('\033[31m> Rate limited :(\033[0m')
            time.sleep(5)

def change_vanity():
    payload = {"code": vanity_url}
    response = requests.patch(f"https://discord.com/api/v10/guilds/{guild_id}/vanity-url", headers=headers, json=payload)
    if response.status_code == 200:
        print('\033[36m> URL changed:', vanity_url, '\033[0m')
        data = {
            "content": f"@everyone discord.gg/{vanity_url} yours now!",
            "username": "fudrk",
            "avatar_url": "https://i.imgur.com/O3EIPHp.gif"
        }
        requests.post(webhook_url, json=data)
        sys.exit()
    else:
        print('\033[36m> Vanity URL could not be changed, error code:', response.status_code, '\033[0m')

check_vanity()
