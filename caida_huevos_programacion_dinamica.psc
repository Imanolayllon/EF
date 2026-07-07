Algoritmo CaidaHuevos_ProgramacionDinamica
	Definir nHuevos, nPisos, operaciones, memoriaCeldas Como Entero;
	Definir k, n, x, mejor, valRompe, valNoRompe, peor Como Entero;
	Definir dp Como Entero;
	Dimension dp[31, 201];

	Escribir "==================================================";
	Escribir "  CAIDA DE HUEVOS - PROGRAMACION DINAMICA";
	Escribir "==================================================";
	Escribir Sin Saltar "Ingrese la cantidad de huevos (1..30): ";
	Leer nHuevos;
	Escribir Sin Saltar "Ingrese la cantidad de pisos (1..200): ";
	Leer nPisos;

	operaciones <- 0;
	memoriaCeldas <- (nHuevos + 1) * (nPisos + 1);

	Para n <- 1 Hasta nPisos Con Paso 1 Hacer
		dp[1, n] <- n;
	FinPara
	Para k <- 1 Hasta nHuevos Con Paso 1 Hacer
		dp[k, 1] <- 1;
	FinPara

	Para k <- 2 Hasta nHuevos Con Paso 1 Hacer
		Para n <- 2 Hasta nPisos Con Paso 1 Hacer
			mejor <- 999999;
			Para x <- 1 Hasta n Con Paso 1 Hacer
				operaciones <- operaciones + 1;
				Si (x - 1) = 0 Entonces
					valRompe <- 0;
				Sino
					valRompe <- dp[k - 1, x - 1];
				FinSi
				Si (n - x) = 0 Entonces
					valNoRompe <- 0;
				Sino
					valNoRompe <- dp[k, n - x];
				FinSi
				Si valRompe > valNoRompe Entonces
					peor <- 1 + valRompe;
				Sino
					peor <- 1 + valNoRompe;
				FinSi
				Si peor < mejor Entonces
					mejor <- peor;
				FinSi
			FinPara
			dp[k, n] <- mejor;
		FinPara
	FinPara

	Escribir "--------------------------------------------------";
	Escribir "Con ", nHuevos, " huevo(s) y ", nPisos, " piso(s):";
	Escribir "Minimo de lanzamientos en el peor caso = ", dp[nHuevos, nPisos];
	Escribir "Cantidad de operaciones                = ", operaciones;
	Escribir "Memoria usada (celdas de la tabla dp)  = ", memoriaCeldas;
FinAlgoritmo
