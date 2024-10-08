### Programm Einheiten Umrechner
#	Rechnet imperiale Einheiten in metrische Einheiten um und umgekehrt
#	Author: Kriger, Scheele

#Zeit Bibliothek importieren für Wartezeit implementieren
import time

#Variablen festlegen
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

#Festlegen der Umrechnungsfaktoren für die Umrechnung der Einheiten
fkt_mi_km = 1.60934
fkt_in_cm = 2.54
fkt_lb_kg = 0.453592
fkt_gal_l = 3.78541


#Ausgabe Hauptmenü
#Wiederhole Schleife solange wahl_menu nicht x ist
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
    
#------------------------------------------------------------------------
#Umrechner Imperial zu Metrisch Untermenü
#------------------------------------------------------------------------
    
    # Wenn Hauptmenü Auswahl weder 1 noch 2, beende das Programm
    if(wahl_menu!="1" and wahl_menu!="2"):
        print("Ende")
        print("-------"*9)
        break
    # Wenn Hauptmenü Auswahl 1 ist, gebe Untermenü Imperial zu Metrisch aus
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
        
        #Benutzereingabe in String, um Fehler auszuschließen
        wahl_einheit=str(input("Ihre Wahl: "))
        
        # Eingabe der Imperialen Daten
        # Wenn Eingabe nicht die Werte in der String-Liste hat, gebe Fehler aus
        if(wahl_einheit not in ("1","2","3","4","5")):
            print("Falsche Eingabe!")
            break
        else:
            print("-------"*9)
            # Falls in der try Abfolge ein Fehler auftritt (zb bei eingabe von Strings in einen float Wert, gebe Fehler aus, sonst setze Variablen
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

            
            print("-------"*9) 
            print("Berechnung wird durchgeführt . . .")
            print("-------"*9)
            
            # Berechnung der Daten mit den jeweiligen Umrechnungsfaktoren
            # bei Umrechnung von imperial in metrisch werden die Faktoren multipliziert
            if(wahl_einheit =="1"):
                cm_num = in_num * fkt_in_cm
            elif(wahl_einheit == "2"):
                km_num = mi_num * fkt_mi_km
            elif(wahl_einheit == "3"):
                kg_num = lb_num * fkt_lb_kg
            elif(wahl_einheit == "4"):
                l_num = gal_num * fkt_gal_l
            elif(wahl_einheit == "5"):
                c_num = (f_num - 32) * 5 / 9
            
            #Ausgabe Metrischen Daten
            if(wahl_einheit =="1"):
                print("Dein Ergebnis lautet: ",cm_num,"cm")
                print("-------"*9)
            elif(wahl_einheit == "2"):
                print("Dein Ergebnis lautet: ",km_num, "km")
                print("-------"*9)
            elif(wahl_einheit == "3"):
                print("Dein Ergebnis lautet: ",kg_num, "kg")
                print("-------"*9)
            elif(wahl_einheit == "4"):
                print("Dein Ergebnis lautet: ",l_num, "l")
                print("-------"*9)
            elif(wahl_einheit == "5"):
                print("Dein Ergebnis lautet: ",c_num, "°C")
                print("-------"*9)
            # Warte 3 Sekunden für Übersichtlichkeit
            time.sleep(3)
            
                
#------------------------------------------------------------------------                      
#Umrechner Metritsch zu Imperial
#------------------------------------------------------------------------
                
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

        #Eingabe der metrischen Daten
        #Benutzereingabe in String, um Fehler auszuschließen
        wahl_einheit=str(input("Ihre Wahl: "))
        
        # Wenn Eingabe nicht die Werte in der String-Liste hat, gebe Fehler aus
        if(wahl_einheit not in ("1","2","3","4","5")):
            print("Falsche Eingabe!")
            break
        else:
            print("-------"*9)
            # Falls in der try Abfolge ein Fehler auftritt (zb bei eingabe von Strings in einen float Wert, gebe Fehler aus, sonst setze Variablen
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
            
            print("-------"*9) 
            print("Berechnung wird durchgeführt . . .")
            print("-------"*9)
            
            # Berechnung der Daten mit den jeweiligen Umrechnungsfaktoren
            # bei Umrechnung von metrisch in imperial werden die Daten mit dem Umrechnungsfaktor dividiert
            if(wahl_einheit =="1"):
                in_num = cm_num / fkt_in_cm
            elif(wahl_einheit == "2"):
                mi_num = km_num / fkt_mi_km
            elif(wahl_einheit == "3"):
                lb_num = kg_num / fkt_lb_kg
            elif(wahl_einheit == "4"):
                gal_num = l_num / fkt_gal_l
            elif(wahl_einheit == "5"):
                f_num = c_num * 1.8 + 32

            #Ausgabe der imperialen Daten

            if(wahl_einheit =="1"):
                print("Dein Ergebnis lautet: ",in_num,"inch")
                print("-------"*9)
            elif(wahl_einheit == "2"):
                print("Dein Ergebnis lautet: ",mi_num, "mi")
                print("-------"*9)
            elif(wahl_einheit == "3"):
                print("Dein Ergebnis lautet: ",lb_num, "lb")
                print("-------"*9)
            elif(wahl_einheit == "4"):
                print("Dein Ergebnis lautet: ",gal_num, "gal")
                print("-------"*9)
            elif(wahl_einheit == "5"):
                print("Dein Ergebnis lautet: ",f_num, "°F")
                print("-------"*9)
            # Warte 3 Sekunden für die Übersichtlichkeit
            time.sleep(3)
                
    else:
        #Falls irgendwelche Fehler auftreten, die nicht aufgefangen werden, gebe Fehlermeldung aus
        print("Falsche Eingaben wurden getätigt")