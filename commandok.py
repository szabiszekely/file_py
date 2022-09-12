from asyncore import write


class Commands_in_Text:
    def __init__(self,line):
        objectum,input_in = line.split(" ")
        
        self.objectum = objectum
        self.input_in = input_in
    
        if objectum == "string":
            objectum.write()
            
    def write(self):
        print("Strings in python are surrounded by either single quotation marks, or double quotation marks.")
    
        



def commands(command):
    str(command)
    if command in {"szia","mi ujság","hello"}:
        return print("Üdvözölek")
    
    if command in {"új"}:
        return print("régi")
    
    if command in {"a"}:
        print("b")
        
    else:
        return print("nincs ijen parancs")
    
    
with open("tarolas.txt","r",encoding='utf-8') as r:
    
    alist = [line.strip().split(" ") for line in r]
    
    for parancs in alist:
        Commands_in_Text(parancs)














