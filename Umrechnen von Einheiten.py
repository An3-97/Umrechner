### Programmschnipsel GUI
#   Author: Kriger
#   Hier wird die Menüführung aufgebaut
wahl_menu=0
wahl_einheit=0
mi_num=0
km_num=0
in_num=0
cm_num=0
lb_num=0
kg_num=0
gal_num=0
l_num=0
f_num=0
c_num=0

while(wahl_menu!="x"):
    print("-------"*9)
    print("Umrechner von Einheiten - Imperial zu Metrisch und umgekehrt")
    print("Hauptmenü (Wählen Sie Ihr Untermenü)")
    print("-------"*9)
    print("1 - Umrechnung von Imperial zu Metrisch")
    print("2 - Umrechnung von Metrisch zu Imperial")
    print("x - Umrechner beenden")
    print("-------"*9)
    wahl_menu=str(input("Ihre Wahl: "))
    print("-------"*9)
    
    if(wahl_menu!="1" and wahl_menu!="2"):
        break
    elif(wahl_menu=="1"):
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
        
        wahl_einheit=str(input("Ihre Wahl: "))
        
        if(wahl_einheit not in ("1","2","3","4","5")):
            print("Falsche Eingabe!")
            break
        else:
            print("-------"*9)
            try:
                if(wahl_einheit == "1"):
                    in_num=float(input("Geben Sie Ihren umzurechnenden Wert ein: "))
                elif(wahl_einheit == "2"):
                    mi_num=float(input("Geben Sie Ihren umzurechnenden Wert ein: "))
                elif(wahl_einheit == "3"):
                    lb_num=float(input("Geben Sie Ihren umzurechnenden Wert ein: "))
                elif(wahl_einheit == "4"):
                    gal_num=float(input("Geben Sie Ihren umzurechnenden Wert ein: "))
                elif(wahl_einheit == "5"):
                    f_num=float(input("Geben Sie Ihren umzurechnenden Wert ein: "))
            except:
                print("Es wurde eine fehlerhafte Eingabe durchgeführt!")
        
    elif(wahl_menu=="2"):
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
        
        wahl_einheit=str(input("Ihre Wahl: "))
        
        if(wahl_einheit not in ("1","2","3","4","5")):
            print("Falsche Eingabe!")
            break
        else:
            print("-------"*9)
            try:
                if(wahl_einheit == "1"):
                    cm_num=float(input("Geben Sie Ihren umzurechnenden Wert ein: "))
                elif(wahl_einheit == "2"):
                    km_num=float(input("Geben Sie Ihren umzurechnenden Wert ein: "))
                elif(wahl_einheit == "3"):
                    kg_num=float(input("Geben Sie Ihren umzurechnenden Wert ein: "))
                elif(wahl_einheit == "4"):
                    l_num=float(input("Geben Sie Ihren umzurechnenden Wert ein: "))
                elif(wahl_einheit == "5"):
                    c_num=float(input("Geben Sie Ihren umzurechnenden Wert ein: "))
            except:
                print("Es wurde eine fehlerhafte Eingabe durchgeführt!")            
    else:
        print("Falsche Eingaben wurden getätigt")
        
    print("-------"*9) 
    print("Berechnung wird durchgeführt . . .")
    print("-------"*9)
    