
wr = open('halmazok.txt','w')
'''
Halmaz (set):
- rendezetlen (elemeknek nincs indexe)
- egy elem csak egyszer szerepelhet
- többféle típust tárolhat egyszerre is
- a halmaz eleme maga nem változtatható meg
'''
wr.write(f"Halmaz (set):\n"
"- rendezetlen (elemeknek nincs indexe)\n"
"- egy elem csak egyszer szerepelhet\n"
"- többféle típust tárolhat egyszerre is\n"
"- a halmaz eleme maga nem változtatható meg\n")
wr.write(f"reggeli = {'víz', 'tea', 'vaj', 'pirítós'}\n")

reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
wr.write(f"ebed = {'víz', 'halászlé', 'kenyér'}\n")
ebed = {'víz', 'halászlé', 'kenyér'}

wr.write(f"# halmaz létrehozása\n"
"reggeli = {'tea', 'vaj', 'piritós'}\n")

# halmaz létrehozása
reggeli = {'tea', 'vaj', 'piritós'}

wr.write(f"# üres halmaz létrehozása\n"
"ebed = {}  <- SZÓTÁRT hoz létre!!!\n"
"ebed = set()\n")

# üres halmaz létrehozása
# ebed = {}  <- SZÓTÁRT hoz létre!!!
ebed = set()

wr.write(f"# bejárható gyűjteményből, pl. listából\n"
"ebed = set(['halászlé', 'kenyér', True])\n")

# bejárható gyűjteményből, pl. listából
ebed = set(['halászlé', 'kenyér', True])  

wr.write(f"# egy elem hozzáadása\n"
"reggeli.add('lekvár')\n")

# egy elem hozzáadása
reggeli.add('lekvár')

wr.write(f"# egy nem meghatározott elem eltávolítása\n"
"reggeli.pop()\n")

# egy nem meghatározott elem eltávolítása
reggeli.pop()

wr.write(f"# egy bizonyos elem eltávolítása\n"
"# ha nincs ilyen elem, akkor hibát eredményez\n"
"reggeli.remove('sajt')\n")

# egy bizonyos elem eltávolítása
# ha nincs ilyen elem, akkor hibát eredményez
reggeli.remove('sajt')

wr.write(f"# egy bizonyos elem eltávolítása\n"
"# ha nincs ilyen elem, nem eredményez hibát\n"
"reggeli.discard('sajt')\n")
# egy bizonyos elem eltávolítása
# ha nincs ilyen elem, nem eredményez hibát
reggeli.discard('sajt')

wr.write(f"# metszet\n"
"print(reggeli & ebed)\n")
# metszet
print(reggeli & ebed)

wr.write(f"# unio\n"
"print(reggeli | ebed)\n")
# unio
print(reggeli | ebed)

wr.write(f"# különbség\n"
"print(reggeli - ebed)\n")
# különbség
print(reggeli - ebed)

wr.write(f"# csak az egyikben, vagy csak a másikban\n"
"print(reggeli ^ ebed)")
# csak az egyikben, vagy csak a másikban
print(reggeli ^ ebed)

wr.write(f"# üres szótár létrehozása"
"raktar = {}"
"print(raktar)"
"# szótár létrehozása adatokkal"
"diak = {"
"      'vezeteknev': 'Kiss',"
"      'keresztnev': 'Péter',"
"      'eletkor': 17,"
"      'menza': True"
"}")
# üres szótár létrehozása
raktar = {}
print(raktar)
# szótár létrehozása adatokkal 
diak = {
      'vezeteknev': 'Kiss',
      'keresztnev': 'Péter',
      'eletkor': 17,
      'menza': True
}


wr.close()