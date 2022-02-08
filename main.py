import random
import functions
from termcolor import colored

functions.besHarfTxtOlustur()
wordle_kelime = "çapak"
olmayan_harfler = []
# 0 yok 1 doğru yerde 2 yanlış yerde

kelimen = random.choice(open('5harfkelimeler.txt',encoding="utf8").read().splitlines())
count = 0

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
var = {

}
for a in var:
    if var.get(a) == 0:
        functions.harfYok(a)
    elif var.get(a) == 1:
        functions.dogruYerde(kelimen[i], i)

print(count)
print(colored(kelimen,"green"))

