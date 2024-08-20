### Programmschnipsel GUI
#   Author: Kriger
#   Hier wird die Menüführung aufgebaut

wahl_menu=0
wahl_einheit=0

while(wahl_menu!="x"):
    print("-------"*9)
    print("Umrechner von Einheiten - Imperial zu Metrisch und umgekehrt")
    print("Hauptmenü (Wählen Sie Ihr Untermenü)")
    print("-------"*9)
    print("1 - Umrechnung von Imperial zu Metrisch")
    print("2 - Umrechnung von Metrisch zu Imperial")
    print("x - Umrechner beenden")
    print("-------"*9)
    wahl_menu=input("Ihre Wahl: ")
    print("-------"*9)
    
    if(int(wahl_menu)!=1 and int(wahl_menu)!=2):
        break
    elif(int(wahl_menu)==1):
        print("Umrechner Imperial zu Metrisch")
        print("-------"*9)
        print("Wählen Sie Ihre umzurechnende Einheit:")
        print("-------"*9)
        print("1 - Inches (in) zu Zentimeter (cm)")
        print("2 - Miles (mi) zu Kilometer (km)")
        print("3 - Pounds (lbs) zu Kilogramm (kg)")
        print("4 - Gallonen (gal) zu Liter (l)")
        print("5 - Fahrenheit (°F) zu Celsius (°C)")
        print("-------"*9)
        
        
    elif(int(wahl_menu)==2):
        print("Umrechner Metrisch zu Imperial")
        print("-------"*9)
        print("Wählen Sie Ihre umzurechnende Einheit:")
        print("-------"*9)
        print("1 - Zentimeter (cm) zu Inches (in)")
        print("2 - Kilometer (km) zu Miles (mi)")
        print("3 - Kilogramm (kg) zu Pounds (lbs)")
        print("4 - Liter (l) zu Gallonen (gal)")
        print("5 - Celsius (°C) zu Fahrenheit (°F)")
        print("-------"*9)

    else:
        print("Falsche Eingaben wurden getätigt")
        
    print("TEST")