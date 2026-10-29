# Del 2: Interaktiv Historie 
# Erling og den digitale innbyggerportalen 

print("Erling og den digitale innbyggerportalen")
print()
print("Erling er prosjektsleder for den digitale innbyggerportalen i kommunen.")
print("etter seks uker oppstår det konflikter i prosjektgruppen")
print("Han må ta tre viktige beslutninger for å få prosjektet tilbake på sporet.")
print()
poeng = 0

# Valg 1: konflikten mellom Silje og Elias
print("valg 1:  hva bør Erling gjøre?")
print("1. snakke med Silje og Elias hver for seg")
print("2. ta opp konflikten i et felles møte")
valg1 = input("Hva gjør Erling? skrive 1 eller 2:  ") 

while valg1 not in ("1", "2"):
    valg1 = input("ugyldig valg. velg 1 eller 2: ")

# Konsekvenser av valg 1 
if valg1 == "1":
    print()
    print("Erling snakker med Silje og Elias hver for seg.")
    print("Begge får forklare sitt syn.")
    print("konflikten roer seg, og samarbeidet blir bedre.")
    poeng = poeng + 1 

else:
    print()
    print("Erling tar opp konflikten i et felles møte.")
    print("Diskusjonen blir anspent.")
    print("konflikten er fortsatt ikke løst")

# Valg 2: Uenighet mellom Hamdi og Hallgeir
print()
print("valg 2: Hva bør Erling gjøre med uenigheten?")
print("1. gripe inn tidlig og kalle inn til et møte")
print("2. vente å se om det løser seg")

valg2 = input("hva gjør Erling? skrive 1 eller 2: ")

while valg2 not in ("1", "2"):
    valg2 = input("ugyldig valg. velg inn 1 eller 2:")

# Konsekvenser av valg 2
if valg2 == "1":
    print()
    print("Erling kaller Hamdi og Hallgeir inn til et møte.")
    print("De lytter til hverandre og diskuterer løsninger.")
    print("teamet blir enige om hvordan møtene skal foregå")
    poeng = poeng + 1

else: 
    print()
    print("Erling venter og ser om uenigheten løser seg. ")
    print("Hamdi og Hallgeir fortsetter å være uenige.")
    print("samarbeidet blir vanskligere.")
 

# Valg 3: Motivasjonen i teamet
print()
print("valg 3: Hva skal Erling prioritere?")
print("1. bygge relasjoner")
print("2. fokusere på oppgaven og fristen")


valg3 = input("hva gjør Erling? skrive 1 eller 2:")

while valg3 not in ("1", "2"):
    valg3 = input("ugyldig valg. velg  1 eller 2:")

# Konsekvenser av valg 3 
if valg3 == "1": 
    print() 
    print("Erling prioriterer å bygge relasjoner i teamet.")
    print("medlemmene får bedre tillit til  hverandre")
    print("motivasjonen og samarbeidet blir bedre.")
    poeng = poeng + 1 

else: 
    print()
    print("Erling foksurer på oppgavene og fristen.")
    print("teamet får jobbet videre med prosjektet")
    print("men samarbeidet kan bli svakere.")


# Avslutning: 
print()
print("Veien videre")
print("du fikk ", poeng, "av 3 poeng.")
print()

if poeng == 3:
    print("god avslutning!")
    print("teamet bygger tillit og samarbeider godt.")
    print("Erling får gruppen på rett spor, og prosjektet går videre.")

elif poeng >= 1:
    print("delvis god avslutning.")
    print("noen konflikter er fortsatt utløst")
    print("teamet må fortsette å jobbe med kommunikasjon og samarbeid")

else:
    print("dårlig avslutning")
    print("konfliktene fortsetter, og teamet mister motivasjonen.")
    print("prosjektet risikerer å bli forsinket")
