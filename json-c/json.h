#ifndef JSON_H
#define JSON_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef struct list{
	int    *e;
	double *r;
	char   **s;
	int nbrE;
	int nbrR;
	int nbrS;
}jsonList;


// outil sublimentaire
int toInt(char *);
double toReel(char *);

//pour traiter un fichier JSON de type [ valeur, valeur, ...]:
//pour initialiser une liste JSON :
jsonList initList();
//pour enlever les [] :
char *popBreaket(char *);
//pour enlever les vergule :
char **popcamma(char *);
//pour detecter les entiers :
int isInt(char *);
//pour detecter les réels :
int isReel(char *);
//pour detecter les chînes des caeactaires :
int isString(char *);
//ajouter entier au liste :
void addInt(jsonList *,int );
//ajouter réel au liste :
void addReel(jsonList *,double );
//ajouter chaîne de caractaires au liste :
void addString(jsonList *,char* );
//ecririe dans la structure de jsonList
jsonList jsonLprint(char *);


#endif
