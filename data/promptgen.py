from datetime import datetime
import random

def generate(options,prompts):
    clist = []
    
    clist = options["Characters"]
    boldusername = options["BoldUsernames"]
    
    chars = len(clist)
    if not chars in list(prompts.keys()):
        return [False,"There isn't prompts for that amount of people."]

    text = "\n".join(random.choice(prompts[chars]))
    now = datetime.now()

    final = text.replace("{day}",now.strftime("%A"))
    for i,v in enumerate(clist,start=1):
        name = v
        if boldusername:
            name = f"**{v}**"
        
        final = final.replace("{" + str(i) + "}",name).replace(" :",":")

    return [True,final]