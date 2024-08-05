Algoritmo triangulos
	Escribir "Ingrese la lontigud del primer lado:"
	Leer ladoA
	Escribir "Ingrese la longitud del segundo lado:"
	Leer ladoB
	Escribir "Ingrese la longitud del tercer lado"
	Leer ladoC
	
	Si ladoA<=0 o ladoB<=0 o ladoC<=0 Entonces
		Escribir "Las longitudes deben ser numeros naturales"
	SiNo
		Si ladoA+ladoB>ladoC y ladoA+ladoC>ladoB y ladoB+ladoC>ladoA Entonces
			Si ladoA==ladoB y ladoB==ladoC Entonces
				Escribir "Se forma un triangulo equilatero"
			SiNo
				Si ladoA==ladoB o ladoB==ladoC o ladoA==ladoC Entonces
					Escribir "Se forma un triangulo isosceles"
				SiNo
					Escribir "Se forma un triangulo escaleno"
				Fin Si
			Fin Si
		SiNo
			Escribir "Los segmentos no forman un triángulo"
		Fin Si
	Fin Si
FinAlgoritmo
