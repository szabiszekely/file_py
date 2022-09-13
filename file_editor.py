import commandok_v2



def file_editor():
    print("---------------------------------------------\nÜdvözölek a file editorban")
    file = input(f"\nAddj meg egy file nevet: ").lower()
    
    try:
        with open(file,"a") as w:
            pass
    except:
        print("smth went wrong")
    
    with open(file,"a") as w:
        
        print(f"\n(ebben a file-ban vagy most: {file})\n")
        szovag = ""
        while szovag != "exit":
            
        
            szovag = input("\nKérek egy szöveget amit tudok tárolni: ").lower()
            
            
            
            if szovag == "clear":
                w.truncate(0)
                szovag = ""
                

            if szovag == "exit":
                szovag = ""
                break
            
            
                            
            w.writelines(f"{szovag}\n")

    with open(file,"r",encoding='utf-8') as r:
    
        alist = [line.strip() for line in r]
        
        print("------------------------")
        for parancs in alist:
            commandok_v2.commands(parancs)









