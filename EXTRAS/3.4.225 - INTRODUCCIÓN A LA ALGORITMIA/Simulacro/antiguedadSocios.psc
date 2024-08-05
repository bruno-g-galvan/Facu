Algoritmo antiguedadSocios
	bandera<-Verdadero;
	categoria1<-0;
	antcat1<-0;
	categoria2<-0;
	antcat2<-0;
	categoria3<-0;
	antcat3<-0;
	totSocios<-0;
	Mientras bandera Hacer
		Escribir "Ingrese la antiguedad desde cuando es socio";
		Leer antiguedad;
		Si antiguedad==-1 Entonces
			bandera=Falso;
		SiNo
			Si antiguedad<0 Entonces
				Escribir "Antiguedad inválida";
			SiNo
				Si antiguedad>=1 y antiguedad<=12 Entonces
					categoria1<-categoria1+1;
					totSocios<-totSocios+1;
					antcat1<-antcat1+antiguedad;
				SiNo
					Si antiguedad>=13 y antiguedad<=26 Entonces
						categoria2<-categoria2+1;
						totSocios<-totSocios+1;
						antcat2<-antcat2+antiguedad;						
					SiNo
						Si antiguedad>26 Entonces
							categoria3<-categoria3+1;
							totSocios<-totSocios+1;
							antcat3<-antcat3+antiguedad;
						Fin Si
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Mientras
	
	Si totSocios>0 Entonces
		Escribir "La cantidad de total socios es:",totSocios;
		Escribir "La cantidad de socios de la categoria 1 es:", categoria1;
		Escribir "La cantidad de socios de la categoria 2 es:", categoria2;
		Escribir "La cantidad de socios de la categoria 3 es:", categoria3;
	SiNo
		Escribir "No ingreso datos";
	Fin Si
	
	Si categoria1>0
		Escribir "El promedio de las edades de los socios correspondientes a categoria 1 es ",(antcat1/categoria1);
	FinSi
	
	Si categoria2>0
		Escribir "El promedio de las edades de los socios correspondientes a categoria 2 es ",(antcat2/categoria2);
	FinSi
	
	
	Si categoria3>0
		Escribir "El promedio de las edades de los socios correspondientes a categoria 3 es ",(antcat3/categoria3);
	FinSi

FinAlgoritmo
