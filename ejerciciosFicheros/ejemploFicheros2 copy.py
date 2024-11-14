f = open('ficheros/aeropuertos.dat', 'w')
canary_iata = ('TFN', 'TFS', 'LPA', 'GMZ', 'VDE', 'SPC', 'ACE', 'FUE')
for linea in canary_iata:
   f.write(linea+'\n')
f.close()
