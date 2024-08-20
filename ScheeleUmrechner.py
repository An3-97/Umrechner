mi_num
km_num
in_num
cm_num
lb_num
kg_num
gal_num
l_num
f_num
c_num
#Festlegen der Umrechnungsfaktoren
fkt_mi_km = 1.60934
fkt_in_cm = 2.54
fkt_lb_kg = 0.453592
fkt_gal_l = 3.78541
#Umrechnung Meilen und Kilometer
if km_num > 0:
    km_num = mi_num * fkt_mi_km
else:
    mi_num = km_num / fkt_mi_km
#Umrechnung Inches in Zentimeter
if cm_num > 0:
    cm_num = in_num * fkt_in_cm
else:
    in_num = cm_num / fkt_in_cm
#Umrechnung Kilogramm und Pounds
if kg_num > 0:
    kg_num = lb_num * fkt_lb_kg
else:
    lb_num = kg_num * fkt_lb_kg
#Umrechnung Liter und Gallon
if l_num > 0:
    l_num = gal_num * fkt_gal_l
else:
    gal_num = l_num / fkt_gal_l
    