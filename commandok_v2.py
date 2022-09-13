from importlib.resources import path
import os, sys, subprocess
import webbrowser
from sys import platform

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
        
def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])



def commands(command):
    
    try:
        objectum,item = command.split(";")
        
    except:
        pass
    else:
        #number;2,5,125,1
        if objectum in {"number"}:
            item = item.strip().split(",")
            item = list(map(int,item))
            return print(sum(item))

        #scream;kmggaga
        if objectum in {"scream"}:
            return print(item.upper())
        
        #creat_new_file;name
        if objectum in {"creat_new_file"}:
            path = os.getcwd()
            dir_list = os.listdir(path)
            with open(item, 'w') as fp:
                pass
            with open("tarolas.txt","a") as w:
                w.truncate(0)
            return print(f"Itt van a mappában lévő elemek: {dir_list}")
        
        #delet_file;name
        if objectum in {"delet_file"}:
            path = os.getcwd()
            dir_list = os.listdir(path)
            os.remove(item)
            with open("tarolas.txt","a") as w:
                w.truncate(0)
            return print(f"Itt van a mappában lévő elemek: {dir_list}")
        
        #i/h;1200,500,1000
        if objectum in {"i/h"}:
            lista = []
            name = None
            item = item.strip().split(",")
            item = list(map(int,item))
            for lolab in item:
                if lolab >= 1000:
                    name = True
                    lista.append(name)
                else:
                    name = False
                    lista.append(name)
            return print(f"\n{lista}")


            

    if command in {"open browser"}:
        url = "https://szabiszekely.github.io/HTML_Ossz/"
    
        if platform == "linux" or platform == "linux2":
            chrome_path = '/usr/bin/google-chrome %s'
        elif platform == "win32":
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

        
        

        return  webbrowser.get(chrome_path).open(url)
        
    if command in {"open file"}:
        cwd = os.getcwd()
        return open_file(cwd)

    if command in {"szia","mi ujság","hello"}:
        return print("Üdvözölek")
      
    if command in {"a"}:
        print("b")
    
    if command in {"b"}:
        print("a")

    if command in {"új"}:
        return print("régi")
    

    
    
    if command in {"info"}:
        file = "útmutató.txt"
        return open_file(file)
    
    