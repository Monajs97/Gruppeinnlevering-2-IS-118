#IS-118 Gruppeinnlevering 2 - Dinas Løsning 
# antall_a forteller hvor mange ganger Erling velger A. Summen bestemmer utfallet. 


antall_a = 0

print("Erling i stormingsfasen")

print("Det har gått seks uker siden Erling samlet teamet")
print("Nå er teamet i stormingfasen, og det er spenninger i teamet.")
print("Prototypen skal være klar om 3 uker.")
print()

#Konlfikt 1: Silje og Elias
print("SITUASJON 1: Silje og Elias")
print("Silje og Elias er uenige om teknologi og design. Det har gått fra saklig til personlig") 
print("A: Snakke med dem individuelt") 
print("B: Ta det opp med hele teamet") 
valg_1 = input("Hva gjør Erling? Skriv A eller B:  ")
if valg_1 == "A":
    print("Erling snakker med dem hver for seg. Konflikten roer seg.")
    antall_a = antall_a + 1 
elif valg_1 == "B": 
    print("Erling tar det opp med hele teamet. Folk begynner å ta side.")
else: 
    print("Skriv inn enten A eller B")

print()
#Konflikt 2: Hamdi og Hallgeir 
print("SITUASJON 2: Hamdi og Hallgeir")
print("Hamdi vil ha digitale folkemøter på kommunens egen plattform.") 
print("Hallgeir vil ha et åpent system der innbyggerne kan komme med spontane innspill.")
print("Uenigheten er fortsatt lavmælt, men Erling merker at frustrasjonen vokser.")
print("A: Gripe inn tidlig og kalle inn til et møte") 
print("B: Vente og se om de løser det selv") 
valg_2 = input("Hva gjør Erling? Skriv A eller B:  ")
if valg_2 == "A":
    print("På møtet oppdages Hamdi og Hallgeir en løsning som passer dem begge.")
    antall_a = antall_a + 1 
elif valg_2 == "B": 
    print("Erling venter. Det blir ingen løsning, og resten av teamet merker at stemningen blir dårligere.")
else: 
    print("Skriv inn enten A eller B")

print() 
#Konflikt 3: Motivasjonen i teamet
print("SITUASJON 3: Motivasjonen i teamet")
print("Det er to uker igjen til prototypen skal være klar. Teamet er demotivert.")
print("A: Sette av en dag til relasjonsbygging og felles lunsj")
print("B: Fortsette som før og satse på at det ordner seg")
valg_3 = input("Hva gjør Erling? Skriv A eller B:  ")
if valg_3 == "A":
    print("Teamet får en pause fra kontoret og blir bedre kjent. Tilliten i gruppen øker.")
    antall_a = antall_a + 1
elif valg_3 == "B": 
    print("Alle holder fokus på oppgaven, men stemningen er dårlig. Tilliten i teamet blir ikke bedre.")
else: 
    print("Skriv inn enten A eller B")

print()
#Avslutning: Tre utfall. 3 A = godt samarbeid, 1-2 A = delvis løst, 0 A = samarbeidet svikter 
print("UTFALL")
if antall_a == 3:
    print("GODT SAMARBEID: Teamet leverer kjempebra, og prototypen leveres i tide.")
elif antall_a >= 1: 
    print("DELVIS LØST: Prototypen blir levert i tide, men relasjonene i teamet er dårlige.")
elif antall_a == 0: 
    print("SAMARBEID SVIKTER: Teamet er splittet, og prototypen blir forsinket.")