# IS-118 Gruppeoppgave 2 - Gruppeløsning

print("--- Prosjektleder-simulatoren ---")
print("Erling leder et team som har havnet rett i stormingfasen.")
print("Målet er å bygge opp tilliten i gruppa før prototypen skal leveres.\n")

tillit = 0

# --- SITUASJON 1 ---
print("[1] Konflikten mellom Silje og Elias")
print("De krangler om teknologivalg, og det har blitt personlig.")
print("A: Ta individuelle samtaler med dem for å roe ned situasjonen.")
print("B: Ta det opp i plenum med hele teamet for å få alt på bordet.")

valg1 = ""
while valg1 not in ["a", "b"]:
    valg1 = input("Hva bør Erling gjøre? (A/B): ").lower()
    
    if valg1 == "a":
        print("-> Erling tar en prat med dem hver for seg. Det funker, og konflikten roer seg ned.\n")
        tillit += 1
    elif valg1 == "b":
        print("-> Dårlig idé. Diskusjonen sporer helt av i plenum, og teamet blir delt i to leire.\n")
    else:
        print("Ugyldig valg. Skriv A eller B.")

# --- SITUASJON 2 ---
print("[2] Spenningen mellom Hamdi og Hallgeir")
print("Det ulmer en uenighet om hvordan folkemøtene skal fungere.")
print("A: Gripe inn tidlig og kalle inn til et møte for å rydde opp.")
print("B: Vente og se om de fikser det selv.")

valg2 = ""
while valg2 not in ["a", "b"]:
    valg2 = input("Hva bør Erling gjøre? (A/B): ").lower()
    
    if valg2 == "a":
        print("-> Erling tar tak i det tidlig. De finner et kompromiss, og stemningen bedrer seg.\n")
        tillit += 1
    elif valg2 == "b":
        print("-> Erling lar det ligge. Frustrasjonen bare bygger seg opp i bakgrunnen.\n")
    else:
        print("Ugyldig valg. Skriv A eller B.")

# --- SITUASJON 3 ---
print("[3] Motivasjonskrisen i teamet")
print("Prototypen skal snart leveres, men teamet er utslitt og mangler motivasjon.")
print("A: Sette av tid til relasjonsbygging og sosiale aktiviteter.")
print("B: Pushe på for å holde tidsfristen og fokusere kun på oppgavene.")

valg3 = ""
while valg3 not in ["a", "b"]:
    valg3 = input("Hva bør Erling gjøre? (A/B): ").lower()
    
    if valg3 == "a":
        print("-> Teamet får et pusterom. Folk blir bedre kjent, og tilliten kommer tilbake.\n")
        tillit += 1
    elif valg3 == "b":
        print("-> Teamet jobber på spreng, men det sosiale samarbeidet er iskaldt.\n")
    else:
        print("Ugyldig valg. Skriv A eller B.")

# --- RESULTAT ---
print("=== SLUTTRESULTAT ===")
if tillit == 3:
    print("Utfall 1: Godt samarbeid (Kombinasjon AAA)")
    print("Teamet når normingfasen. Prototypen leveres i tide med høy kvalitet og god stemning!")
elif tillit == 1 or tillit == 2:
    print("Utfall 2: Delvis løst")
    print("Dere kom i mål med prototypen, men det er fortsatt mye gnisninger i teamet.")
    print("Teamet vil svinge mellom storming og norming fremover.")
else:
    print("Utfall 3: Samarbeidet svikter (Game Over)")
    print("Tilliten er på null, teamet motarbeider hverandre, og prosjektet kræsjer helt.")
