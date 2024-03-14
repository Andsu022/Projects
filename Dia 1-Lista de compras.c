#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define TAM 20

    typedef struct lista{
        char nome_produto[10];
        int quantidade;
    }Lista;

    void adicionar_itens(){
        int quant;

        struct lista Lista[TAM];

        printf("\nDigite quantos produtos quer adicionar: ");
        scanf("%d", &quant);
        setbuf(stdin,NULL);

        for(int i = 0; i <= quant; i++){
            printf("\nDigite o nome do produto: ");
                scanf("%[^\n]s", &Lista[i].nome_produto);
            printf("\nDigite a quantidade do produto: ");
                scanf("%d", &Lista[i].quantidade);
            setbuf(stdin,NULL);
        }
    }

    void mostrar_lista(){

        struct lista Lista[TAM];
        for(int i= 0; i <= sizeof(Lista); i++){
           printf("\nProduto: %s\nQuantidade: %d", Lista[i].nome_produto, Lista[i].quantidade);
            
        }
        
    }

    int main(){
        int menu;

        while(menu!=4){
            printf("\nMENU\n1-Adicionar Produto na lista\n2-Remover produto da lista\n3-Mostrar lista\n4-Sair\nOPC:");
                scanf("%d", &menu);
            
            switch(menu){
                
                case 1:
                    adicionar_itens();
                    system("pause");
                    system("cls");
                break;
                
                case 2:
                    printf("OPCAO INDISPONIVEL NO MOMENTO !!!");
                    system("pause");
                    system("cls");
                break;

                case 3:
                    mostrar_lista();
                    system("pause");
                    system("cls");
                break;

                case 4:
                    printf("ENCERRANDO...");
                    system("exit");
                break;
            
                default:
                    printf("OPCAO INVÁLIDA !!!");
                break;
            }
        }
        return 0;
    }