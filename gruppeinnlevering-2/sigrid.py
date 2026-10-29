# Sigrid sin løsning på gruppeinnlevering 2
# Innledning
print("\n")
print("Det er tre uker til protoypen skal være klar")
print("tiden er knapp og det oppstår to konflikter i teamet.")
print("Den første konflikten er mellom Silje og Elias")
print("der uenighet om teknologivalg og design har gått fra en")
print("sakskonflikt til en personkonflikt.")
print("Den andre konflikten er mellom Hamdi og Hallgeir")
print("hvor en lavmælt diskusjon om brukerportalens funksjonalitet")
print("og prioriteringer har oppstått.")
print("De neste valgene er avgjørende for prosjektet.")
print("\n")

# Besluttningspunkt 1: Konflikt mellom Silje og Elias

print("Den første konflikten mellom Silje og Elias hvor ")
print("diskusjonen blir stadig mer emosjonell og personlig")
print("hvordan vil du håndtere konflikten?")
print("Du får to valg:")
print("Valg 1: Konflikten blir løst individuelt")
print("Valg 2: Konflikten blir tatt opp med resten av teamet")
print("\n")

runde1 = input("Hva velger du? 1 eller 2: ")

if runde1 == "1":
    print("Silje og Elias får snakket ut om konflikten og finner en felles løsning")
elif runde1 == "2":
    print("Forholdet mellom Silje og Elias blir verre og det går utover tidsrammen")
    print("for prosjektet. Du må bruke mer tid på å megle mellom Silje og Elias.")
else:
    print("Du ga et ugyldig svar, vennligst skriv 1 eller 2")
print("\n")    
while runde1 not in ["1", "2"]:
    
    runde1 = input("Hva velger du? 1 eller 2: ")

# Besluttningspunkt 2: Konflikt mellom Hamdi og Hallgeir

print("Samtidig oppstår det en lavmælt diskusjon mellom Hamdi og Hallgeir hvor trykket øker") 

print("Du får to valg:")
print("Valg 1: Du velger å ikke gripe inn")
print("valg 2: Du vurderer risikoen og velger å gripe inn")
print("\n")
runde2 = input("Hva velger du? 1 eller 2: ")

if runde2 == "1":
    print("Hamdi og Hallgeir kommer til enighet etter noen dager og relasjonen mellom dem blir styrket")
elif runde2 == "2":
    print("Hamdi og Hallgeir ble fornærmet og snakker mindre når du er tilstede.")
    print("De så ikke diskusjonen som en konflikt og vil ikke at det skal gjentas.")
else:
    print("Du ga et ugyldig svar, vennligst skriv 1 eller 2")
while runde2 not in ["1", "2"]:
    
    runde2 = input("Hva velger du? 1 eller 2: ")

# Besluttningspunkt 3: Motivasjon og stemningen i teamet

print("For å bevare motivasjonen og styrke relasjonene i teamet,")
print("må ta en avgjørelse om å prioritere teambuilding eller prosjektet")  
print("\n")
print("Du får to valg:")
print("Valg 1: Avsetter tid til teambuilding")
print("Valg 2: Prioriterer fremdrift og leveranse av prosjektet")  
print("\n")
runde3 = input("Hva velger du? 1 eller 2: ")

if runde3 == "1":
    print("Verdifull tid gikk tapt, men teamet har fått sterkere relasjoner,")
    print("de jobber mer effektivt sammen og stolheten i teamet øker.")
elif runde3 == "2":
    print("Teamet leverer en fullstendig prototype, men relasjonene i teamet er svekket og samarbeid blir vanskeligere fremover")
else:
    print("Du ga et ugyldig svar, vennligst skriv 1 eller 2")
print("\n")    
while runde3 not in ["1", "2"]:
    
    runde3 = input("Hva velger du? 1 eller 2: ")

# Avslutning:

if runde1 == "1" and runde2 == "1" and runde3 == "1" or runde1 == "1" and runde2 == "1" and runde3 == "2":
    print("Godt jobbet! Du har håndtert konfliktene på en god måte og teamet har levert en prototype i tide.")
    print("De samarbeider godt og har et godt forhold til hverandre, og gleder seg til å jobbe videre sammen.")
elif runde1 == "1" and runde2 == "2" and runde3 == "1" or runde1 == "2" and runde2 == "1" and runde3 == "1" or runde1 == "1" and runde2 == "2" and runde3 == "2" or runde1 == "2" and runde2 == "1" and runde3 == "2":
    print("Du har håndtert konfliktene på en delvis god måte, men teamet har levert en prototype i tide.")
elif runde1 == "2" and runde2 == "2" and runde3 == "1" or runde1 == "2" and runde2 == "2" and runde3 == "2":
    print("Du har håndtert konfliktene på en dårlig måte, og teamet har ikke levert en prototype i tide.")  
    print("Teamet har ikke et godt forhold til hverandre, og samarbeidet er vanskelig fremover.")  

