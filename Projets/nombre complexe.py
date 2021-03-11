def creeer(a,b) :
    nbr_complexe = [a,b]
    return nbr_complexe

def afficher(nbr) :
    if(nbr[0]==0) :
        if(nbr[1]==0) :
            print("z = 0")
        else :
            if(nbr[1]>0) :
                print("z = i{}".format(nbr[1]))
            else :
                print("z = -i{}".format(-nbr[1]))
    else:
        if(nbr[1]==0):
            print("z = {}".format(nbr[0]))
        else:
            if(nbr[1]>0) :
                print("z = {}+i{}".format(nbr[0],nbr[1]))
            else :
                print("z = {}-i{}".format(nbr[0],-nbr[1]))
def somme(nbr1,nbr2):
    nbr = list
    nbr[0]=nbr1[0]+nbr2[0]
    nbr[1]=nbr1[1]+nbr2[1]
    return nbr
def difference(nbr1,nbr2):
    nbr = list
    nbr[0]=nbr1[0]-nbr2[0]
    nbr[1]=nbr1[1]-nbr2[1]
    return nbr
def produit(nbr1,nbr2):
    