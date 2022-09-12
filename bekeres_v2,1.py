import os
import commandok_v1
import webbrowser

with open("tarolas.txt","a") as w:

  

    
    szovag = ""
    while szovag != "exit":
            
            
        szovag = input("\nKérek egy szöveget amit tudok tárolni: ").lower()
            
        
        if szovag == "clear":
            w.truncate(0)
            szovag = ""


        if szovag == "delet":
            os.remove("tarolas.txt")
            szovag = ""
            

        if szovag == "exit":
            szovag = ""
            break
            
        w.writelines(f"{szovag}\n")


with open("tarolas.txt","r",encoding='utf-8') as r:

    
    alist = [line.strip() for line in r]
    #lista = []
    #lista.append(r.readlines())

    
    #read_content = r.read()

    #print(read_content) 
    print(alist)

with open("tarolas.txt","r",encoding='utf-8') as r:
    
    alist = [line.strip() for line in r]
    
    for parancs in alist:
        commandok_v1.commands(parancs)