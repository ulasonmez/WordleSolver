import random
import functions
from termcolor import colored
toplam = 0
for i in range(0,500):
    functions.besHarfTxtOlustur()
    wordle_kelimesi = random.choice(open('5harfkelimeler.txt', encoding="utf8").read().splitlines())
    dogruluk = ""
    kelimen = random.choice(open('5harfkelimeler.txt', encoding="utf8").read().splitlines())
    count = 1
    while dogruluk != '11111':
        count += 1
        dogruluk = ""
        for i in range(0, 5):
            if kelimen[i] not in wordle_kelimesi:
                dogruluk += "0"
            else:
                if kelimen[i] == wordle_kelimesi[i]:
                    dogruluk += "1"
                else:
                    dogruluk += "2"
        if len(dogruluk) == 5:
            for i in range(0, 5):
                if dogruluk[i] == '0':
                    functions.harfYok(kelimen[i])
                elif dogruluk[i] == '1':
                    functions.dogruYerde(kelimen[i], i)
                elif dogruluk[i] == '2':
                    functions.dogruYerdeDegil(kelimen[i], i)
        kelimen = random.choice(open('5harfkelimeler.txt', encoding="utf8").read().splitlines())

    print(colored(f'{count} denemede bulunan kelime = {kelimen}', "green"))
    toplam += count
print(f'toplam = {toplam}, ortalama = {toplam/100}')

