
import time
from datetime import datetime
import sys
class KULUTUKSET:
    Aika=None
    Kulutus=float(0)
    KulutusPaiva=float(0)
    KulutusYo=float(0)   
    
# class RIVIT:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    # KulutusMaara=float(0)
    # Kulutuskeski=int(0)
    # MatalinKulutus=0
    # KorkeinKulutus=0
    # MatalaAika=None
    # KorkeaAika=None

   
def tiedosto(Valinta):
    if Valinta ==1:
        Luettava_tiedosto=input("Anna luettavan tiedoston nimi: ")     

    elif Valinta ==3 or 4:
        Luettava_tiedosto=input("Anna kirjoitettavan tiedoston nimi: ")
         
    return Luettava_tiedosto
    
def kysyjalue(Tiedot, Luettava_tiedosto):
    try:
        Tiedosto=open(Luettava_tiedosto, "r", encoding="utf-8")
        Rivi = Tiedosto.readline()
        Tiedot.clear()
        Askel=0
        for Rivi in Tiedosto:
            Tieto = KULUTUKSET()
            Sarakkeet = Rivi.strip().split(";")
            Tieto.Aika = Sarakkeet[0]
            Tieto.KulutusYo=float(Sarakkeet[1])
            Tieto.KulutusPaiva=float(Sarakkeet[2])
            Tieto.Kulutus=Tieto.KulutusPaiva+Tieto.KulutusYo
            Tiedot.append(Tieto)
            Askel +=1
        Tiedosto.close()
        print("Tiedostosta '"+Luettava_tiedosto+"' lisättiin listaan", Askel, "datariviä.")  
    except OSError:
        print("Tiedoston '", Luettava_tiedosto, "' käsittelyssä virhe, lopetetaan.", end="", sep="")
        sys.exit()
    return Tiedot
    
def lueJaAnalysoi(Tiedot,Kuukausikustannukset):
    # Rivi= RIVIT()
    EdellinenKuukausi = None
    KuukausikulutusPaiva = float(0)
    KuukausikulutusYo = float(0)
    KuukausienMaara=1

    for Tieto in Tiedot:
        
        Aika = time.strptime(Tieto.Aika, "%d-%m-%Y %H:%M")
        AikaKuukausi = Aika.tm_mon
        
        if AikaKuukausi != EdellinenKuukausi and EdellinenKuukausi is not None:
            Kuukausikustannukset.append((EdellinenKuukausi, KuukausikulutusPaiva, KuukausikulutusYo))
            KuukausikulutusPaiva = 0.0
            KuukausikulutusYo = 0.0
            KuukausienMaara += 1

        KuukausikulutusPaiva += Tieto.KulutusPaiva
        KuukausikulutusYo += Tieto.KulutusYo
        EdellinenKuukausi = AikaKuukausi
    
    Kuukausikustannukset.append((EdellinenKuukausi, KuukausikulutusPaiva, KuukausikulutusYo))
  
    print("Kuukausittaiset summat laskettu", KuukausienMaara ,"kuukaudelle.")
    return Kuukausikustannukset
    

    
def luejaAnalysoi2(Tiedot,Paivakustannukset):  
    ViikonpaivaKulutukset = [0.0] * 7
            
    for Tieto in Tiedot:
        Aika = time.strptime(Tieto.Aika, "%d-%m-%Y %H:%M")
        AikaPaiva = Aika.tm_wday  
        ViikonpaivaKulutukset[AikaPaiva] += Tieto.Kulutus

    Paivakustannukset = [(i, ViikonpaivaKulutukset[i]) for i in range(7)]
             
    return Paivakustannukset

    
def tallenna(Luettava_tiedosto, Paivakustannukset,Kuukausikustannukset):
    try:
        Tiedosto = open(Luettava_tiedosto, "w", encoding="utf-8")
        
        if Kuukausikustannukset:
            Tiedosto.write("Kuukausittaiset kulutukset (MWh):\n")
            Tiedosto.write("Kuukausi;Yö;Päivä;Yhteensä\n")
            for EdellinenKuukausi, KuukausikulutusPaiva, KuukausikulutusYo in Kuukausikustannukset:
                Tiedosto.write(datetime(1900, EdellinenKuukausi, 1).strftime("%b")
                + ";" 
                + str(round(KuukausikulutusYo/1000,1)) +";"
                + str(round(KuukausikulutusPaiva/1000,1)) +";" 
                + str(round((KuukausikulutusYo+KuukausikulutusPaiva)/1000,1)) + "\n")
            Tiedosto.write("\n")
                
        if Paivakustannukset:
            Tiedosto.write("Viikonpäivä;Kulutus (MWh)\n")
            for Paiva, Kulutus in Paivakustannukset:
                Tiedosto.write(["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"][Paiva] + ";" + str(round(Kulutus/1000,1))+ "\n")
                
        print("Tiedosto '"+Luettava_tiedosto+"' kirjoitettu.") 
        Tiedosto.close()
    except OSError:
        print("Tiedoston '", Luettava_tiedosto, "' käsittelyssä virhe, lopetetaan.", end="", sep="")
        sys.exit()
    return None