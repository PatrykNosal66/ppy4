import math

def liczba_opakowan(dlugosc_podlogi, szerokosc_podlogi, dlugosc_panela, szerokosc_panela, liczba_paneli_w_opakowaniu):
    powierzchnia_pomieszczenia = (dlugosc_podlogi * szerokosc_podlogi) * 1.1
    powierzchnia_panela = dlugosc_panela * szerokosc_panela
    liczba_paneli_potrzebna = math.ceil(powierzchnia_pomieszczenia / powierzchnia_panela) # zaokrąglanie w górę do całkowitej ilości paneli
    liczba_opakowan_potrzebna = math.ceil(liczba_paneli_potrzebna / liczba_paneli_w_opakowaniu) # zaokrąglanie w górę do całkowitej ilości opakowań
    return liczba_opakowan_potrzebna



def czy_pierwsza(*liczby):
    wynik = []
    for liczba in liczby:
        if liczba < 2:
            wynik.append(False)
        elif liczba == 2:
            wynik.append(True)
        elif liczba % 2 == 0:
            wynik.append(False)
        else:
            wynik.append(False)
    return wynik

def caesar_alphabet(data, number,alphabet=''):
    if alphabet:
        ddata = data.lower()
        new_data = "";
        for c in ddata:
            if c.isalpha():
                if c in alphabet:
                    index = alphabet.index(c)
                    if (index + number < len(alphabet)):
                        result = alphabet[index + number]
                        new_data += result
                    else:
                        result = alphabet[(index + number) - len(alphabet)]
                        new_data += result
                else:
                    new_data += c
            else:
                new_data+=c

        print(new_data)

    else:
        ddata = data.lower()
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        new_data="";
        for c in ddata:
            if c in alphabet:
                index = alphabet.index(c)
                if(index+number<len(alphabet)):
                    result = alphabet[index + number]
                    new_data+=result
                else:
                    result = alphabet[(index + number) - len(alphabet)]
                    new_data+=result
            else:
                new_data += c
    print(new_data)

#caesar_alphabet("Ala ma kotaz",1,["a","b"])
