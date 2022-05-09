import os


with open("tarolas.txt","a") as w:

  

    
    szovag = ""
    while szovag != "exit":
            
            
        szovag = input("\nKérek egy szöveget amit tudok tárolni: ").lower()
            
        
        if szovag == "clear":
            w.truncate(0)
            szovag = ""
        
        if szovag == "delet":
            os.remove("tarolas.txt")
        
        if szovag == "exit":
            w.writelines("-----------------------------------\n")
            
        w.writelines(f"{szovag}\n")


with open("tarolas.txt","r",encoding='utf-8') as r:

    
    alist = [line.strip() for line in r]
    #lista = []
    #lista.append(r.readlines())

    
    #read_content = r.read()

    #print(read_content) 
    print(alist)

