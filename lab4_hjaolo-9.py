class Person: #varje person i katalogen blir ett eget objekt, när listan söks igenom kallas de "x"
    def __init__(self, namn, nummer):
        self.namn = namn
        self.nummer = nummer
        self.alias = []
    
    def change(self, nummer): #används för att byta nummer
        self.nummer = nummer
    
    def addalias(self, alias): #lägger till ett nytt alias i aliaslistan
        self.alias.append(alias)
    
def main():
    namnlista = []
    while True:
        knapp = input("telebok> ")
        kommando = knapp.split(" ") #delar upp inputen efter blankstegen
        try:        
            if kommando[0] == "add": #kollar vad första ordet är
                add(namnlista, *kommando[1:])
        
            elif kommando[0] == "lookup":
                lookup(namnlista, *kommando[1:])
                
            elif kommando[0] == "change":
                change(namnlista, *kommando[1:])
        
            elif kommando[0] == "alias":
                alias(namnlista, *kommando[1:])
            
            elif kommando[0] == "save":
                savefile(namnlista, *kommando[1:])
        
            elif kommando[0] == "load":
                load(namnlista, *kommando[1:])

            elif kommando[0] == "remove":
                delete(namnlista, *kommando[1:])

            elif kommando[0] == "quit": 
                print("tack och godnatt")
                break

            else: #om inget av kommandona angavs säger programmet till
                print("Inte giltigt kommando")

        except TypeError: #Om fel antal argument skrivs efter ett kommando
            print("Fel antal argument")
        
def savefile(lstnamn, filnamn):
    f = open(filnamn, "w")
    for x in lstnamn:
        if x.alias != []: #sätter upp utskriften med eller utan alias
            utskrift = x.nummer + ";" + x.namn + ";" 
            for alias in x.alias: #går igenom objektets alias och lägger till dem i utskriften
                utskrift = utskrift + alias + ";"
        else: #om alias saknas skrivs bara nummer och namn in
            utskrift = x.nummer + ";" + x.namn + ";"
        f.write(utskrift+"\n") #skrivs ut följt av en ny rad
    f.close()

def add(namnlst, nynamn, nynummer):
    hittad = 0
    for x in namnlst: #kollar om numret finns
        if x.nummer == nynummer:
            hittad = 1
    if hittad == 1: #om numret finns läggs det inte till
        print("Numret finns redan")
    else: #annars kan det läggas till
        namnlst.append(Person(nynamn, nynummer)) #lägger till en ny person i listan

def load(lstnamn, filnamn):
    try:
        f = open(filnamn, "r")
        lstnamn.clear() #listan töms efter filen laddats in
        for rad in f: #går igenom varje rad i filen
            y = rad.split(";") #delar upp raden vid semikolon för att hitta namn och nummer
            lstnamn.append(Person(y[1], y[0]))
            z = 2 #z kommer användas för att hitta potentiella alias
            while y[z] != "\n": #Kollar om det finns fler namn och gör dem till alias, 
                lstnamn.append(Person(y[z], y[0]))
                z = z+1 #z blir större för att kolla nästa del av raden
        f.close()
    except FileNotFoundError: #om filen inte hittades skrivs ett meddelande ut
        print("Filen finns inte")

def delete(lstnamn, söknamn, söknummer = None):
    hittade = 0
    if söknummer == None: #om användaren inte angav ett söknummer
        for x in lstnamn: #kollar om det finns mer än ett av söknamnet
            if x.namn == söknamn or söknamn in x.alias: #kommer ihåg objektet som p
                hittade = hittade+1
                p = x
        if hittade == 1: #om bara ett namn hittades kommer p att vara personen med det namnet
            lstnamn.remove(p) #objektet p tas bort från listan, det är fortfarande personen med det önskade namnet
        elif hittade == 0:
            print("namnet finns inte")
        elif hittade > 1:
            print("Det finns flera nummer med det namnet")
    else: #om specifikt nummer angivits används en kortare version av förra koden
        for x in lstnamn:
            if (x.namn == söknamn and x.nummer == söknummer) or (söknamn in x.alias and x.nummer == söknummer):
                lstnamn.remove(x) #tar bort objektet x från listan om allt stämmer
                hittade = hittade + 1
        if hittade == 0:
            print("Det namnet finns inte")
            
def lookup(namnlst, söknamn = None):
    if söknamn == None:
        print("Du glömde skriva ett namn") #om användaren inte skrev ett namn
    else: 
        hittade = 0
        for x in namnlst:
            if x.namn == söknamn or söknamn in x.alias: #kollar om namnet stämmer
                print("nummer:", x.nummer)
                hittade = hittade+1
        if hittade < 1: #Om inga namn hittades
            print("Det namnet finns inte")

def change(namnlst, söknamn, newnumber, söknummer = None):
    hittade = 0 #hur många namn som hittats i listan
    tagetnummer = False #när den är "true" är numret upptaget
    if söknummer == None: #om inget nummer angivits
        for x in namnlst: #kollar hur många gånger namnet förekommer och om numret är taget
            if x.namn == söknamn or söknamn in x.alias:
                hittade = hittade + 1
                p = x
            if newnumber == x.nummer: #kollar alltid om numret är taget
                tagetnummer = True
        if hittade == 1 and tagetnummer == False: #kollar så att namnet bara förekommer en gång
            p.change(newnumber) #p är objektet med det namnet och kan anropas direkt
        elif hittade < 1:
            print("Det namnet finns inte")
        elif hittade > 1: #annars behövs ett nummer också
            print("Det finns fler nummer med det namnet")
        elif tagetnummer == True:
            print("Numret finns redan")
    else: #Nu har användaren sökt efter ett nummer också
        for x in namnlst:
            if x.nummer == newnumber: #kollar så att numret inte är taget
                tagetnummer = True
        if tagetnummer == True:
            print("Numret finns redan")
        else:
            for x in namnlst: #letar upp personen och anropar change-metoden
                if x.namn == söknamn and x.nummer == söknummer:
                    x.change(newnumber)
                    hittade = 1
                elif söknamn in x.alias and x.nummer == söknummer:
                    x.change(newnumber)
                    hittade = 1
            if hittade < 1:
                print("Det namnet finns inte")

def alias(namnlst, söknamn, newname, söknummer = None):
    hittade = 0 #för att räkna hur många namn som är likadana
    if söknummer == None:
        for x in namnlst:
            if x.namn == söknamn or söknamn in x.alias:
                hittade = hittade + 1 
                p = x #objektet får tllfälliga namnet p, p används bara om namnet förekommer en gång 
        if hittade == 1: #om endast en person hittades anropas addalias-metoden
            p.addalias(newname)
        elif hittade < 1:
            print("Det namnet finns inte")
        elif hittade > 1:
            print("Det finns fler nummer med det namnet")
    else: #En kortare version av koden ovan körs då användaren angivit ett söknummer också
        for x in namnlst:
            if x.namn == söknamn and x.nummer == söknummer: #om söknamnet och söknumret stämmer
                x.addalias(newname) #addalias-metoden anropas för objektet
                hittade = hittade + 1
            elif söknamn in x.alias and x.nummer == söknummer: #om sökaliaset och söknumret stämmer
                x.addalias(newname)
                hittade = hittade + 1
        if hittade == 0: #om inget hittades säger programmet till
            print("Det namnet finns inte")

main()