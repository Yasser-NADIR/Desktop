#include "graphe.h"

//pour le point
Point *createPoint(int x, int y){
	Point *point;
	point = (Point *)malloc(sizeof(Point));
	point->x = x;
	point->y = y;
	return point;
}

int comparePoint(Point *point1, Point *point2){
	return point1->x == point2->x && point1->y == point2->y;
}

//pour les sommets
EleSommet *createEleSommet(Point *point){
  EleSommet *element;
  element = (EleSommet *)malloc(sizeof(EleSommet));
  element->point = point;
  element->arc = NULL;
  return element;
}

Sommet *createSommet(EleSommet *eleSommet){
  Sommet *sommet;
  sommet = (Sommet *)malloc(sizeof(Sommet));
  sommet->eleSommet = eleSommet;
  sommet->next = NULL;
  return sommet;
}

Sommet *lastSommet(Sommet *sommet){
  if(sommet){
    while(sommet->next) sommet = sommet->next;
  }
  return sommet;
}

EleSommet *searchEleSommet(Sommet *sommet, Point *point){
  while(sommet){
    if(comparePoint(sommet->eleSommet->point, point)) return sommet->eleSommet;
    sommet = sommet->next;
  }
  return NULL;
}

void addSommet(Sommet **sommet, EleSommet *eleSommet){
  Sommet *element, *dernier;
  element = createSommet(eleSommet);
  if(*sommet == NULL){
    *sommet = element;
    return ;
  }
  dernier = lastSommet(*sommet);
  dernier->next = element;
}

void displaySommet(Sommet *sommet){
  while(sommet){
    printf("(%d;%d)", sommet->eleSommet->point->x, sommet->eleSommet->point->y);
    if(sommet->next) printf("-");
    sommet = sommet->next;
  }
  printf("\n");
}

void freeSommet(Sommet **sommet){
  Sommet *element;
  while(*sommet){
    element = *sommet;
    *sommet = (*sommet)->next;
    //freeArret(&element->eleSommet->arret);
    free(element->eleSommet->point);
    free(element->eleSommet);
    free(element);
  }
}

//pour les arret
EleArc *createEleArc(EleSommet *eleSommet1, EleSommet *eleSommet2){
  EleArc *eleArc;
  eleArc = (EleArc *)malloc(sizeof(EleArc));
  eleArc->actualPhero = 0;
  eleArc->acumulePhero = 0;
  eleArc->eleSommet1 = eleSommet1;
  eleArc->eleSommet2 = eleSommet2;
  return eleArc;
}


Arc *createArc(EleArc *eleArc){
  Arc *arc;
  arc = (Arc *)malloc(sizeof(Arc));
  arc->eleArc = eleArc;
  arc->next = NULL;
  return arc;
}

Arc *lastArc(Arc *arc){
  if(arc){
    while(arc->next) arc = arc->next;
  }
  return arc;
}

EleArc *searchEleArc(Arc *arc, EleSommet *eleSommet1, EleSommet *eleSommet2){
  if(!eleSommet1 || !eleSommet2) return NULL;
  while(arc){
    if(arc->eleArc->eleSommet1 == eleSommet1 && arc->eleArc->eleSommet2 == eleSommet2) break;
    arc = arc->next;
  }
  return arc->eleArc;
}

void addArc(Arc **arc, EleArc *eleArc){
  Arc *element, *dernier;
  element = createArc(eleArc);
  if(*arc == NULL){
    *arc = element;
    return ;
  }
  dernier = lastArc(*arc);
  dernier->next = element;
}

void displayArc(Arc *arc){
  while(arc){
    printf("(%d;%d)->(%d;%d) actuel Pheromone:%f, Pheromone acumule:%f\n", arc->eleArc->eleSommet1->point->x, arc->eleArc->eleSommet1->point->y, arc->eleArc->eleSommet2->point->x, arc->eleArc->eleSommet2->point->y, arc->eleArc->actualPhero, arc->eleArc->acumulePhero);
    arc = arc->next;
  }
}

void freeArc(Arc **arc){
  Arc *element;
  while(*arc){
    element = *arc;
    *arc = (*arc)->next;
    free(element->eleArc);
    free(element);
  }
}

//pour le Graphe
Graphe *createGraphe(){
  Graphe *graphe;
  graphe = (Graphe *)malloc(sizeof(Graphe));
  graphe->sommet = NULL;
  graphe->arc = NULL;
  return graphe;
}

void addSommetToGraphe(Graphe **graphe, Point *point){
  EleSommet *element;
  element = createEleSommet(point);
  addSommet(&(*graphe)->sommet, element);
}

void displaySommetGraphe(Graphe *graphe){
  printf("les sommets de la graphe sont : ");
  displaySommet(graphe->sommet);
}

void addArcToGraphe(Graphe **graphe, Point *point1, Point *point2){
  //creation de liaison arc->sommet
  //ici on suppost que les sommet sont deja creer 
  //car les sommet sont les position
  EleSommet *eleSommet1, *eleSommet2;
  EleArc *element;
  eleSommet1 = searchEleSommet((*graphe)->sommet, point1);
  eleSommet2 = searchEleSommet((*graphe)->sommet, point2);
  element = createEleArc(eleSommet1, eleSommet2);
  addArc(&(*graphe)->arc, element);

  //creation de liaison sommet->arc
  //puisque ici on a un arc danc la liaison se fait just avec sommet1
  //car eleSommet2 de de ce eleArc represante les sommet adjasante de eleSommet 1
  addArc(&eleSommet1->arc, element);
}

void displayArcGraphe(Graphe *graphe){
  printf("les arcs du graphe sont : \n");
  displayArc(graphe->arc);
}

void breakLienArcSommet(Graphe **graphe){
  Arc *arc;
  arc = (*graphe)->arc;
  while(arc){
    arc->eleArc->eleSommet1 = NULL;
    arc->eleArc->eleSommet2 = NULL;
    arc = arc->next;
  }
}

void breakLienSommetArc(Graphe **graphe){
  Sommet *sommet;
  Arc *arc;
  sommet = (*graphe)->sommet;
  while(sommet){
    arc = sommet->eleSommet->arc;
    while(arc){
      arc->eleArc = NULL;
      arc = arc->next;
    }
    sommet = sommet->next;
  }
}

void freeArcGraphe(Graphe **graphe){
  freeArc(&(*graphe)->arc);
}

void freeSommetGraphe(Graphe **graphe){
  freeSommet(&(*graphe)->sommet);
}

void freeGraphe(Graphe **graphe){
  breakLienArcSommet(graphe);
  breakLienSommetArc(graphe);
  freeArcGraphe(graphe);
  freeSommetGraphe(graphe);
  free(*graphe);
}


Graphe *initGraphe(int x, int y){
	Graphe *graphe;
	int i, j;
	graphe = createGraphe();
	for(i=1; i<=x; i++){
		for(j=1; j<=y; j++){
			addSommetToGraphe(&graphe, createPoint(i,j));
		}
	}

	for(i=1; i<=x; i++){
		for(j=1; j<=y; j++){
			if(i-1>=1) addArcToGraphe(&graphe, createPoint(i,j), createPoint(i-1,j));
			if(i+1<=x) addArcToGraphe(&graphe, createPoint(i,j), createPoint(i+1,j));
			if(j-1>=1) addArcToGraphe(&graphe, createPoint(i,j), createPoint(i,j-1));
			if(j+1<=y) addArcToGraphe(&graphe, createPoint(i,j), createPoint(i,j+1));
			if(i-1>=1 && j-1>=1) addArcToGraphe(&graphe, createPoint(i,j), createPoint(i-1,j-1));
			if(i-1>=1 && j+1<=y) addArcToGraphe(&graphe, createPoint(i,j), createPoint(i-1,j+1));
			if(i+1<=x && j-1>=1) addArcToGraphe(&graphe, createPoint(i,j), createPoint(i+1,j-1));
			if(i+1<=x && j+1<=y) addArcToGraphe(&graphe, createPoint(i,j), createPoint(i+1,j+1));
		}
	}

	return graphe;
}

void updateAcumulePhero(Graphe **graphe, Point *point1, Point *point2, float pheroDepose){
  //premierement on va chercher arc (element1, element2)
  EleSommet *element1, *element2;
  EleArc *eleArc;
  element1 = searchEleSommet((*graphe)->sommet, point1);
  element2 = searchEleSommet((*graphe)->sommet, point2);
  eleArc = searchEleArc((*graphe)->arc, element1, element2);
  if(eleArc == NULL){
    printf("Erreur: cet arc n'existe pas\n");
    return ;
  }
  //après on maj leur contité de pheromone
  eleArc->acumulePhero += pheroDepose;
}

void updatePhero(Graphe **graphe){
  Arc *arc;
  arc = (*graphe)->arc;
  while(arc){
    arc->eleArc->actualPhero = (1-VAPORISATION)*arc->eleArc->actualPhero + arc->eleArc->acumulePhero;
    //après le calcule il faut mis a zero la quantité acumulé
    arc->eleArc->acumulePhero = 0;
    arc = arc->next;
  }

}

float getPhero(Graphe *graphe, Point *point1, Point *point2){
  float phero;
  EleSommet *element1, *element2;
  EleArc *element;

  element1 = searchEleSommet(graphe->sommet, point1);
  element2 = searchEleSommet(graphe->sommet, point2);
  element = searchEleArc(graphe->arc, element1, element2);
  return element->actualPhero;
}

//la definition le prochain point
Point *getNextPoint(int choix, Point *actualPoint){
  Point *nextPoint;
  nextPoint = createPoint(actualPoint->x, actualPoint->y);
  switch(choix){
    case 1:
    nextPoint->x += 1;
    break;

    case 2:
    nextPoint->x += 1;
    nextPoint->y += 1;
    break;

    case 3:
    nextPoint->y += 1;
    break;

    case 4:
    nextPoint->x -= 1;
    nextPoint->y += 1;
    break;

    case 5:
    nextPoint->x -= 1;
    break;

    case 6:
    nextPoint->x -= 1;
    nextPoint->y -= 1;

    break;

    case 7:
    nextPoint->y -= 1;
    break;

    case 8:
    nextPoint->x += 1;
    nextPoint->y -= 1;
    break;
  }
  return nextPoint;
}

//la verification le prochain position
int isRightDerection(Point *point, int xLimit, int yLimit){
  if(point->x<1 || point->x>xLimit || point->y<1 || point->y>yLimit) return 0;
  return 1;
}

int getRandNumber(int max){
  int choix;
  do{
    srand(time(NULL));
    choix = rand()%max;
  }while(choix == 0);
  return choix;
}