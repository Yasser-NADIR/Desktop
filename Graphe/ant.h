#ifndef ANT_H
#define ANT_H

#include "graphe.h"


typedef struct Path{
	Point *point;
	struct Path *next;
}Path;//la structure de chemin

typedef struct Ant{
	Path *path;//liste chainnée 
	Path *actualPosition;//un seul élément
	int lenghPath;
}Ant;//la structure de fourmi

//pour le chemin
Path *createPath(Point *point);
Path *getLast(Path *path);
void addPath(Path **path, Point *point);
void displayPath(Path *path);
void freePath(Path **path);
int countLenghPath(Path *path);
//test existance une point dans une chemin
int isExistPoint(Path *path, Point *point);
Path *searchPaht(Path *path, Point *point);

//pour la fourmie
Ant *createAnt(Point *nest);
void addPathAnt(Ant **ant, Point *point);
void takeStep(Ant **ant);

//la generation de chemin basant
//sur la quantité de pheromone deposé sur les arcs
Ant *generatePath(Graphe *graphe, Point *start, Point *food);

//la validation d'un chemin complé
//un chemin complé est un chemin qui valide
//la structure suivante nid->..->nouriture->..->nid
int validePath(Path *path, Point *nest, Point *food);

//la generation de chemin aleatoire en respectant les conditions les bons choix
Ant *generateRandomPath(Point *nest, Point *food);

//pour verifier si tous les fourmies de tableau de fourmie ont fini ses tours
int isEnd(Ant **tabAnt, int nbr);

//ecrasement des cycles dans les chemins
void deleteCyclePath(Ant *ant, Point *nest, Point *food);

//ecrire dans un fichier les chemin utiliser
void writePathFile(Path *path);
#endif