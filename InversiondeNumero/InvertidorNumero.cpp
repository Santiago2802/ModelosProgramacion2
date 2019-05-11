/*
Programa para invertir un numero entero usando recursividad
Gabriel Esteban Castillo Ramire
11-05-2019
*/
#include<iostream>
#include<math.h>
using namespace std;

int invertirNumero(int recepcion){
	
	static int potencia=-1; 
	int descomp=1;
	
	if(recepcion!=0){
		
		for(descomp;recepcion%descomp!=recepcion;descomp*=10);
		descomp/=10;
		potencia++;  
		return (recepcion/descomp)*(pow(10,potencia))+
				invertirNumero(recepcion%descomp);
	}	
	return 0;
}


int main(){
	int ingreso;
	cout<<"Ingrese numero a invertir: ";
	cin>>ingreso;
	
	cout<<endl<<"El numero invertido es: "<<invertirNumero(ingreso);
	
}
