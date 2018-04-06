import time

print("""Ärkasid metsas. On väga pime ja sa ei saa aru
kuidas sa siia sattusid. Sul pole peale telefoni mitte midagi kaasas.
Telefonil on aku tühi. Sa ei tea teed metsast välja, sest mets on võõras.
Valik on selline: Kas lähed otse (sisesta "o"), vasakule (sisesta "v")
või paremale (sisesta "p"? """)
otsus = input()
if otsus == "p":
    print("Sa läksid paremale!")
    time.sleep(2)
    print("Sa märkad üht helendavat olendit hauda kaevamas.")
    time.sleep(1)
    print("""Kas sa kõnetad teda ("k") või mitte ("m")? Võibolla ehk toksid teda? (t)""")
    kõnetus = input()
    if kõnetus == "k":
        print("Sa küsid, et kas tal on abi vaja.")
        time.sleep(3)
        print(""" "Jah on küll", vastas olend.""")
        time.sleep(2)
        print("Sa võtad ka labida kätte ning kaevad temaga koos haua lõpuni.")
        time.sleep(2)
        print("""Olend tänab sind haua kaevamise eest.
Ta ütles, et see haud on ebaviisakatele, aga kuna sa ei olnud
ebaviisakas, siis ta andis selle eest sulle preemia. Rikkus
nii pea kui üles ärkad.""")
        lõpp = "õnnelik"
    elif kõnetus == "m":
        print("""Sa ei kõneta teda ning paned jooksu.
Korra taha vaadates märkad, et ta jookseb sulle järgi.
Ta ütles, et seda hauda ta kaevaski sinusugusele tropile,
kes teisi hädas ei aita.""")
        time.sleep(6)
        print("""Sa jäid liiga aeglaseks ning ta tappis su ära!
Hiljem lükkas ta su hauda ning viskas labidaga mulla peale.""")
        lõpp = "õnnetu"
    elif kõnetus == "t":
        time.sleep(1)
        print("""Teda toksima minnes komistate ja kukute hauda""")
        lõpp = "õnnetu"

        
if otsus == "v":
    print("Sa sammud julgelt vasakule")
    time.sleep(2)
    print("Märkasid metslooma. Ta jooksis su juurde ning hammustas sind!")
    lõpp = "õnnetu"
    
if otsus == "o":
    time.sleep(1)
    print("""Märkad üht tumedat meest, kes
ajab sulle hirmu nahka, kas põgened ("p") või mitte ("m")?""")
    põgenemine = input()
    if põgenemine == "p":
        print("Sa hakkasid põgenema!")
        time.sleep(2)
        print("""Ebaõnn! Joostes sattusid sa nii palju
paanikasse, et sa ei pannud tähelegi, et otse lõksu astusid!""")
        lõpp = "õnnetu"
    elif põgenemine == "m":
        print("Sa otsustasid seisma jääda!")
        time.sleep(2)
        print("""Mees läheneb sulle ja küsib,
et kas te olete ehitaja John.
Sisesta "j", et vastata jaatavalt
ja "e", et vastata eitavalt.""")
        vastus = input()
        if vastus == "j":
            time.sleep(1)
            print("Mees juhatab sind vana katkise maja juurde. Hiljem kaob ta ära.")
            time.sleep(2)
            print("""Mida sa otsustad teha?, kas avad maja ukse ("a")
või vaatad maja taha ("v")?""")
            tegevus = input()
            if tegevus == "v":
                time.sleep(1)
                print("""Maja taga näed sa keldri sissepääsu.
Sellele lähenedes lükkab tundmatu jõud sind pikali.""")
                lõpp = "õnnetu"
            elif tegevus == "a":
                print("Sa avasid maja ukse")
                time.sleep(1)
                print("Ebaõnn! Ust avades kukkusid sulle tööriistad pähe!")
                lõpp = "õnnetu"
        elif vastus == "e":
            print("""Mees sammub veelgi lähemale hirm on
niivõrd suur, et te ei saa ennast liigutadagi.""")
            time.sleep(5)
            print("MEES SÕI SU ÄRA!!")
            lõpp = "õnnetu"

            
time.sleep(2)
if lõpp == "õnnetu":
    print("Te ärkate üles ja taipate, et see oli hoopis üks hirmus unenägu.")
elif lõpp == "õnnelik":
    print("""Te ärkasite üles. Hiljem avastate, et olete miljonär!""")
input()
