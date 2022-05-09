import os


os.remove("tarolas.txt")



with open("tarolas.txt","a") as f:
    
    while szovag in {exit}:
        szovag = input("\nKérek egy szöveget amit tudok tárolni: ").lower()
        if szovag in {""}:
            f.write("\n")
        f.write(f"{szovag}\n")


