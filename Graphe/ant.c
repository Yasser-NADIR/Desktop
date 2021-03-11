#include "ant.h"

Path *createPath(Point *point){
	Path *path;
	path = (Path *)malloc(sizeof(Path));
	path->point = point;
	path->next = NULL;
	return path;
}

Path *getLast(Path *path){
	if(path!=NULL) while(path->next) path = path->next;
	return path;
}

void addPath(Path **path, Point *point){
	Path *element, *last;
	element = createPath(point);
	if(*path==NULL){
		*path = element;
		return ;
	}
	last = getLast(*path);
	last->next = element;
}

void displayPath(Path *path){
	while(path){
		printf("(%d,%d) ",path->point->x, path->point->y);
		path = path->next;
	}
	printf("\n");
}

void freePath(Path **path){
	Path *aux;
	while(*path){
		aux = *path;
		*path = (*path)->next;
		free(aux->point);
		free(aux);
	}
}

int countLenghPath(Path *path){
	int s;
	s = 0;
	if (path) while(path->next){
		s++;
		path = path->next;
	}
	return s;
}

//existance d'une point
int isExistPoint(Path *path, Point *point){
	while(path){
		if(comparePoint(path->point, point)) return 1;
		path = path->next;
	}
	return 0;
}

//la recherche de chemin dans une liste chainée
Path *searchPaht(Path *path, Point *point){
	while(path){
		if(comparePoint(path->point, point)) break;
		path = path->next;
	}
	return path;
}

//pour la fourmie
Ant *createAnt(Point *nest){
	Ant *ant;
	ant = (Ant *)malloc(sizeof(Ant));
	ant->path = createPath(nest);
	ant->actualPosition = ant->path;
	ant->lenghPath = 0;
	return ant;
}

void addPathAnt(Ant **ant, Point *point){
	addPath(&(*ant)->path, point);
	(*ant)->lenghPath += 1;
}

void takeStep(Ant **ant){
	if ((*ant)->actualPosition) (*ant)->actualPosition = (*ant)->actualPosition->next;
}


//la generatione
Ant *generatePath(Graphe *graphe, Point *nest, Point *food){
	Ant *ant;
	Path *path, *lastElement;
	Arc *arc, *eleSommetArc;
	Sommet *sommet;
	EleSommet *ele1, *ele2, *ele3;
	float phero1, phero2;

	ant = (Ant *)malloc(sizeof(Ant));
	path = createPath(nest);
	lastElement = path;
	arc = graphe->arc;
	sommet = graphe->sommet;
	ele1 = searchEleSommet(sommet, nest);

	do{
		eleSommetArc = ele1->arc;
		ele2 = eleSommetArc->eleArc->eleSommet2;
		
		while(eleSommetArc){
			ele3 = eleSommetArc->eleArc->eleSommet2;
			phero1 = getPhero(graphe, ele1->point, ele2->point);
			phero2 = getPhero(graphe, ele1->point, ele3->point);
			//comparePoint(lastElement->point, ele3->point) == 0: cette comparaison sert à evite le va et vient
			//ex: si on a de arc (a, b), (b, a) et (b, c) qui ont le meme quantité de pheromone alors 
			//on peut tomber sur une boucle infini (a, b)->(b, a)->(a, b)
			//avec cette condition on evite ce probleme
			//d'autre par si il y a deux arc ont le meme quantité de pheromone
			//si 2 arc ou plus on le meme quantité de pheromone
			//il va choisi aleatoiremen
			if(comparePoint(lastElement->point, ele3->point) == 0 ){
				if(phero1==phero2){
					//dans ce block on va essayer si 2 arcs on le même
					//quantité de pheromone on choisi l'un des 2
					//en basant sur rand:
					//si il donne 1 on va choisi le deuxieme arc
					//sinon on prend le premier
					srand(time(NULL));
					if(rand()%2) ele2 = ele3;
				}else if(phero1<phero2){
					ele2 = ele3;
				}
			}
			
			eleSommetArc = eleSommetArc->next;
		}
		lastElement = getLast(path);
		addPath(&path, ele2->point);
		ele1 = ele2;
	}while(validePath(path, nest, food)==0 && countLenghPath(path)<100);
	ant->path = path;
	ant->actualPosition = path;
	ant->lenghPath = countLenghPath(path);
	return ant;
}

//la validation de chemin
int validePath(Path *path, Point *nest, Point *food){
	if(comparePoint(path->point, nest) && comparePoint(getLast(path)->point, nest) && isExistPoint(path, food)) return 1;
	return 0;
}

//la generetion de chemin aliatoire
Ant *generateRandomPath(Point *nest, Point *food){
  Point *next;
  int choix;
  Path *aux;
  Ant *ant;

  ant = createAnt(nest) ;
  aux = ant->path;
  next = NULL;

  do{
    do{//ici on va chercher la nouvelle direction 
      //celon une des 8 direction possible
      //(6) (7) (8)
      //   \ | /
      //(5)-(*)-(1)
      //   / | \
      //(4) (3) (2)
      //(*) est la point actuel 
      //au debut la point actuel c'est le nid
      free(next);
      choix = getRandNumber(9);//ici on va choisi une des directions
      next = getNextPoint(choix, getLast(ant->path)->point);//creation de le prochain point celon la direction 
    }while(isRightDerection(next, 4, 5)==0 || comparePoint(aux->point, next));//ici on valide si le prochain point
                                        //n'est pas hors le plan
                                        //et varifier de pas tember sur le vas 
                                        //et le viens
    aux = getLast(ant->path);
    addPathAnt(&ant, next);
    next = NULL;
  }while(validePath(ant->path, nest, food)==0);//ici on verifie si le chemin contient la position de nouriture 
                      // en plus le debut et la fin n'est que le nid
  return ant;
}

//tester si toute les fourmis du tableau de foumis
//ont fini ses tours
int isEnd(Ant **tabAnt, int nbr){
	int i;
	for(i=0; i<nbr; i++){
		if(tabAnt[i]->actualPosition != NULL) return 0;
	}
	return 1;
}

//pour supprimer les cycles qui trouvent dans les chemins
void deleteCyclePath(Ant *ant, Point *nest, Point *food){
	Path *element, *aux, *delete, *aux2;

	aux = element = ant->path->next;
	//pour ecraser les cycle il faut:
	//faire attention pour la grande cycle nest->..->food->..->nest
	//si une cycle contient food il faut l'ignorer
	//pour ecraser une cycle il suffit de supprimer tout les neoud
	//entre un meme point 
	while(element && comparePoint(element->point, food)==0){
		//pour cette boucle on essaye de supprimer les boucle 
		//de type nest->..->nest
		if(element && comparePoint(element->point, nest)){
			aux = ant->path;
			ant->path = element;
			while(aux->next!=ant->path){
				delete = aux;
				aux = aux->next;
				delete->next = NULL;
				free(delete);
				ant->lenghPath --;
			}
			aux->next = NULL;
			free(aux);
			ant->lenghPath--;
		}
		
		element = element->next;
	}
	
	aux2 = element;
	element = element->next;
	while(element->next && comparePoint(element->point, nest)==0){
		//pour cette boucle on essaye de supprimer les boucle 
		//de type food->..->food en laissant une seul food
		if(comparePoint(element->point, food)){
			while(aux2->next!=element){
				delete = aux2->next;
				aux2->next = delete->next;
				delete->next = NULL;
				free(delete);
				ant->lenghPath --;
			}
			aux2->next = element->next;
			delete = element;
			free(delete);
			ant->lenghPath--;
			element = aux2->next;
		}
		element = element->next;
	}

	//la suppression des cycles qui ce trouve entre
	//nest et food
	element = ant->path;
	while(comparePoint(element->point, food)==0){
		aux = element->next;
		while(comparePoint(aux->point, food)==0){
			if(comparePoint(element->point, aux->point)) {
				
				while(element->next!=aux){
					delete = element->next;
					element->next = delete->next;
					delete->next = NULL;
					free(delete);
				}
				element->next = aux->next;
				element = aux;
			}
			aux = aux->next;
		}
		element = element->next;
	}

	//la suppresion tous les cycles qui se trouve
	//entre food et nest
	while(element->next){
		aux = element->next;
		while(aux->next && comparePoint(aux->point, nest)==0){
			if(comparePoint(element->point, aux->point)){
				while(element->next!=aux){
					delete = element->next;
					element->next = delete->next;
					delete->next = NULL;
					free(delete);
				}
				element->next = aux->next;
				element = aux;
			}
			aux = aux->next;
		}
		element = element->next;
	}
	ant->lenghPath = countLenghPath(ant->path);
	ant->actualPosition = ant->path;
}

//ecriture un chemin dans un fichier
//pour par la suite l'appele dans python
void writePathFile(Path *path){
	FILE *f;
	f = fopen("resultatFourmi1.txt", "a");
	while(path){
		fprintf(f, "%d-%d", path->point->y, path->point->x);
		if(path->next) fprintf(f, ",");
		path = path->next;
	}
	fprintf(f, "\n");
	fclose(f);
	free(f);
}