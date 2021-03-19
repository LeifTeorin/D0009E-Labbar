def meny1():
    #definierar listorna
    ord = []
    beskrivning = []
    
    #Börjar en loop för menyn så att den kommer tillbaka efter et kommando
    while True:
        #skriver ut menyn
        print("""
        1. Lägg till ord
        2. Slå upp ett ord
        3. Stäng av""")
        #variabeln knapp definieras som det användaren skriver in
        knapp = input("Vad skall göras idag? ")
        
        if knapp == "1": #kollar om användaren angav 1
            ord, beskrivning = nyttordmeny1(ord, beskrivning)
        
        elif knapp=="2": #Kollar om användaren angav 2
            letameny1(ord, beskrivning)
        
        elif knapp=="3": #kollar om användaren angav 3
            print("Hejdå")
            break #avbryter loopen och menyn
        #om ingen av dessa hände har användaren skrivit något annat och då säger programmet till
        else:
            print("Inte ett alternativ")

def nyttordmeny1(ordlista, besklista):
    nyttord = input("Vilket ord vill du lägga till?")
    if nyttord not in ordlista: #kollar om ordet användaren angav redan finns i programmet
        #Lägger till ordet och beskrivningen sist i listorna
        ordlista.append(nyttord)
        nybeskrivning = input("Beskriv ordet")
        besklista.append(nybeskrivning)
        return ordlista, besklista
    else:
        print("Det där ordet finns redan.")
        return ordlista, besklista

def letameny1(ordlista, besklista):
    sökord = input("Vilket ord söker du?")
    if sökord in ordlista: #kollar om ordet användaren sökte finns i listan med ord
        #letar upp ordets position och läser av beskrivningen på motsvarande position
        position= ordlista.index(sökord)
        print(ordlista[position])
        print(besklista[position])
    else:
        print("Det där ordet finns inte")

def meny2():
    lista = {} #definierar ordlistan

    while True:
        print("""
        1. Lägg till ord
        2. Slå upp ett ord
        3. Stäng av""")
        knapp = input("Vad skall göras idag? ")

        if knapp == "1":
            lista = nyttordmeny2(lista)

        elif knapp == "2":
            letameny2(lista)
                
        elif knapp == "3":
            print("Tack och godnatt")
            break 
        
        else:
            print("Så funkar det inte")

def nyttordmeny2(listan):
    nyttord = input("Vilket ord vill du lägga till? ")
    if nyttord not in listan: #kollar om ordet redan finns
        beskrivning = input("Beskriv ordet ")
        listan[nyttord] = beskrivning #skapar en ny nyckel med värdet 'beskrivning'
        return listan
    else:
        print("Det där ordet finns redan")
        return listan

def letameny2(listan):
    sökord = input("Vilket ord söker du? ")
    if sökord in listan: #kollar om sökordet finns som nyckel
        #skriver ut ordet och dess värde (beskrivningen)
        print(sökord, "Beskrivning:", listan[sökord])
    else:
        print("Det ordet finns inte")

def meny3():
    ordlista=[] #definierar första listan

    while True:
        print("""
        1. Lägg till ord
        2. Slå upp ett ord
        3. Stäng av""")
        knapp = input("Vad skall göras idag? ")

        if knapp == "1":
            ordlista = nyttordmeny3(ordlista)
            
        elif knapp == "2":
            letameny3(ordlista)

        elif knapp == "3":
            print("Tack och godnatt")
            break
        
        else:
            print("Det där är inget alternativ")

def nyttordmeny3(listan):
    nyttord=input("Lägg till ett ord ")
    if len(listan) != 0: #Kollar om listan är tom annars läggs ett ord till direkt
        for y in listan: #Går igenom listan och letar efter det nya ordet
            if y[0]== nyttord:
                print("Ordet finns redan") #Om det nya ordet redan finns säger programmet till
                break
        if y[0] != nyttord: #Om programmet har gått igenom listan och inte hittar ordet kan det läggas till
            beskrivning = input("Beskriv ordet ")
            nytuppel = (nyttord, beskrivning) #Definierar en tuppel med ord och beskrivning
            listan.append(nytuppel) #Lägger till tuppeln i slutet av listan
        return listan
    else: #Om listan är tom kan ett ord läggas till då det garanterat inte finns redan
        beskrivning = input("Beskriv ordet ")
        nytuppel = (nyttord, beskrivning)
        listan.append(nytuppel)
        return listan

def letameny3(listan):
    sökord = input("Vilket ord söker du?")
    if len(listan) != 0:
        for x in listan:
            if x[0] == sökord:
                print(x[1])
                break
        if x[0] != sökord:
            print("ordet finns ej")
    else:
        print("Listan är tom :(")


