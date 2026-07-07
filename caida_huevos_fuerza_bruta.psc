Algoritmo CaidaHuevos_FuerzaBruta
	Definir nHuevos, nPisos, rpta, operaciones Como Entero;

	Escribir "==============================================";
	Escribir "  CAIDA DE HUEVOS - FUERZA BRUTA (recursion)";
	Escribir "==============================================";
	Escribir Sin Saltar "Ingrese la cantidad de huevos: ";
	Leer nHuevos;
	Escribir Sin Saltar "Ingrese la cantidad de pisos: ";
	Leer nPisos;

	operaciones <- 0;
	rpta <- CaidaHuevosFB(nHuevos, nPisos, operaciones);

	Escribir "----------------------------------------------";
	Escribir "Con ", nHuevos, " huevo(s) y ", nPisos, " piso(s):";
	Escribir "Minimo de lanzamientos en el peor caso = ", rpta;
	Escribir "Cantidad de operaciones                = ", operaciones;
FinAlgoritmo

Funcion resultado <- CaidaHuevosFB ( huevos, pisos, operaciones Por Referencia )
	Definir x, minimo, seRompe, noSeRompe, peorCaso Como Entero;

	Si pisos = 0 O pisos = 1 Entonces
		resultado <- pisos;
	Sino
		Si huevos = 1 Entonces
			resultado <- pisos;
		Sino
			minimo <- 999999;
			Para x <- 1 Hasta pisos Con Paso 1 Hacer
				operaciones <- operaciones + 1;
				seRompe   <- CaidaHuevosFB(huevos - 1, x - 1, operaciones);
				noSeRompe <- CaidaHuevosFB(huevos, pisos - x, operaciones);
				Si seRompe > noSeRompe Entonces
					peorCaso <- 1 + seRompe;
				Sino
					peorCaso <- 1 + noSeRompe;
				FinSi
				Si peorCaso < minimo Entonces
					minimo <- peorCaso;
				FinSi
			FinPara
			resultado <- minimo;
		FinSi
	FinSi
FinFuncion
