#include "json.h"

//cd desktop\"projet JSON"
//les fonctions sublimontaire :
int toInt(char *S){
	int a=0,i,n=strlen(S);
	for(i=0;i<n;i++){
		a=a*10+(S[i]-48);
	}
	return a;
}

double toReel(char *S){
	double a=0;
	int i,n=strlen(S),trouve=0,e=0;
	for(i=0;i<n;i++){
		if(S[i]=='.'){
			trouve=1;
			continue;
		}
		if(!trouve){
			a=a*10+(S[i]-48);
		}else{
			a=a*10+(S[i]-48);
			e++;
		}
	}
	a=a*pow(10,-e);
	return a;
}


jsonList initList(){
	jsonList list;
	list.nbrE=0;
	list.nbrR=0;
	list.nbrS=0;
	list.e=NULL;
	list.r=NULL;
	list.s=NULL;
	return list;
}

char *popBreaket(char *S){
	int len=strlen(S);
	char *newS=(char *)calloc(len,sizeof(char)),*p,*q;
	for(p=S+1,q=newS;p<S+len-2;p++){
		if(*p!='\n'&&*p!=' ') {
			*q = *p;
			q++;
		}
		*q='\0';
	}
	return newS;
}

char **popcamma(char *S){
	char **tString,**String,**s,**p,*q,*r;
	int n;
	const int len=strlen(S);
	// spliting
	tString = (char **)calloc(len,sizeof(char *));
	for(p=tString;p<tString+len;p++) *p = (char *)calloc(len,sizeof(char));
	for(p=tString,r=S;r<S+len;p++,r++){
		for(q=*p;*r!=','&&r<S+len;q++,r++) *q=*r;
		*q='\0';
	}
	strcpy(*p,"$");// le caractaire $ pour definir la fin d d une chaine du caractaire
	n = p-tString;
	//pour optimizer la memoire
	String = (char **)calloc(n+1,sizeof(char *));
	for(p=tString,s=String;s<=String+n+1;s++,p++) *s = (char *)calloc(strlen(*p)+1,sizeof(char));
	for(p=tString,s=String;strcmp(*p,"$");p++,s++) {
		strcpy(*s,*p);
	}
	strcpy(*s,"$");
	free(tString);
	return String;
}


int isInt(char *S){
	const int len = strlen(S);
	char *r;
	for(r=S;r<S+len;r++) if(*r=='.'||*r=='"') return 0;
	return 1;
}
int isReel(char *S){
	if(isInt(S)) return 0;
	if(*S=='"') return 0;
	return 1;
}
int isString(char *S){
	if(*S=='"') return 1;
	return 0;
}
void addInt(jsonList* liste,int a){
	if(liste->e==NULL){
		liste->e = (int *)calloc(1,sizeof(int));
		liste->nbrE = 1;
	}else{
		realloc(liste->e,liste->nbrE+1);
		liste->nbrE++;
	}
	liste->e[liste->nbrE-1] = a;
}
void addReel(jsonList* liste,double a){
	if(liste->r==NULL){
		printf("alert1\n");
		liste->r = (double *)calloc(1,sizeof(double));
		printf("alert2\n");
		liste->nbrR = 1;
		printf("alert3\n");
	}else{
		realloc(liste->r,liste->nbrR+1);
		liste->nbrR++;
	}
	realloc(liste->r,liste->nbrR+1);
	liste->nbrR++;
	printf("alert4\n");
	liste->r[liste->nbrR-1] = a;
	printf("alert5\n");
}
void addString(jsonList* liste,char *S){
	if(liste->s==NULL){
		liste->s = (char **)calloc(1,sizeof(char *));
		liste->nbrS = 1;
	}else
	{
		realloc(liste->s,liste->nbrS+1);
		liste->nbrS++;
	}
	const int len = strlen(S);
	liste->s[liste->nbrS-1] = (char *)calloc(len,sizeof(char));
	strcpy(liste->s[liste->nbrS-1],S);
}
jsonList jsonLprint(char *S){
	jsonList liste = initList();
	char *S1,**S2,**p,*q;
	S1 = popBreaket(S);
	S2 = popcamma(S1);
	for(p=S2;strcmp(*p,"$");p++){
		q=*p;
		if(isInt(q)) addInt(&liste,toInt(q));
		else if(isReel(q)) {
			addReel(&liste,toReel(q));
		}
		else addString(&liste,q);
	}
	free(S1);
	free(S2);
	return liste;
}
