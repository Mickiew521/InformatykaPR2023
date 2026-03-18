import sys
from collections import Counter
from pickletools import TAKEN_FROM_ARGUMENT4

# programy są w kolejności alfabetycznej wobec zadań

def iloczyn(x,y,i=1):

    if y == 1:
        print(f"Wywołanie[{i}]: x = {x}, y = {y}, wynik = {x}")
        return x
    else:
        k = y//2
        z = iloczyn(x,k,i+1)

        wynik = 0
        dodawanie = 0
        if y%2 == 0:
            wynik += z + z
            dodawanie += 1
        else:
            wynik += x + z + z
            dodawanie +=2
        print(f"Wywołanie[{i}]: x = {x}, y = {11}, k = {k}, z = {z}, wynik = {wynik}, dodawanie = {dodawanie}")
        return wynik

'''
    z = 0
    dopuki y>0 wykonuj:
        jeżeli y mod 2 = 1:
            z+= x
        x +=x
        y = y div 2
'''

S = 'mascarpone'

Sufiksy = []

for k,letter in enumerate(S,start=1):
        Sufiksy.append(S.removeprefix(S[:k-1]))

Sufiksy = sorted(Sufiksy)


Słownik = {}

for i in range(1,len(Sufiksy)+1):
    Słownik[i] = (Sufiksy[i-1])

#print(Słownik)

def czy_mniejszy(n,s,k1,k2):
    i = k1 -1
    j = k2 -1
    while i<n and j<n:
        if s[i] == s[j]:
            #print(f"porównanie == {s[j]}")
            i+=1
            j+=1
        elif s[i] < s[j]:
            #print(f"porównanie {s[i]} < {s[j]}")
            return True

        else:
            #print(f"porównanie {s[i]} > {s[j]}")
            return False
    if j<n:
        return True
    else:
        return False

with open("DANE/DANE_M/slowa1.txt",'r',encoding='utf-8') as file:
    dane = file.read()
    slowo = []
    slowo = dane.split()

slowo[0] = int(slowo[0])
slowo[2] = int(slowo[2])
slowo[3] = int(slowo[3])
#print(czy_mniejszy(slowo[0],slowo[1],slowo[2],slowo[3]))



def sortowanie(s):
    n = len(s)
    T = list(range(1,n+1))

    for i in range(n-1):
        for j in range(i+1,n):
            if czy_mniejszy(n,s,T[j],T[i]):
                T[i],T[j] = T[j],T[i]

    return T

#print(sortowanie(input('Podaj wyraz: ')))

def najmnijeszy_sufiks():
    with open("DANE/DANE_M/slowa4.txt",'r',encoding='utf-8') as f:
        read = f.read()
        slowa = read.split()
        for i,slowo in enumerate(slowa):
            if i%2 == 1:
                s = slowa[i]
                T = sortowanie(s)
                a = T[0]
                print(s[a-1:],end="\n")


#najmnijeszy_sufiks()

def binarne():
    with open("DANE/DANE_M/anagram.txt",'r',encoding='utf-8') as f:
        read = f.read()
        liczby = read.split()
        zrow = 0
        pzrow = 0
        for liczba in liczby:
            jedynki = 0
            zera = 0
            for cyfra in liczba:
                cyfra = int(cyfra)
                if cyfra == 1:
                    jedynki+=1
                elif cyfra == 0:
                    zera+=1
                else:
                    print('jakims cudem to nie 0 ani 1')

            if jedynki == zera:
                zrow+=1
            elif abs(jedynki-zera)== 1:
                pzrow+=1

        return zrow, pzrow




#print(binarne())

def silnia(n):
    wynik = 1
    for i in range(1,n+1):
        wynik*=i
    return wynik

def permutacja(num):


    jeden = 0
    zero = 0

    for l in num:
        l = int(l)
        if l == 1:
            jeden+=1
        else:
            zero+=1

    dlugosc = len(num)

    wynik = silnia(dlugosc-1)/(silnia(jeden-1)*silnia(zero))
    return int(wynik)


def anagramy():
    with open("DANE/DANE_M/anagram.txt",'r',encoding='utf-8') as f:
        LIP = []
        Liczby = []
        for line in f:
            line = line.strip()
            if len(line) == 8:
                Liczby.append(line)
        for liczba in Liczby:
            LIP.append((liczba,permutacja(liczba)))

        for element in LIP:
            if element[1] == max(LIP, key=lambda x: x[1])[1]:
                print(element[0])

        return LIP

#print(anagramy())

def bezwzgledna():
    with open("DANE/DANE_M/anagram.txt",'r',encoding='utf-8') as f:
        read = f.read()
        liczby = read.split()
        Bezl = []
        for i,liczba in enumerate(liczby[0:len(liczby)-1:]):
            liczba = int(liczba,2)
            liczba2 = int(liczby[i+1],2)
            wynik = abs(liczba - liczba2)
            Bezl.append(wynik)

        max_wart = max(Bezl)

        return bin(max_wart)[2:]


#print(bezwzgledna())

def zamiana():
    with open("DANE/DANE_M/przyklad.txt",'r',encoding='utf-8') as f:
        read = f.read()
        liczby = read.split()
        liczba_bez_zera = 0

        for liczba in liczby:
            zerocounter = 0
            liczba = int(liczba,2)
            if '0' not in str(liczba):
                liczba_bez_zera+=1

        Sumy = []

        for libc in liczby:
            libc2 = set(str(int(libc,2)))
            libc = int(libc,2)
            suma = 0
            for cyfra in libc2:
                cyfra = int(cyfra)
                suma += cyfra

            Sumy.append((libc,suma))

        for k, e in Sumy:
            if e == max(Sumy, key=lambda x: x[1])[1]:
                break







        return liczba_bez_zera, k

#print(zamiana())

def na3(n):
    wynik = ""
    while n>0:
        wynik = str(n % 3) + wynik
        n //= 3
    return wynik

def na9(n):
    wynik = ""
    while n>0:
        wynik = str(n % 9) + wynik
        n //= 9
    return wynik


#print(na9(int('101201',3)))
#print(na3(int('2487',9)))











