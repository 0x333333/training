#include <stdio.h>
#include <memory.h>
 
#define OK 1
#define OVERFLOW -1
#define NOTFOUND 0
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

int Annonce(String S1, String S2)
{
	int len = (S1.length < S2.length) ? S1.length : S2.length;
	// {len <= S1.length && len <= S2.length 
	//  && (len == S1.length || len == S1.length)}
	int i, j;
	int maxSame=0;
	// {maxSame == 0}
	for (i=1;i<=len;i++)
	{
		// {i == 1}
		int k = 0;
		// {k == 0}
		for (j=S1.length-i;j<S1.length;j++)
		{
			// {j == S1.length-1}
			if (S1.ch[j]==S2.ch[k])
				// {S1.ch[j]==S2.ch[k]}
			    k++;
			    // {k' = k + 1}
			else
			    break;			
		}
		maxSame = (maxSame>=k)?maxSame:k;
		// {(maxSame == maxSame && maxSame>=k) ||
		//  (maxSame == k && maxSame<k)}
	}
	if (!maxSame)
		printf("Rien à imprimer.\n");
	else
	{
		printf("La chaîn c = ");
        for (i=0;i<maxSame;i++)
        	// {i == 0}
            printf("%c",S2.ch[i]);
        // {i == maxSame-1}
        printf("\n\n");
	}
	return OK;
}
 
int main()
{
    String S1[MAXLEN]={0};
    String S2[MAXLEN]={0};  // Les deux string à comparer
    String *p1, *p2;
    char tmp[MAXLEN]={0};
 	int ret;                  // Le retour de la fonctions

 	while (1)
 	{
 		printf("String 1: \n");
		scanf("%s",tmp);
		p=&S1[0];
		StrAssign(p,tmp);

		printf("String 2: \n");
		scanf("%s",tmp);
		p=&S2[0];
		StrAssign(p, tmp);

		Annonce(*&S1[0], *&S2[0]);
 	}
 
    return 0;
}