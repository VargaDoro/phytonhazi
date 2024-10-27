import math
import random

'''1.	Kérj be egy [200, 920] intervallumban lévő egész számot 
(ha nem ebben az intervallumban van, jelezz hibát!), majd írasd ki az első számjegyét!'''

def elso():
    szam:int=int(input("Adj megy egy [200, 920] intervallumban lévő egész számot: "))
    while(szam<200 or szam>920):
            print("A megadott intervallumba adj meg számot!")
            szam:int=int(input("Adj megy egy [200, 920] intervallumban lévő egész számot: "))
    elso=str(szam)[0]
    print("Az első számjegy:", elso)


'''2.	Egy hétfői napon az 1-es csoportnak 9 órája van. Az első órában a teljesítményük 90%-át képesek nyújtani. A 2-3. órában már kissé
 éhesek, és csupán 60%-os a munkabírásuk. A 4-7. órában szerencsére programozást tanulnak, 
 így némiképp javul a hatékonyságuk (70%), a 8-9. órában azonban már újra lecsökken (50%).
Írj metódust, mely paraméterében kap egy egész számot 1 és 9 között (melyik órán vannak; jelezz hibát,
 ha nem ebben az intervallumban lévő számot kapsz, pl. “Ez már tényleg túlzás.”). Példa egy esetre: Be: 3, Ki: “Még bírjuk (60%).”  
  -  nem kell tesztfüggvényeket írni, de az alábbi táblázat alapján ellenőrizzétek a munkátokat!'''

def masodik(ora):
    if(ora>9):
        print("Ez már tényleg túlzás.")
    if(ora==0):
         print("Be se jövök!")
    if(ora==1):
        print("Még 90% on vagyunk!")
    elif(ora in [2, 3]):
        print("Még bírjuk (60%)")
    elif(ora in [4, 5, 6, 7]):
        print("Progit tanulunk, töltődünk! 70%")
    elif(ora in [8, 9]):
        print("Lassan nem bírjuk tovább! 50%")


'''3. Az egyik diák (legyen Márti a neve) az alábbi algoritmus alapján tevékenykedik az órákon:
        a.	hétfőn alszik az összes órán,
        b.	kedden csak hittan órán figyel,
        c.	programozás órán dolgozik, de csak szerdán
        d.	csütörtökön minden órán figyel, mert jó kedve van (aznap szokott moziba menni),
        e.	pénteken a hétvégéről ábrándozik, így csak félig figyel minden aznapi órán,
        f.	a többi óráról semmit nem tudunk.
    Írj metódsut, melynek  2 bemenő prarmétere van (nap neve, óra neve) és tájékoztatást ad Márti állapotáról. '''

def harom(nap_neve, ora_neve):
    if nap_neve == "hétfő" and (ora_neve == "programozás" or ora_neve == "bármi" or ora_neve == "hittan"):
        print("alszik")
    elif nap_neve == "kedd" and ora_neve == "hittan":
        print("figyel")
    elif nap_neve == "kedd" and (ora_neve == "programozás" or ora_neve == "bármi"):
        print("alszik")
    elif nap_neve == "szerda" and ora_neve == "programozás":
        print("dolgozik")
    elif nap_neve == "szerda" and (ora_neve == "hittan" or ora_neve == "bármi"):
        print("nincs info")
    elif nap_neve == "csütörtök" and (ora_neve == "programozás" or ora_neve == "bármi" or ora_neve == "hittan"):
        print("figyel")
    elif nap_neve == "csütörtök" and (ora_neve == "programozás" or ora_neve == "bármi" or ora_neve == "hittan"):
        print("félig van jelen")


'''4. A program számítsa ki egy beolvasott valós szám négyzetgyökét! 
A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!'''

def negy():
    szam:float=float(input("Adj meg egy számot: "))
    while(szam<0):
       print("A szám negatív!")
       szam:int=int(input("Adj meg egy számot: ")) 
    gyok = math.sqrt(szam)
    print(f"A(z) {szam} négyzetgyöke: {gyok}")


'''5.	A program olvasson be a konzolról két valós számot! Ha mindkét szám pozitív, akkor legyenek
a beolvasott számok egy téglalap oldalai. A program számítsa ki a téglalap kerületét, 
területét, és írja ki két tizedesre kerekítve az eredményeket a konzolra! Hiba esetén írja ki: "Hiba: a téglalap oldalai nem pozitívak!"!'''

def ot():
    szam1:float=float(input("Adj meg egy számot: "))
    szam2:float=float(input("Adj meg egy számot: "))
    while szam1<=0 or szam2<=0:
        print("Hiba: a téglalap oldalai nem pozitívak!")
        szam1:float=float(input("Adj meg egy számot: "))
        szam2:float=float(input("Adj meg egy számot: ")) 
    terulet=szam1*szam2
    kerulet=2*(szam1+szam2)
    print(f"A téglalap kerülete: {kerulet:.2f} a területe: {terulet:.2f}")


'''6.	Írj metódust, amelyben 13 véletlen egész számot generálunk [-5;12) intervallumban. A metódus térjen vissza a listával,
a következő függvények esetén ezzel a listával dolgozz tovább. Az eredmény kiírása mindig a main.py-ban történjen!
Hány pozitív és hány negatív szám van? '''

def hat():
