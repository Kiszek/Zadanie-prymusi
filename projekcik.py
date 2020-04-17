import random

def generuj_slowo_z_bazy():
    plik = open("C:\\Users\\Bartłomiej\\Desktop\\baza_slow.txt")
    #tutaj należy wstawić ścieżkę dostępu do pliku( jeśli windows to podwójne slashe
    slowa = []
    for line in plik:
        slowa.extend(line.strip().split())
    word = slowa[random.randrange(0, len(slowa))]
    return word

def validate_input(wpisane):
    invalid=0
    while not invalid:
        x = input()
        if x in wpisane:
            print("Już tego użyto głuptasku :) ")
        elif (x.isalpha()) and (len(x)==1):
            invalid = 1
            return x
        else:
            print("Podaj proszę jeden znak alfabetu łacińckiego,"
                  " jeśli możesz to mały i taki,"
                  " którego jeszcze nie wykorzystałeś")

def list_to_string(list):
    str=""
    for i in list:
        str+=i
    return str

if __name__=="__main__":
    iterator = 3
    odgadnione=set([])
    zapytane=set([])
    szukane = generuj_slowo_z_bazy()
    rezultat=["_"]*len(szukane)

    print("Zagrajmy w wisielca! "
          "Ja wyznaczę słowo, a Ty wpisuj"
          " pojedyńcze małe litery alfabetu łacińskiego" )
    print("Długosć słowa to:")
    print(len(szukane))
    print("Zacznij zgadywać, masz 3 szanse ;)")
    print("Powodzenia!")
    while iterator:
        sprawdzacz_zgodności = 1
        x = validate_input(zapytane)
        zapytane.add(x)
        if x in szukane:
            odgadnione.add(x)
        else:
            iterator-=1

        for i in range(len(szukane)):
            if szukane[i] in odgadnione:
                rezultat[i]=szukane[i]
        print(list_to_string(rezultat), "Masz jeszcze", iterator, "szanse")

        for i in range(len(szukane)):
            if szukane[i] != rezultat[i]:
                sprawdzacz_zgodności=0
        if sprawdzacz_zgodności:
            print("Gratulacje, zostałem pokonany!")
            exit(0)
    print("ojj, nie wyszło :(")
    print("Hasłem było:")
    print(szukane)
    exit(0)