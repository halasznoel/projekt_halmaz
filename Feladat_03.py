#1
halmaz = {"1","2","3"}
halmaz.remove("1")
halmaz.remove("2")
halmaz.remove("3")
print(halmaz)
#2
halmaz1 = halmaz.copy()
print(halmaz1)
#3
halmaz01 = {"1","2","3"}
halmaz02 = {"4","5","6"}

difference = halmaz01.difference(halmaz02)
print(difference)
#4
halmaz03 = {"1","2","3"}
halmaz04 = {"4","5","6"}

halmaz03.difference_update(halmaz04)
#5
halmaz05 = {"1","2","3"}
halmaz06 = {"4","5","6"}
intersection = halmaz05.intersection(halmaz06)
print(intersection)
#6
halmaz07 = {"1","2","3"}
halmaz08 = {"4","5","6"}
halmaz07.intersection_update(halmaz08)
#7
halmaz09 = {"1","2","3"}
halmaz10 = {"4","5","6"}
isdisjoint = halmaz09.isdisjoint(halmaz10)
print(isdisjoint)
#8
halmaz11 = {"a", "b", "c"}
halmaz12 = {"f", "e", "d", "c", "b", "a"}

issubset = halmaz11.issubset(halmaz12)
print(issubset)
#9
halmaz13 = {"f", "e", "d", "c", "b", "a"}
halmaz14 = {"a", "b", "c"}

issuperset = halmaz13.issuperset(halmaz14)
print(issuperset)
#10
halmaz15 = {"apple", "banana", "cherry"}
halmaz16 = {"google", "microsoft", "apple"}

sd = halmaz15.symmetric_difference(halmaz16)
print(sd)
#11

#1.
halmaz17 = {"apple", "banana", "cherry"}
halmaz18 = {"google", "microsoft", "apple"}

unio = halmaz17.union(halmaz18)
print(unio)

#2.
halmaz19 = {"apple", "banana", "cherry"}
halmaz20 = {"google", "microsoft", "apple"}

halmaz19.update(halmaz20)

print(halmaz19)

#3.
gyümölcsök = {"alma", "banán", "cseresnye"}

gyümölcsök.add("narancs")
print(gyümölcsök)