Algoritmo calcularChocotorta
	Escribir "Ingrese la cantidad de galletitas de choclota en kilos";
	Leer galletitas_kg;
	Escribir "Ingrese la cantidad de dulce de leche en kilos";
	Leer dulce_de_leche_kg;
	Escribir "Ingrese la cantidad de queso crema en kilos";
	Leer queso_crema_kg;
	
	
	galletitas_gramos<- galletitas_kg*1000;
	dulce_de_leche_gramos<-dulce_de_leche_kg*1000;
	queso_crema_gramos<-queso_crema_kg*1000;
	
	chocotortas_posibles <- 0;
	
	Mientras galletitas_gramos>=500 y dulce_de_leche_gramos>=400 y queso_crema_gramos>=180 Hacer
		chocotortas_posibles<- chocotortas_posibles+1;
		galletitas_gramos<-galletitas_gramos-500;
		dulce_de_leche_gramos<-dulce_de_leche_gramos-400;
		queso_crema_gramos<-queso_crema_gramos-180;
	Fin Mientras

	
	Escribir "Se pueden preparar ", chocotortas_posibles, " chocotortas.";
	Escribir "Sobran ", galletitas_gramos, " gramos de galletitas de chocolate.";
	Escribir "Sobran ", dulce_de_leche_gramos, " gramos de dulce de leche.";
	Escribir "Sobran ", queso_crema_gramos, " gramos de queso crema.";

	
FinAlgoritmo
