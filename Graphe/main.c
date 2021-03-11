#include "graphe.h"
#include "ant.h"

int main(){
	Graphe *graphe;
	Point *nest, *food;
	Ant **tabAnt, **tabAntEclero, *antResultat, *aux;
	Path *fromPosAnt, *toPosAnt;
	int nbrAnt, i;

	graphe = initGraphe(4, 5);//initialisation du graphe avec tous les sommets et les arcs qu'il faut
	nest = createPoint(3, 1);//le nid
	food = createPoint(4, 5);//la nourriture

	//initialisation des chemins des nbrAnt fourmis
	printf("Donnez le nombre des fourmis: ");
	scanf("%d", &nbrAnt);
	getchar();
	tabAnt = (Ant **)malloc(sizeof(Ant *)*nbrAnt);
	for(i=0; i<nbrAnt; i++){
		printf("la creation du chemin libre du fourmi N%d\n", i+1);
		tabAnt[i] = generateRandomPath(nest, food);
		deleteCyclePath(tabAnt[i], nest, food);
		printf("pour la fourmi N%d le chemin :\n", i+1);
		displayPath(tabAnt[i]->path);
	}

	//les deux fourmis eclaireuses
	tabAntEclero = (Ant **)malloc(sizeof(Ant *)*2);
	for(i=0; i<2; i++){
		tabAntEclero[i] = generateRandomPath(nest, food);
		deleteCyclePath(tabAntEclero[i], nest, food);
	}

	//la boucle de parcour des fourmis
	//pour le parcour chaque fois une fourmi va deplacer de pos1 vers pos2
	//elle va deposer une quantité de pheromone dans l'arc (pos1, pos2)
	//qu'elle s'acumule au cour de la tour de chaque fourmie
	
	//on va commencer par deux fourmis ecrlaireuses
	while(isEnd(tabAntEclero, 2)==0){
		for(i=0; i<2; i++){
			if(tabAntEclero[i]->actualPosition){
				fromPosAnt = tabAntEclero[i]->actualPosition;
				takeStep(&tabAntEclero[i]);
				toPosAnt = tabAntEclero[i]->actualPosition;
				if(toPosAnt) updateAcumulePhero(&graphe, fromPosAnt->point, toPosAnt->point, 1.0/tabAntEclero[i]->lenghPath);
			}
		}
	}

	//la mise à jour de quantite de pheromone
	updatePhero(&graphe);
	//trouver le premier chemin dans le graphe
	antResultat = generatePath(graphe, nest, food);
	deleteCyclePath(antResultat, nest, food);

	//au cas ou il ne trouve pas le chemin il prend une chemin d'un des deux fourmis eclaireus
	if(countLenghPath(antResultat->path)>countLenghPath(tabAntEclero[0]->path)) antResultat = tabAntEclero[0];


	//dans cette boucle les fourmis qui ont des chemins libres
	//vont parcourir
	for(i=0; i<nbrAnt; i++){
		//le parcour de la fourmi numero i+1
		while(tabAnt[i]->actualPosition){
			fromPosAnt = tabAnt[i]->actualPosition;
			takeStep(&tabAnt[i]);
			toPosAnt = tabAnt[i]->actualPosition;
			if(toPosAnt) updateAcumulePhero(&graphe, fromPosAnt->point, toPosAnt->point, 1.0/tabAnt[i]->lenghPath);
		}
		//le mise à jour aprés le parcour
		updatePhero(&graphe);
		//le recherche de plus cour chemin
		aux = generatePath(graphe, nest, food);
		if(countLenghPath(aux->path)<100)deleteCyclePath(aux, nest, food);
		//si il ne trouve pas le chemin il prend le dernier trouver "antResultat"
		if(countLenghPath(aux->path)<countLenghPath(antResultat->path)) antResultat = aux;
	}

	
	//après la fin du boucle on aura le chemin optimal
	printf("le chemin optimal est:\n");
	displayPath(antResultat->path);

	FILE *f = fopen("resultatFourmi1.txt", "w");
	fprintf(f, "%d\n", nbrAnt);
	fclose(f);
	free(f);
	for(i=0; i<nbrAnt; i++){
		writePathFile(tabAnt[i]->path);
	}
	writePathFile(antResultat->path);
	system("python graphic.py");
  	return 0;
}
