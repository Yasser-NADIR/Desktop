#include "json.h"


int main(int argc,char *argv[]){
	FILE *f = fopen("test.json", "r");
	jsonList liste=initList();
	char baffer[1024];
	fread(baffer,sizeof(char),1024,f);
	fclose(f);
	liste = jsonLprint(baffer);
	/*printf("le nombre des entier est : ");
	printf("%d\n",liste.nbrE);
	printf("le nombre des reel est : ");
	printf("%d\n",liste.nbrR);
	printf("le nombre des chaine du caractaire est : ");
	printf("%d\n",liste.nbrS);
	printf("%d\n",liste.e[0]);
	printf("%f\n",liste.r[0]);
	printf("%s\n",liste.s[0]);*/
	//system("pause");
	return 0;
}
