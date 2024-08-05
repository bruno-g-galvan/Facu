Algoritmo subsidios_escuela
	total_inicial<-0
	total_primario<-0
	total_secundario<-0
	cant_inicial<-0
	cant_primario<-0
	cant_secundario<-0
	bandera=Verdadero
	
	Mientras bandera==Verdadero Hacer
		Escribir "Ingrese la edad del alumno (0 para salir)"
		Leer edad
		Si edad==0 Entonces
			Escribir "Gracias por usar nuestro sistema"
			bandera=Falso
		SiNo
			Si edad>=1 y edad<=5 Entonces
				total_inicial=total_inicial+800
				cant_inicial=cant_inicial+1
			SiNo
				Si edad>=6 y edad<=12 Entonces
					total_primario=total_primario+1200
					cant_primario=cant_primario+1
				SiNo
					Si edad>=13 y edad<=17 Entonces
						total_secundario=total_secundario+2100
						cant_secundario=cant_secundario+1
					SiNo
						Escribir "Edad no válida. Ingrese una edad entre 1 y 17"
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Mientras
	Escribir "Informe"
	Escribir "Nivel Inicial - Total: $",total_inicial," - Cantidad de Alumnos:",cant_inicial
	Escribir "Nivel Primario - Total: $",total_primario," - Cantidad de Alumnos:",cant_primario
	Escribir "Nivel Secundario o Medio - Total: $",total_secundario," - Cantidad de Alumnos:",cant_secundario
FinAlgoritmo
