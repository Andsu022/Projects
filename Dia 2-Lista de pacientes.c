#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct paciente{
    int id_Paciente;
    char *nome_Paciente;
    char *estado_Saude_atual;
    struct paciente* proximo;
}Paciente;

Paciente* criarLista(){
    return NULL;
}

Paciente* adicionarPaciente(Paciente* p, char *nome, int id, char *estado_saude){
    
    Paciente *novo = (Paciente*)malloc(sizeof(Paciente));

    novo->id_Paciente = id;
    novo->nome_Paciente = strdup(nome);
    novo->estado_Saude_atual = strdup(estado_saude);
    novo->proximo = p;
    
    return novo;
}

void Mostrar_Lista(Paciente* p){
    Paciente* aux = p;
    while(aux!=NULL){
        printf("\n|ID: %d", aux->id_Paciente);
        printf("\n|Paciente: %s", aux->nome_Paciente);
        printf("\n|Estado de saude: %s", aux->estado_Saude_atual);
        printf("\n|---------------------------------------------|");
        aux = aux->proximo;
    }
}

int main(){
    Paciente* p;
    char *nome;
    char *estado_saude;
    int id;

    p = criarLista();
    p = adicionarPaciente(p, "Anderson", 01, "estavel");
    p = adicionarPaciente(p, "Andre", 02, "em tratamento intensivo");
    Mostrar_Lista(p);
}