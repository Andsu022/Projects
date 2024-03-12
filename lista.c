#include"lista.h"
#include<stdio.h>

typedef struct lista{
    int valor;
    Lista* proximo;
}Lista;

Lista *criarLista(){
    return NULL;
}

Lista* inserirValores(Lista* l, int num){
    Lista *aux = l;
    int atual;
    if(aux == NULL){
        aux->valor = num;
        aux->proximo = NULL;
    }else{
        atual = l;
        aux->valor = num;
        aux->proximo = atual
    }
}