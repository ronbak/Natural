import math
# Reciclant codi anterior :◁)
def funciona ():
	print ("Funciona el nnton i el ton, son el mateix pero amb la entrada different")
def ntonn ( x ):
	f = math.floor ( ( -1 + math.sqrt ( 1 + 8 * x ) ) / 2 )
	s = int ( f * ( f + 1 ) / 2 )
	return ( x - s, f - x + s )
#☺☻

def nnton ( x ):
	f = x[0] + x[1]
	return int (x[0] + f * ( f + 1 ) / 2)
def ton ( x0, x1 ):
	f = x0 + x1
	return int (x0 + f * ( f + 1 ) / 2)

def a ():
	for i in range ( 20 ):
		print ( i, nnton ( ntonn ( i ) ) )

def b ():
	for i in range ( 20 ):
		print ( ton (i,i) )
