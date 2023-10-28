import requests
with open("version","r") as f:
    latest = int(requests.get("https://raw.githubusercontent.com/gustwho/gusts-prompt-generator/main/version").text)
    current = int(f.read())
    if latest > current:
        input(f"Theres a new version! Download it at https://github.com/gustwho/gusts-prompt-generator/\n\nYou are {latest-current} versions behind!\n\n[OK]")