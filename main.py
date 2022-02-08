import random
import functions
from termcolor import colored
functions.besHarfTxtOlustur()
# 0 yok 1 doğru yerde 2 yanlış yerde
"""
while kelimen!=wordle_kelime:
    count += 1
    for i in range(0,len(kelimen)):
        if kelimen[i] not in wordle_kelime:
            functions.harfYok(kelimen[i])
        else:
            #aynı yer
            if(kelimen[i] == wordle_kelime[i]):
                functions.dogruYerde(kelimen[i],i)
            #farklı yerdeyse
            else:
                functions.dogruYerdeDegil(kelimen[i],i)

    kelimen = random.choice(open('5harfkelimeler.txt', encoding="utf8").read().splitlines())
"""
dogruluk = ""
kelimen = random.choice(open('5harfkelimeler.txt',encoding="utf8").read().splitlines())
print(kelimen)
while dogruluk != '11111':
    dogruluk = str(input('dogruluk giriniz'))
    if len(dogruluk) == 5:
        for i in range(0,5):
            if dogruluk[i] == '0':
                functions.harfYok(kelimen[i])
            elif dogruluk[i] == '1':
                functions.dogruYerde(kelimen[i],i)
            elif dogruluk[i] == '2':
                functions.dogruYerdeDegil(kelimen[i],i)
    kelimen = random.choice(open('5harfkelimeler.txt', encoding="utf8").read().splitlines())
    print(kelimen)

print(colored(kelimen,"green"))

