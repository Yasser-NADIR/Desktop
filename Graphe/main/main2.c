#include "graphe.h"
#include "ant.h"

int main(){
	Graphe *graphe;
	Point *nest, *food;
	Ant **tabAnt, *ant;
	Path *fromPosAnt1, *toPosAnt1, *fromPosAnt2, *toPosAnt2;
	int nbrAnt, i;
	int *tabIntAnt;
	//tabIntAnt vont utiliser pour un protocole
	//de la mise à jour de la quantité de pheromone
	//alors on a testé la maj de pheromone après la boucle ça marce
	//mais hors de ce qui est demander
	//après on a testé la maj pour chaque mouvement
	//ça ne marche pas à cause des fourmie qui ont des chemin qui sont trop long
	//ces derniers plus ou moins diminue la quantité de pheromone des chemins des fourmies qui
	//ont un court chemin
	//ce protocol va maj la quantité de pheromone quand chaque fourmie fini sont tour
	//le protocole va consister sur les étapes suivantes
	//1- on initialise tous les cases par des 0
	//2- après qu'une fourmie d'indice i fini son tour on maj la contité de pheromone
	//et on change la case d'indice i par 1
	//==>si la case d'indice i dans le tableau tabIntAnt est 1
	//ça veut dire que la fourmie d'indice i deja fini son tour
	//dans une iteration precedante

	graphe = initGraphe(4, 5);//initialisation du graphe avec tous les sommets et les arcs qui faut
	nest = createPoint(3, 1);//le nid
	food = createPoint(4, 5);//la nourriture

	//creation des fourmies
	ant = createAnt(nest);

	//initialisation des chemins des nbrAnt de fourmies
	printf("Donnez le nombre des fourmies: ");
	scanf("%d", &nbrAnt);
	getchar();
	tabAnt = (Ant **)malloc(sizeof(Ant *)*nbrAnt);
	
	for(i=0; i<nbrAnt; i++){
		tabAnt[i] = generateRandomPath(nest, food);
		deleteCyclePath(tabAnt[i], nest, food);
		printf("le chemin N%d ( longueur: %d):\n", i+1, tabAnt[i]->lenghPath);
		displayPath(tabAnt[i]->path);
	}
	
	//initialisation de tabIntAnt
	tabIntAnt = (int *)malloc(sizeof(int)*nbrAnt);
	for(i=0; i<nbrAnt; i++) tabIntAnt[i] = 0;

	//la boucle de parcour des fourmies
	//pour le parcour chaque fois une fourmie va deplacer de pos1 vers pos2
	//elle va deposer une quantité de pheromone dans l'arc (pos1, pos2)
	//qu'elle s'acumule au cour de la tour de chaque fourmie
	
	while(isEnd(tabAnt, nbrAnt)==0){
		for(i=0; i<nbrAnt; i++){
			if(tabAnt[i]->actualPosition){//la fourmie 1 va se deplacer de postion 1 vers la position 2
				fromPosAnt1 = tabAnt[i]->actualPosition;//la position 1
				takeStep(&tabAnt[i]);
				toPosAnt1 = tabAnt[i]->actualPosition;//la position 2
			}
			if(tabAnt[i]->actualPosition) updateAcumulePhero(&graphe, fromPosAnt1->point, toPosAnt1->point, 1.0/tabAnt[i]->lenghPath);
			else if(tabIntAnt[i]==0){//après la fourmie i fini son tour
				//si la fourmie i fini son tour pour la premiere fois
				//la maj de quantité de pheromone actual dans les arcs du graphe
				printf("avant la mise a jour\n");
				updatePhero(&graphe);
				tabIntAnt[i] = 1;
				printf("une mise a jour est fait\n");
			} 
		}

		
	}
	printf("la fin du boucle et le debut de la recherche de chemin\n");
	Path *path;
	path = generatePath(graphe, nest, food);
	printf("le chemin optimale est: (longueur : %d)\n", countLenghPath(path));
	//displayPath(path);
  	return 0;
}
