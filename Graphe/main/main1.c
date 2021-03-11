#include "graphe.h"
#include "ant.h"

int main(){
	Graphe *graphe;
	Point *nest, *food;
	Ant *ant1, *ant2, *ant3;

	Path *fromPosAnt1, *toPosAnt1, *fromPosAnt2, *toPosAnt2;

	graphe = initGraphe(4, 5);//initialisation du graphe avec tous les sommets et les arcs qui faut
	nest = createPoint(3, 1);//le nid
	food = createPoint(4, 5);//la nourriture

	//creation des fourmies
	ant1 = createAnt(nest);
	ant2 = createAnt(nest);
	ant3 = createAnt(nest);

	//initialisation des chemins des deux fourmies
	//pour la fourmie 1
	addPathAnt(&ant1,createPoint(2, 2));
	addPathAnt(&ant1,createPoint(2, 3));
	addPathAnt(&ant1,createPoint(2, 4));
	addPathAnt(&ant1,createPoint(2, 5));
	addPathAnt(&ant1,createPoint(3, 5));
	addPathAnt(&ant1,createPoint(4, 5));
	addPathAnt(&ant1,createPoint(4, 4));
	addPathAnt(&ant1,createPoint(4, 3));
	addPathAnt(&ant1,createPoint(4, 2));
	addPathAnt(&ant1,nest);

	//pour la fourmie 2
	addPathAnt(&ant2,createPoint(3, 2));
	addPathAnt(&ant2,createPoint(3, 3));
	addPathAnt(&ant2,createPoint(3, 4));
	addPathAnt(&ant2,createPoint(4, 5));
	addPathAnt(&ant2,createPoint(4, 4));
	addPathAnt(&ant2,createPoint(4, 3));
	addPathAnt(&ant2,createPoint(3, 2));
	addPathAnt(&ant2,nest);
	
	//la boucle de parcour des deux fourmies
	//pour le parcour chaque fois une fourmie va deplacer de pos1 vers pos2
	//elle va depose une quantité de pheromone dans l'arc (pos1, pos2)
	//qu'elle s'acumule au cour de la tour de chaque fourmie
	while(ant1->actualPosition || ant2->actualPosition){
		if(ant1->actualPosition){//la fourmie 1 va se deplacer de postion 1 vers la position 2
			fromPosAnt1 = ant1->actualPosition;//la position 1
			takeStep(&ant1);
			toPosAnt1 = ant1->actualPosition;//la position 2
		}
		if(ant2->actualPosition){//la meme chose pour la fourmie 2 de pos 1 vers pos 2
			fromPosAnt2 = ant2->actualPosition;//pos 1
			takeStep(&ant2);
			toPosAnt2 = ant2->actualPosition;//pos 2
		}
		//la maj de la quantité de pheromone acumul& de position 1 vers la position 2 pour les deux fourmies
		if(ant1->actualPosition) updateAcumulePhero(&graphe, fromPosAnt1->point, toPosAnt1->point, 1.0/ant1->lenghPath);
		if(ant2->actualPosition) updateAcumulePhero(&graphe, fromPosAnt2->point, toPosAnt2->point, 1.0/ant2->lenghPath);
	}
	//la maj de quantité de pheromone actual dans les arcs du graphe
	updatePhero(&graphe);

	ant3 = generatePath(graphe, nest);
	printf("le chemin obtimale est: \n");
	displayPath(ant3->path);

  	return 0;
}
