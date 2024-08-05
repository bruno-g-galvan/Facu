Algoritmo multiplo
	Escribir "Ingrese un número entre 2 y 9 que será tomado como múltiplo";
	Leer nummultiplo;
	
	Mientras nummultiplo<2 y nummultiplo>9 Hacer
		Escribir "Numero fuera de rango. Por favor, ingrese un número entre 2 y 9";
		Escribir "Ingrese un número entre 2 y 9";
		Leer nummultiplo;
	Fin Mientras
	
	multiplo_mayor<-nummultiplo;
	multiplo_menor<-999999;
	cantidad_multiplos <- 0;	
	bandera<-Verdadero;
	
	Mientras bandera Hacer
		Escribir "Ingrese un número entero positivo (o -1 para terminar)";
		Leer numerito;
		Si numerito==-1 Entonces
			bandera<-Falso;
		SiNo
			Si numerito%nummultiplo==0 Entonces
				Escribir numerito," es multiplo de ", nummultiplo;
				cantidad_multiplos<-cantidad_multiplos+1;
				Si numerito>multiplo_mayor Entonces
					multiplo_mayor<-numerito;
				FinSi
				Si numerito==None o numerito<multiplo_menor Entonces
					multiplo_menor<-numerito;
				FinSi
			Fin Si
		Fin Si
	FinMientras
	
	Si cantidad_multiplos>0 Entonces
		
		Escribir "Cantidad total de números ingresados que son multiplos de" ,nummultiplo, ":",cantidad_multiplos;
		Escribir "El multiplo mayor ingresado es:", multiplo_mayor;
		
    Fin Si
	Si multiplo_menor<>999999 Entonces
		Escribir "El multiplo menor ingresado es :", multiplo_menor;
	FinSi
FinAlgoritmo
