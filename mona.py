# Gruppeinnlevering 2 Mona - sin løsning

# Forteller hvor mange ganger Erling velger A

antall_a = 0

# ------ Introduksjon ------ 

print("Erling er prosjektleder for et tverrfaglig team.")
print("Teamet er i stormingfasen og mellom ett par i teamet har det begynt å oppstå konflikter.")

# ------ Beslutningspunkt 1: Konflikt mellom Elias og Silje ------

print("Silje og Elias er uenige om teknologivalg og design, og dette har gått fra en sakskonflikt til en personkonflikt.")
print("A: Erling tar individuelle samtaler med dem")
print("B: Erling tar det opp i felleskap med hele teamet")

valg1 = input("Hva velger Erling? (A/B): ")

if valg1 == "A":
    print("Etter samtalene finner Erling en kompromissløsning som begge parter kan akseptere, og teamet fortsetter å jobbe sammen.")
    antall_a = antall_a +1

elif valg1 == "B":
    print("Dette fører til at konflikten eskalerer, og teamet blir mer splittet. Erling må nå bruke mer tid på å megle mellom Silje og Elias.")

else: 
    print("Skriv inn A eller B")

# ------ Beslutningspunkt 2: Konflikt mellom Hamdi og Hallgeir

print("Hamdi og Hallgeir har en konflikt om brukerportalens funksjonalitet og prioriteringer.")
print("Konflikten er fremdeles lavmælt")
print("A: Erling venter å se om de klarer å løse konflikten selv")
print("B: Erling griper inn selv")

valg2 = input("Hva velger Erling? (A/B): ")

if valg2 == "A": 
    print("Hamdi og Hallgeir prater sammen, og kommer frem til en løsning som passer for dem begge")
    print("Konflikten er løst")
    antall_a = antall_a +1

elif valg2 == "B":
    print("Erling griper inn, å har en samtale med dem begge")
    print("Konflikten eskalerer, da de ikke føler tillit fra Erling til å prøve å løse konflikten selv")

else:
    print("Skriv inn A eller B")


# ------ Beslutningspunkt 3: Motivasjon og stemningen i teamet

print("Det er to uker til protoypen skal være klar")
print("Erling merker motivasjonen i teamet synker og folk har lite engasjement")
print("A: Erling finner tid til teambuilding")
print("B: Det blir ingen teambulding")

valg3 = input("Hva velger Erling (A/B): ")

if valg3 == "A":
    print("Teambuldingen fører til at stemingen og motivasjonen i teamet blir bedre")
    antall_a = antall_a +1

elif valg3 == "B": 
    print("Motivasjonen og stemingen i teamet fortsetter å være dårlig")

else:
    print("Skriv inn A eller B")


# ------ Avslutning: Tre utfall: 3 A - Problem løst, 1-2 A - Delvis løst, 0 A - Ikke løst

print("Utfall av beslutningene") 

if antall_a == 3: 
    print("Problem løst, teamet jobber bra sammen og prototypen blir levert i tide")

elif antall_a >= 1:
    print("Delvis løst, stemingen i teamet er ikke veldig bra, men prototypen er levert i tide")

elif antall_a == 0:
    print("Ikke løst, det er ingen samarbeid i teamet, og konfliktene for store")
    print("Prototypen blir ikke levert i tide") 

