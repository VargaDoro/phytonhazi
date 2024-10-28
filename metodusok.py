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
    elif(ora==0):
         print("Be se jövök!")
    elif(ora==1):
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


'''6/a Írj metódust, amelyben 13 véletlen egész számot generálunk [-5;12) intervallumban. A metódus térjen vissza a listával,
a következő függvények esetén ezzel a listával dolgozz tovább. Az eredmény kiírása mindig a main.py-ban történjen!
Hány pozitív és hány negatív szám van? '''

def hat():
    lista=[]
    for i in range(0, 13, 1):
        szam:int=int(random.random()*17)-5
        lista.append(szam)
    return lista

def hat_pozitiv(lista):
    i:int=0
    db:int=0
    while(i<len(lista)):
        if(lista[i]>0):
            db+=1
        i+=1
    return db

def hat_negativ(lista):
    i:int=0
    db:int=0
    while(i<len(lista)):
        if(lista[i]<0):
            db+=1
        i+=1
    return db


'''6/b Mennyi a páros számok összege? 
A páros, vagy a páratlan számok összege a nagyobb? 
Mennyi a számok átlaga? 
Mekkora a legnagyobb szám?'''

def hat_paros_ossz(lista):
    i:int=0
    ossz:int=0
    while(i<len(lista)):
        if(lista[i]%2==0):
            ossz+=lista[i]
        i+=1
    return ossz

def hat_paratlan_ossz(lista):
    i:int=0
    ossz1:int=0
    while(i<len(lista)):
        if(lista[i]%2!=0):
            ossz1+=lista[i]
        i+=1
    return ossz1

def hat_atlag(lista):
    atlag = sum(lista) / len(lista)
    return atlag

def hat_legnagyobb(lista):
    legnagyobb=max(lista)
    return legnagyobb


'''7. Írj metódust, mely neveket kér a felhasználótól addig amíg a „@” jelet nem kapja. 
Hány nevet adott meg a felhasználó? 
Van-e benne A betűvel kezdődő név? 
Melyik a leghosszabb név? '''

def het():
    i = input("Adj megy egy nevet (@-jelet kilépéshez): ")
    tarolas = []
    while i != "@":
        tarolas.append(i)
        i = input("Adj meg egy szót (@-jelet kilépéshez): ")
    return tarolas

def het_mennyi(tarolas):
    nevek_szama=len(tarolas)
    return nevek_szama

def het_a(tarolas):
    for nev in tarolas:
        if nev.startswith('A') or nev.startswith('a'):
            a_betu=("Van benne 'A' betűvel kezdődő név")  
        else:
            a_betu=("Nincs benne 'A' betűvel kezdődő név")
    return a_betu

def het_leghosszabb(tarolas):
    leghosszabb=max(tarolas, key=len)
    return leghosszabb


'''8.	Írj metódust, mely egy érmedobás eredményét kéri be a felhasználótól 10-szer egymás után!
A felhasználó minden lépésben a „f” vagy  „i” betűket kell megadjon. Addig kérd be a jeleket, amíg jó jelet nem ad meg. 
Hányszor adott meg „f” betűt? 
Mekkora a leghosszabb f sorozat?'''

def nyolc():
    tarolas = []
    while(len(tarolas)<10):
        dobas = input("Add meg az érmedobás eredményét (csak 'i' vagy 'f'-et): ")
        if dobas == "i" or dobas == "f":
            tarolas.append(dobas)
        else:
            print("Helytelen jelet adott meg!")
    return tarolas

def nyolc_f(tarolas):
    i:int=0
    db:int=0
    while(i<len(tarolas)):
        if tarolas[i]=="f":
            db+=1
        i+=1
    return db

def nyolc_leghosszabb(tarolas):
    leghosszabb_f:int=0
    i:int=0
    for dobas in tarolas:
        if dobas=="f":
            i += 1
            leghosszabb_f=max(leghosszabb_f, i)
        else:
            i=0
    return leghosszabb_f


'''9.	Írj programot, ami kiírja a 10x10-es alapú szorzótáblát! 10-esével egymás alá! használj hozzá formázott kiiratást!'''

def kilenc():
    i:int = 1
    while(i<=10):
        n:int = 1
        while(n <= 10):
            print(f"{i * n:>3}", end=' ')
            n += 1
        print()
        i += 1


'''10.	Írj metódust, mely a paraméterében kapott számról megmondja, hogy hány 1-es, 10-es, 100 - as, 1000 - es, stb van benne!
 használd hozzá az egész osztás operátorát - // ! pl: 123//10 =12  123%10=3'''

def tiz(szam:int):
    egyesek = szam % 10
    tizesek = (szam // 10) % 10
    szazak = (szam // 100) % 10
    ezer = (szam // 1000) % 10
    print(f"A(z) {szam} szám jellemzői:")
    print(f"1-esek: {egyesek}")
    print(f"10-esek: {tizesek}")
    print(f"100-asok: {szazak}")
    print(f"1000-esek: {ezer}")


'''11.	+++ Írj eljárást, mely paraméterében kap egy számot, majd összeadja a számjegyeket és kiírja a számjegyek összegét a képernyőre. 
PL. 324 -> „324 számjegyeinek összege: 9”'''

def tizenegy(szam:int):
    szam_str = str(szam)
    osszeg = 0
    for i in range(len(szam_str)):
        osszeg+=int(szam_str[i])
    print(f"A {szam} számjegyeinek összege: {osszeg}")


'''12.	++ Írj programot, mely beolvas egy pozitív egész számot, és megmondja, hogy tökéletes szám-e! (A tökéletes számok azok,
melyek osztóinak összege egyenlő a szám kétszeresével. Ilyen szám pl. a 6, mert 2*6 = 1 + 2 + 3 + 6.)'''

def tizenketto():
    szam:int=int(input("Adj meg egy pozitív számot: "))
    oszto:int = 1
    osszeg:int = 0
    while(oszto<szam): 
        if szam%oszto==0:
            osszeg+=oszto
        oszto+=1
    if osszeg==szam:
        print("A szám tökéletes")
    else:
        print("A szám nem tökéletes")


'''13.	++ Írj metódust, ami paraméterében kap két számot, és kiírja a két szám legnagyobb közös osztóját!
Segítség::: A kisebbik számtól visszafelé nézzük, hogy van-e közös osztó. Nincs, ha az egyet elértük.'''

def legnagyobb_kozos_oszto(a, b):
    while b:
        a, b = b, a % b
    return a
def tizenharom():
    szam1:int = int(input("Adj meg egy számot: "))
    szam2:int = int(input("Adj meg egy kisebb számot: "))
    lko = legnagyobb_kozos_oszto(szam1, szam2)
    print(f"A {szam1} és {szam2} legnagyobb közös osztója: {lko}")


'''1. ++Írj metódust, ami paraméterében kap két számot, és kiírja a legkisebb közös többszörösüket! Segítség: 
Indulj a nagyobb számtól egyesével és keresd meg azt a számot, amelyet mindkettő oszt! Meddig kell mennie a ciklusnak? '''

def legkisebb_kozos_tobbszoros(a, b):
    nagyobb = max(a, b)
    while True:
        if nagyobb % a == 0 and nagyobb % b == 0:
            return nagyobb
        nagyobb += 1
def tizennegy(szam1:int, szam2:int):
    lkt = legkisebb_kozos_tobbszoros(szam1, szam2)
    print(f"A {szam1} és {szam2} legkisebb közös többszörösük: {lkt}")


'''1.feladat:	Egy a természettel  Vadászati és Természeti Világkiállításon téged bíztak meg, hogy egy kihelyezett információs
tábla részműködését leprogramozd! 
A felhasználónak be kell gépelnie melyik szektort szeretné megnézni, a te programod pedig kiírja az ott található kiállítás nevét.
•	A esetén Nemzetközi Csarnok, World Conservation Forum 2021
•	B és E esetén a Kereskedelmi Csarnok felirat jelenjen meg
•	C esetén Konferencia-központ Innovációs Showroom
•	D esetén Hal, Víz és Ember
•	F esetén Hagyományos Vadászati Módok Csarnoka
•	G Hazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21.században kiállítás
•	H esetben Központi Magyar Kiállítás
•	Minden egyéb nem szám adatra írja ki, hogy forduljon a pénztárhoz.
Pl1: 
Be: Szektor: D
Ki: Hal, Víz és Ember
Pl2:
Be: Szektor: 4
Ki: HIBA: Adjon meg egy betűt A-H-ig!'''

def tizenot(szektor):
    if szektor == "A":
        print("Nemzetközi Csarnok, World Conservation Forum 2021")
    elif szektor == "B" or szektor=="E":
        print("Kereskedelmi Csarnok")
    elif szektor=="C":
        print("Konferencia-központ Innovációs Showroom")
    elif szektor=="D":
        print("Hal, Víz és Ember")
    elif szektor == "F":
        print("Hagyományos Vadászati Módok Csarnoka")
    elif szektor=="G":
        print("Hazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21.században kiállítás")
    elif szektor=="H":
        print("Központi Magyar Kiállítás")
    else:
        print("Forduljon a pénztárhoz!")
