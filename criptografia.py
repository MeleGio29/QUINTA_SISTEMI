import string
import random

LUNGHEZZAALFABETO = 22

def chiaveRandom(listaChiaviDizionario):
    chiave = ""
    length_of_string = int(input("Inserisci la lunghezza della stringa: "))
    chiave = ''.join([random.choice(listaChiaviDizionario) for _ in range(length_of_string)])
    print (chiave)
    return chiave

def invertiDizionario(dizionario):
    dizionarioInvertito = {v: k for k, v in dizionario.items()}

    return dizionarioInvertito

def codificaCriptografia(dizionario, parola, chiave):
    parolaCriptografata = ""

    dizionarioInvertito = invertiDizionario(dizionario)

    for i in range(len(parola)):
        n = ((dizionario[parola[i]] + dizionario[chiave[i]]) % LUNGHEZZAALFABETO)
        parolaCriptografata = parolaCriptografata + dizionarioInvertito[n]

    return parolaCriptografata

def decodificaCriptografia(dizionario, parola, chiave):
    parolaNonCriptografata = ""

    dizionarioInvertito = invertiDizionario(dizionario)

    for i in range(len(parola)):
        n = ((dizionario[parola[i]] - dizionario[chiave[i]]) % LUNGHEZZAALFABETO)
        parolaNonCriptografata = parolaNonCriptografata + dizionarioInvertito[n]

    return parolaNonCriptografata

def inserisciParola():
    s = input("Vuoi codificare o decodificare? ")
    ok = True

    if(s == "codificare"):
        parola = input("Inserisci una parola da codificare: ")
        ok = True
    else:
        parola = input("Inserisci una parola da decodificare: ")
        ok = False

    return parola, ok

def main():
    dizionario = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'l':9,
    'm':10, 'n':11, 'o':12, 'p':13, 'q':14, 'r':15, 's':16, 't':17, 'u':18, 'v':19, 'z':20, ' ':21}

    listaChiaviDizionario = []

    for k in dizionario:
        listaChiaviDizionario.append(k)

    risp = input("Chiave predefinita o randomica?")

    if risp == "predefinita":
        chiave = "itisdelpozzo"
    else:
        chiave = chiaveRandom(listaChiaviDizionario)

    parola, ok = inserisciParola()

    if len(parola) > len(chiave):
        parola, ok = inserisciParola()

    if ok == True:
        parolaCriptografata = codificaCriptografia(dizionario, parola, chiave)
        print(parolaCriptografata)
    else:
        parolaNonCriptografata = decodificaCriptografia(dizionario, parola, chiave)
        print(parolaNonCriptografata)

if __name__ == "__main__":
    main()