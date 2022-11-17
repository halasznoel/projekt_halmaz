wr = open("Feladat_03.txt","w")
wr.write('halmaz = {"1","2","3"}\n')
wr.write('halmaz.remove("1")\n'
'halmaz.remove("2")\n'
'halmaz.remove("3")\n'
'print(halmaz)\n')
wr.write("\n")

#1
halmaz = {"1","2","3"}
halmaz.remove("1")
halmaz.remove("2")
halmaz.remove("3")
print(halmaz)

wr.write('halmaz1 = halmaz.copy()\n'
'print(halmaz1)\n')
wr.write("\n")

#2
halmaz1 = halmaz.copy()
print(halmaz1)

wr.write('halmaz01 = {"1","2","3"}\n'
'halmaz02 = {"4","5","6"}\n'
'difference = halmaz01.difference(halmaz02)\n'
'print(difference)\n')
wr.write("\n")

#3
halmaz01 = {"1","2","3"}
halmaz02 = {"4","5","6"}

difference = halmaz01.difference(halmaz02)
print(difference)

wr.write('halmaz03 = {"1","2","3"}\n'
'halmaz04 = {"4","5","6"}\n'
'halmaz03.difference_update(halmaz04)\n')
wr.write('\n')

#4
halmaz03 = {"1","2","3"}
halmaz04 = {"4","5","6"}

halmaz03.difference_update(halmaz04)

wr.write('halmaz05 = {"1","2","3"}\n'
'halmaz06 = {"4","5","6"}\n'
'intersection = halmaz05.intersection(halmaz06)\n'
'print(intersection)\n')
wr.write('\n')

#5
halmaz05 = {"1","2","3"}
halmaz06 = {"4","5","6"}
intersection = halmaz05.intersection(halmaz06)
print(intersection)

wr.write('halmaz07 = {"1","2","3"}\n'
'halmaz08 = {"4","5","6"}\n'
'halmaz07.intersection_update(halmaz08)\n')
wr.write('\n')

#6
halmaz07 = {"1","2","3"}
halmaz08 = {"4","5","6"}
halmaz07.intersection_update(halmaz08)

wr.write('halmaz09 = {"1","2","3"}\n'
'halmaz10 = {"4","5","6"}\n'
'isdisjoint = halmaz09.isdisjoint(halmaz10)\n'
'print(isdisjoint)\n')
wr.write('\n')

#7
halmaz09 = {"1","2","3"}
halmaz10 = {"4","5","6"}
isdisjoint = halmaz09.isdisjoint(halmaz10)
print(isdisjoint)

wr.write('halmaz11 = {"a", "b", "c"}\n'
'halmaz12 = {"f", "e", "d", "c", "b", "a"}\n'
'issubset = halmaz11.issubset(halmaz12)\n'
'print(issubset)\n')
wr.write('\n')

#8
halmaz11 = {"a", "b", "c"}
halmaz12 = {"f", "e", "d", "c", "b", "a"}

issubset = halmaz11.issubset(halmaz12)
print(issubset)

wr.write('halmaz13 = {"f", "e", "d", "c", "b", "a"}\n'
'halmaz14 = {"a", "b", "c"}\n'
'issuperset = halmaz13.issuperset(halmaz14)\n'
'print(issuperset)\n')
wr.write('\n')

#9
halmaz13 = {"f", "e", "d", "c", "b", "a"}
halmaz14 = {"a", "b", "c"}

issuperset = halmaz13.issuperset(halmaz14)
print(issuperset)

wr.write('halmaz15 = {"apple", "banana", "cherry"}\n'
'halmaz16 = {"google", "microsoft", "apple"}\n'
'sd = halmaz15.symmetric_difference(halmaz16)\n'
'print(sd)\n')
wr.write('\n')

#10
halmaz15 = {"apple", "banana", "cherry"}
halmaz16 = {"google", "microsoft", "apple"}

sd = halmaz15.symmetric_difference(halmaz16)
print(sd)

wr.write('#11\n')
wr.write('#1.\n'
'halmaz17 = {"apple", "banana", "cherry"}\n'
'halmaz18 = {"google", "microsoft", "apple"}\n'
'unio = halmaz17.union(halmaz18)\n'
'print(unio)\n'
'#2.\n'
'halmaz19 = {"apple", "banana", "cherry"}\n'
'halmaz20 = {"google", "microsoft", "apple"}\n'
'halmaz19.update(halmaz20)\n'
'print(halmaz19)\n'
'#3.\n'
'gyümölcsök = {"alma", "banán", "cseresnye"}\n'
'gyümölcsök.add("narancs")\n'
'print(gyümölcsök)\n')
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

wr.close()