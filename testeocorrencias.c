#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>
#define A 5
#define B 5

int main(){
    int mat[A][B];
    int num;
    srand(time(NULL));

    //pedir pro usuário preencher a matriz
    printf("Digite com quantos numeros quer preencher a matriz: ");
        scanf("%d", &num);
    system("cls");

    //realizar alocação dinâmica do ponteiro de ocorrencias
    int *ocorrencia = (int *)malloc(num * sizeof(int));
    if(ocorrencia == NULL){
        printf("\nErro de alocacao de memoria !!");
        return 1;
    }
    
    //inicializar vetor de ocorrencias
    for(int i = 0; i < num; i++){
        ocorrencia[i] = 0;
    }

    //preencher a matriz e verificar ocorrências
    for(int i = 0; i < A; i++){
        for(int j = 0; j < B; j++){
            mat[i][j] = rand() % num;
            ocorrencia[mat[i][j]]++;
        }  
    }

    for(int i = 0; i < A; i++){
        for(int j = 0; j < B; j++){
            printf("%d ", mat[i][j]);
        }  
        printf("\n");
    }

    for(int i = 0; i < num; i++){
        if(ocorrencia[i] > 0){
            printf("\nNumero %d Ocorrencia(s): %d", i, ocorrencia[i]);
        }
    }

    return 0;
}