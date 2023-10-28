import json
import os
from data.promptgen import generate

prompts = {}
options = {}
def load(prompts_path):
    global prompts,options
    pp = os.path.realpath(prompts_path)
    for i in os.listdir(pp):
        with open(pp + "/" + i,"r") as f:
            prompts[int(i.split(".")[0])] = json.loads(f.read())

    with open("./data/options.json","r") as f:
        options = json.loads(f.read())
    
    valid = []

    for key in prompts.keys():
        valid.append([key,len(prompts[key])])

    return valid

def gen():
    return generate(options,prompts)