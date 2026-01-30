
import HTPerusKirjasto

def valikko(): 
    while True:
        print("Valitse haluamasi toiminto:")
        print("1) Lue tiedosto")
        print("2) Analysoi")
        print("3) Kirjoita tiedosto")
        print("4) Analysoi viikonpäivittäiset tulokset")
        print("0) Lopeta")
        
        Valinta = int(input("Anna valintasi: "))
        if Valinta in [0, 1, 2, 3, 4]:
            return Valinta
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()

    return None        
def paaohjelma():
    Valinta=None
    Tiedot=[]
    Rivi=[]
    Luettava_tiedosto=None
    Analyysitehty=None
    Paivakustannukset=[]
    Kuukausikustannukset=[] 
    while Valinta != 0:
        Valinta=valikko()
        if (Valinta==1):
            Luettava_tiedosto=HTPerusKirjasto.tiedosto(Valinta)
            Tiedot=HTPerusKirjasto.kysyjalue(Tiedot, Luettava_tiedosto)
                  
        elif (Valinta==2):
            if len(Tiedot) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                Paivakustannukset.clear()
                Kuukausikustannukset.clear()
                Kuukausikustannukset=HTPerusKirjasto.lueJaAnalysoi(Tiedot, Kuukausikustannukset)
                Analyysitehty=1
                  
        elif (Valinta==3):
            if Analyysitehty !=1 :
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
            else:    
                Luettava_tiedosto=HTPerusKirjasto.tiedosto(Valinta)
                HTPerusKirjasto.tallenna(Luettava_tiedosto, Paivakustannukset, Kuukausikustannukset)
                
        elif (Valinta==4):
            if len(Tiedot) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                Paivakustannukset.clear()
                Kuukausikustannukset.clear()                
                Paivakustannukset=HTPerusKirjasto.luejaAnalysoi2(Tiedot, Paivakustannukset)              
                Luettava_tiedosto=HTPerusKirjasto.tiedosto(Valinta)
                HTPerusKirjasto.tallenna(Luettava_tiedosto, Paivakustannukset)
        elif (Valinta ==0):
            print("Lopetetaan.")
        print()
    Tiedot.clear()
    Paivakustannukset.clear()
    Kuukausikustannukset.clear()
    # Rivi.clear()
    print("Kiitos ohjelman käytöstä.")

    return None

paaohjelma()

