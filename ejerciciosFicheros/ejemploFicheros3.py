f = open('ficheros/aeropuertos.dat', 'a')
canary_iata = ('VLC','CDT','ORL')
for linea in canary_iata:
   f.write(linea+'\n')
f.close()
