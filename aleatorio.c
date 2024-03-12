#include<stdio.h>
#include<stdlib.h>
#include<string.h>

    void contador(int num){
        int tabuada;
        
        for(int i = 0; i < 10; i++){
            tabuada = num*(i+1);
            printf("\n%d x %d = %d", num, i+1, tabuada);
            
        }
        printf("\nFim !");
    }
    
    int main(){
        int num;


        printf("\nDigite o numero que voce quer fazer a tabuada: ");
            scanf("%d", &num);

        system("cls");
        contador(num);
    }