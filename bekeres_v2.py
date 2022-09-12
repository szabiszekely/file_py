import os
import commandok_v1
import webbrowser

def file(szovag):
    with open("tarolas.txt","a") as w:

        
        
                
            
        if szovag == "clear":
            w.truncate(0)
            szovag = ""

        if szovag in {""," "}:
            pass


        
            
        w.writelines(f"{szovag}\n")


def lista():
    with open("tarolas.txt","r",encoding='utf-8') as r:

        
        alist = [line.strip() for line in r]
        #lista = []
        #lista.append(r.readlines())

        
        #read_content = r.read()

        #print(read_content) 
        print(alist)
def commandok():
    with open("tarolas.txt","r",encoding='utf-8') as r:
        
        alist = [line.strip() for line in r]
        
        for parancs in alist:
            commandok_v1.commands(parancs)