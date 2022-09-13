import os
import commandok_v2
import webbrowser
from re import search
import file_editor




#----------------------------------------------------------------
try:
    with open("tarolas.txt","r",encoding='utf-8') as r:

        
        alist = [line.strip() for line in r]
        
        print(alist)
except:
    with open("tarolas.txt","a") as w:
        pass


#---------------------------------------------------------------
with open("tarolas.txt","a") as w:

    file = "tarolas.txt"

    print(f"\n(ebben a file-ban vagy most: {file})\n")
    szovag = ""
    while szovag != "exit":
            
            
        szovag = input("\nKérek egy szöveget amit tudok tárolni: ").lower()
           
        if szovag == "file_editor":
            file_editor.file_editor()
            szovag = ""
        
        if szovag == "clear":
            w.truncate(0)
            szovag = ""
            

        if szovag == "exit":
            szovag = ""
            break
            
        if szovag == "read":
            for i in alist:
                print(i)
         
        
                        
        w.writelines(f"{szovag}\n")
        

with open("tarolas.txt","r",encoding='utf-8') as r:

    
    alist = [line.strip() for line in r]
     
    print(alist)

with open("tarolas.txt","r",encoding='utf-8') as r:
    
    alist = [line.strip() for line in r]
    
    for parancs in alist:
        commandok_v2.commands(parancs)