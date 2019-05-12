/*
Programa para imprimir la inversion de un numero entero usando recursividad
Gabriel Esteban Castillo Ramire
11-05-2019
*/
#include<iostream>
#include<math.h>
using namespace std;

void invertirNumero(int recepcion){
	if(recepcion!=0){		
		cout<<recepcion%10; 
		return invertirNumero(recepcion/10);
	}	
}


int main(){
	int ingreso;
	cout<<"Ingrese numero a invertir: ";
	cin>>ingreso;
	invertirNumero(ingreso);
	
}
