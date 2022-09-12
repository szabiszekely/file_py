import os
import webbrowser

"""
class Commands_in_Text:
    def __init__(self,line):
        objectum,input_in = line
        
        self.objectum = objectum
        self.input_in = input_in
    
        if objectum == "number":
            number(input_in)

        else:
            pass
            
        def number(self):
            return sum(self)
"""        
        



def commands(command):
    
    try:
        objectum,item = command.split(";")
        
    except:
        pass
    else:
        if objectum in {"number"}:
            item = item.strip().split(",")
            item = list(map(int,item))
            return print(sum(item))

        if objectum in {"scream"}:
            return print(item.upper())

    if command in {"open browser"}:
        url = "https://szabiszekely.github.io/HTML_Ossz/"
        try:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        except:
            chrome_path = '/usr/bin/google-chrome %s'
        else:
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
  

        return  webbrowser.get(chrome_path).open(url)
        
    if command in {"open file"}:
        cwd = os.getcwd()
        return os.startfile(cwd)

    if command in {"szia","mi ujság","hello"}:
        return print("Üdvözölek")
    
    if command in {"új"}:
        return print("régi")
    
    if command in {"a"}:
        print("b")
    
    if command in {"b"}:
        print("a")

    if command in {""," "}:
        pass

    if command in {"show basic commands"}:
        return os.startfile("All_command.txt")

    else:
        return print("nincs ijen parancs")
    
    






