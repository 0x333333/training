#include <stdio.h>
#include <memory.h>
 
#define OK 1
#define ERROR 0
#define OVERFLOW -1
#define NOTFOUND -2
#define MAXLEN 10000    //La limité de longeur de string
#define MAXCMD 20       //La limité de longeur de commande
 
 
typedef struct
{
    char *ch;
    int length;
}String;
 
 
int StrAssign(String *T,char *chars)
{   
    if (T->ch) free(T->ch);
    int i,len;

    // Calculer la longeur de string
    for (len=0;chars[len];len++);
 
    // Si string est nul
    if (!len)  
    {
        T->ch=NULL;
        T->length=0;
    }
    else
    {
        // Assigner l'espace à T->ch
        if (!(T->ch=(char*)malloc(len*sizeof(char)))) 
            return OVERFLOW;
        // Assigner le contenu
        for (i=0;i<len;i++) 
            T->ch[i]=chars[i];
        // Assigner la longeur
        T->length=len;
    }
   
    return OK;
}
 
 
int StrLength(String T)
{
    return T.length;
}
 
int StrPrint(String T)
{
    int i;
    if (T.length)
    {
        for (i=0;i<T.length;i++) 
            printf("%c",T.ch[i]);
        printf("\n");
    }
    else printf("Rien à imprimer.\n");
    return OK;
}
 
 
int CharsCompare(char *T,char *S)
{
    int i;
    for (i=0;T[i] && S[i];i++)
        if (T[i]!=S[i]) 
            return T[i]>S[i]?1:-1;
    return T[i]?1:0;
}
 
int main()
{
    char cmd[MAXCMD]={0};     // Commande
    int ret;                  // Le retour de la fonctions
    String S[MAXLEN]={0},*p;  //S:String  p:Pointeur à String
    char tmp[MAXLEN]={0};
 
    printf("***********************************************\n");
    printf("------ Première implementaion du String ------\n");
    printf("La maxime longeur du string: %d\n",MAXLEN);
    printf("Options de commandes: \n");
    printf("0: StrAssign \n");
    printf("1: StrLength \n");
    printf("2: StrPrint \n");
    printf("#: Quit \n");
    printf("***********************************************\n");
 
    while (1)
    {
        scanf("%s",cmd);// Lire la commande
 
        if (cmd[0]=='#') break; // Quiter
       
                  
        if (!CharsCompare(cmd,"0\0"))
        {
            scanf("%s",tmp);    // La valeur initial
            p=&S[0];
            ret=StrAssign(p,tmp);
        }
       
        else if (!CharsCompare(cmd,"1\0"))
        {
            p=&S[0];
            ret=StrLength(*p);
           
            printf("length is %d.\n",ret);
            ret=OK;
        }
       
        else if (!CharsCompare(cmd,"2\0"))
        {
            p=&S[0];
            ret=StrPrint(*p);
        }
        else
        {
            printf("The Command is Error.\n");
        }
 
        if (ret==OK) 
            printf("This Command is Successful.\n\n");
        else if (ret==ERROR) 
            printf("The input data is Error.\n\n");
        else if (ret==OVERFLOW) 
            printf("OVERFLOW.\n\n");
    }
 
    return 0;
}