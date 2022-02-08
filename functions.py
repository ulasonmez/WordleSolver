def besHarfTxtOlustur():
    besHarfDosya = open("5harfkelimeler.txt","w",encoding="utf8")
    with open("kelimeler.txt","r",encoding="utf8") as file:
        for line in file:
            if len(line.strip().lower()) == 5:
                if(icindeVarMi(line)):
                    continue
                else:
                    besHarfDosya.write(line.lower())
def icindeVarMi(str1:str):
    with open("5harfkelimeler.txt","r",encoding="utf8") as file:
        for line in file:
            word = line.strip().lower()
            if word == str1.lower():
                return True
        return False
def harfYok(str1:str):
    eski = open("5harfkelimeler.txt","r",encoding="utf8")
    lines = eski.readlines()
    eski.close()
    yeni = open("5harfkelimeler.txt", "w", encoding="utf8")
    for line in lines:
        if str1 not in line.strip().lower():
            yeni.write(line)
    yeni.close()
def harfVar(str1:str):
    eski = open("5harfkelimeler.txt","r",encoding="utf8")
    lines = eski.readlines()
    eski.close()
    yeni = open("5harfkelimeler.txt", "w", encoding="utf8")
    for line in lines:
        if str1 in line.strip().lower():
            yeni.write(line)
    yeni.close()
def dogruYerde(str1:str,yeri: int):
    eski = open("5harfkelimeler.txt", "r", encoding="utf8")
    lines = eski.readlines()
    eski.close()
    yeni = open("5harfkelimeler.txt", "w", encoding="utf8")
    for line in lines:
        if str1 in line.strip().lower():
            if line.strip().lower()[yeri] == str1:
                yeni.write(line)

def dogruYerdeDegil(str1: str, yeri: int):
    eski = open("5harfkelimeler.txt", "r", encoding="utf8")
    lines = eski.readlines()
    eski.close()
    yeni = open("5harfkelimeler.txt", "w", encoding="utf8")
    for line in lines:
        if str1 in line.strip().lower():
            if line.strip().lower()[yeri]  != str1:
                yeni.write(line)

    yeni.close()