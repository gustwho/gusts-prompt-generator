import requests
with open("version","r") as f:
    if requests.get("https://raw.githubusercontent.com/gustwho/gusts-prompt-generator/main/version").text != f.read():
        input("Theres a new version! Download it at https://github.com/gustwho/gusts-prompt-generator/\n\n[OK]")