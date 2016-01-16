import math
# Primer estudi, veien si es \sum_i=0^n = n(n-1)/2
def funciona ():
	e ()
def fun1 ( x ):
	print ( x * ( x -1  ) /2 )
	print ( x * ( x + 1 ) /2 )

def fun2 ( x ):
	print ("+", (-1 + math.sqrt ( 1 + 4 * x ) ) /2)
	print ("-", (-1 - math.sqrt ( 1 + 4 * x ) ) /2)

def a ():
	for i in range ( 20 ):
		print ( i, "+", math.ceil ( ( -1 + math.sqrt ( 1 + 4 * i ) ) /2 ) )

def important ( x ): return math.ceil ( ( -1 + math.sqrt ( 1 + 4 * x ) ) /2 )
def NaturalToNaturalNatural ( x ):
	t = important ( x )
	if t:
		q = x%t
	else:
		q = 0
	return ( t, q, t-q)

def b ():
	for i in range ( 10 ):
		print ( i, NaturalToNaturalNatural ( i ) )

def first ( x ): return math.ceil ( ( -1 + math.sqrt ( 1 + 4 * x ) ) / 2 )
def second ( x ): return x *( x + 1 ) / 2
def vectorNtoNN ( x ):
	t = first ( x )
	s = second ( t )
	return (x, t, s, ( x - s, t - x + s ))

def c ():
	for i in range ( 20 ):
		print ( vectorNtoNN ( i ) )

# sembla ser que m'he equivocat amb el first, alguna cosa no vol funcionar
def first01 ( x ):
	if x:
		lola = ( -1 + math.sqrt ( 1 + 8 * x ) ) / 2
		return lola
		loly = math.ceil ( lola )
		if ( lola == loly ):
			return loly +1
		return loly
	return 0
def d ():
	for i in range ( 20 ):
		print ( i, first01 ( i ) )

def ntoNN ( x ):
	f = math.floor ( ( -1 + math.sqrt ( 1 + 8 * x ) ) / 2 )
	s = int ( f * ( f + 1 ) / 2 )
	#return ( x,q, f, s, x - s, f - x + s )
	return ( x - s, f - x + s )

def e ():
	for i in range ( 20 ):
		print ( ntoNN ( i ), i )

def nto2n ( x ):
	return ( x - math.floor ( ( -1 + math.sqrt ( 1 + 8 * x ) ) / 2 ) * (math.floor ( ( -1 + math.sqrt ( 1 + 8 * x ) ) / 2 ) +1)/2, math.floor ( ( -1 + math.sqrt ( 1 + 8 * x ) ) / 2 ) +math.floor ( ( -1 + math.sqrt ( 1 + 8 * x ) ) / 2 ) * (math.floor ( ( -1 + math.sqrt ( 1 + 8 * x ) ) / 2 ) +1)/2 - math.floor ( ( -1 + math.sqrt ( 1 + 8 * x ) ) / 2 ) )
def f ():
	for i in range ( 20 ):
		print ( nto2n ( i ), i )
