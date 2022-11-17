
wr = open("halmazokhazi.txt","w")
wr.write(f"reggeli = {'vaj', 'tea', 'pirítós'}\n")
reggeli = {'vaj', 'tea', 'pirítós'}
wr.write("ebed = {} \n")
ebed = {}
wr.write(f"ebed = set(['halászlé', 'kenyér', True])\n")
ebed = set(['halászlé', 'kenyér', True])
wr.write(f"print(type(ebed))\n")
print(type(ebed))
wr.write(f"print(ebed)\n")
print(ebed)

wr.write(f"reggeli.add('víz')\n")
reggeli.add('víz')
wr.write(f"#reggeli.remove('körte')\n")
#reggeli.remove('körte')
wr.write(f"reggeli.discard('körte')\n")
reggeli.discard('körte')
wr.write(f"print(reggeli)\n")
print(reggeli)
wr.write(f"ebed = {'víz', 'halászlé','kenyér'}\n")
ebed = {'víz', 'halászlé','kenyér'}
wr.write(f"print(reggeli & ebed\n")
wr.write(f"print(reggeli | ebed\n")
wr.write(f"print(reggeli - ebed\n")
wr.write(f"print(reggeli ^ ebed\n")
print(reggeli & ebed)
print(reggeli | ebed)
print(reggeli - ebed)
print(reggeli ^ ebed)

wr.write(f"gyumolcskosar = ['eper', 'alma', 'szilva', 'eper']\n")
gyumolcskosar = ['eper', 'alma', 'szilva', 'eper']
wr.write(f"fajta = set()\n")
fajta = set()
wr.write(f"for gyumolcs in gyumolcskosar:\n")
for gyumolcs in gyumolcskosar:
    fajta.add(gyumolcs)
wr.write(f"fajta.add(gyumolcs)\n")
wr.write(f"print(fajta)")
print(fajta)

wr.close()