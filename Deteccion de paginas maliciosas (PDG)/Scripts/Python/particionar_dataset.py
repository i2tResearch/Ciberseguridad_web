import random


def subset(cantidad, ruta):
	with open(ruta, mode='w') as subconjunto:
		lines = open('dataset_benigno.txt').read().splitlines()
		for indice in xrange(1,cantidad):
			myline = random.choice(lines)
			subconjunto.writelines(myline + '\n')
			print myline

ruta = 'subdataset.txt'
subset(30000,ruta)