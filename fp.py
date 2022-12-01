import math
import struct
import bitstring
import numpy as np

def unpack_float(f):
	"""
	Prende un float in input e ritorna 
	segno, mantissa ed esponente in formato stringa binaria
	"""
	f_b = bitstring.BitArray(float=f, length=32)
	s = f_b.bin[0:1]
	e = f_b.bin[1:9]
	m = f_b.bin[9:32]
	return s,e,m

def repack_float(s,e,m):
	"""
	Prende in input mantissa ed esponente in formato stringa binaria
	Ritorna il float corrispondente unendo segno, esponente e mantissa
	"""
	f_s = s + e + m
	return stru

def bin_to_float(f_s):
	"""
	Prende in input un float in formato stringa binaria
	Ritorna il numero in formato float
	"""
	return struct.unpack('!f',struct.pack('!I', int(f_s, 2)))[0]

def float_analytical_count(begin, end):
	"""
	Prende in input un intervallo (float o int)
	Ritorna il numero teorico di float compresi in tale intervallo utilizzando una formula empirica
	NOTA1: funziona con estremi dell'intervallo positivi
	"""
	return float_binary_to_int(end) - float_binary_to_int(begin)
	#return 8388608 * math.log(float(end)/float(begin), 2)

def float_bruteforce_count(begin, end, step, verbose=0):
	"""
	Prende in input un intervallo (float o int)
	Ritorna il numero esatto di float compresi in tale intervallo
	NOTA: funziona con estremi dell'intervallo positivi
	"""
	i = 0
	curr = begin
	while (curr < end):
		s,e,m = unpack_float(curr)
		f_s = s + e + m
		
		if (verbose):
			print(s,e,m,":", curr)

		#dimezza lo step se l'incremento supera la fine dell'intervallo
		while (bin_to_float(add_binary_string(f_s,step,32)) > end) & (int(step) > 1):
			step = math.ceil(step/2)
			if (verbose):
				print("New step:", step)

		f_s = add_binary_string(f_s,step,32)

		curr = bin_to_float(f_s)
		
		i += step
	return i

def add_binary_string(s,i,l):
	"""
	Prende in input una stringa binaria, un incremento, e il numero di bit totali 
	Ritorna la stringa binaria incrementata della quantità desiderata
	"""
	n = int(s,2)
	n += i
	s_incr = format(n,'0'+str(l)+'b')
	return s_incr

def float_binary_to_int(f):
	"""
	Prende in input float 
	Ritorna gli stessi 32 bit del float trattati come int
	"""
	s,e,m = unpack_float(f)
	f_b = s + e + m
	n = int(f_b,2)
	return n

if __name__ == "__main__":
	min_range = 0.0
	max_range = 1.0

	print(float_bruteforce_count(min_range, max_range, 100000000, verbose=1))
	print(round(float_analytical_count(min_range, max_range)))


