#ifndef GRAPHE_H
#define GRAPHE_H

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define VAPORISATION 0.3

typedef struct Arc Arc;

typedef struct{
	int x;
	int y;
}Point;//la structure de point

typedef struct{
  Point *point;
  Arc *arc;
}EleSommet;//la structure de element de sommet

typedef struct Sommet{
  EleSommet *eleSommet;
  struct Sommet *next;
}Sommet;//la structure de liste chaine de sommet

typedef struct{
  float actualPhero;
  float acumulePhero;
  EleSommet *eleSommet1;//ordre est important car on a des arcs
  EleSommet *eleSommet2;//donc arc = (eleSommet1, eleSommet2)
}EleArc;//la structure de donné de element d'arc

typedef struct Arc{
  EleArc *eleArc;
  struct Arc *next;
}Arc;//la structure de donné de liste chainé des arc

typedef struct{
  Sommet *sommet;
  Arc *arc;
}Graphe;//la structure de graphe

//les fonctions concernant la structure de points
Point *createPoint(int x, int y);
int comparePoint(Point *point1, Point *point2);

//les fonctions de manipulation de la liste chainée des sommets
EleSommet *createEleSommet(Point *point);
Sommet *createSommet(EleSommet * eleSommet);
Sommet *lastSommet(Sommet *sommet);
EleSommet *searchEleSommet(Sommet *sommet, Point *point);
void addSommet(Sommet **sommet, EleSommet * eleSommet);
void displaySommet(Sommet *sommet);
void freeSommet(Sommet **sommet);

//les fonctiond de manipulation de la liste chainée des arrêts
EleArc *createEleArc(EleSommet *eleSommet1, EleSommet *eleSommet2);
Arc *createArc(EleArc *eleArc);
Arc *lastArc(Arc *arc);
EleArc *searchEleArc(Arc *arc, EleSommet *eleSommet1, EleSommet *eleSommet2);
void addArc(Arc **arc, EleArc *eleArc);
void displayArc(Arc *arc);
void freeArc(Arc **arc);

//les fonctions de manipulation du graphe
Graphe *createGraphe();
//pour les sommets
void addSommetToGraphe(Graphe **graphe, Point *point);
void displaySommetGraphe(Graphe *graphe);
//pour les arrets
void addArcToGraphe(Graphe **graphe,Point *point1, Point *point2);
void displayArcGraphe(Graphe *graphe);

//pour liberer la mem pour le graphe
void breakLienArcSommet(Graphe **graphe);
void breakLienSommetArc(Graphe **graphe);
void freeArcGraphe(Graphe **graphe);
void freeSommetGraphe(Graphe **graphe);
void freeGraphe(Graphe **graphe);

//initialisation du graphe par les points convenable
Graphe *initGraphe(int x, int y);

//mis à jour la quantité acumulé de pheromone
void updateAcumulePhero(Graphe **graphe, Point *point1, Point *point2, float pheroDepose);

//mis à jour la quantié de pheromone dans l'instant t basant sur la quantité de pheromone dans l'instant t-1 et la quantité de pheromone acumulé
void updatePhero(Graphe **graphe);

//avoir la quantité de pheromone d'un arc
float getPhero(Graphe *graphe, Point *point1, Point *point2);

//avoir la prochain position celon les 8 positions
Point *getNextPoint(int choix, Point *actualPoint);

//la verification la prochain position
int isRightDerection(Point *point, int xLimit, int yLimit);

int getRandNumber(int max);

#endif
