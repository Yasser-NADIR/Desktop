from views import *

root   = Tk()
root.option_add("*tearOff",False)
root.state("zoomed")
#root.iconbitmap("icon.ico")

menu = Menu(root)
root.configure(menu=menu)
creation = frame_creation(root)

#pour fournisseur
R_AchatsFourniseurNomLabel = ["code Fournisseur","nom fournisseur","code Fournisseur","registre de commerce","telephone","fax","c correspondance","site web","email","fichier","adresse banque","compte b","adresse Fournisseur","adresse","adresse1","Remarque1","Remarque2","flag"]
R_AchatsFourniseurDBField = ["code_Fournisseuri","nom_Fournisseur","code_Fournisseur","regc","tel","fax","c_corresp","siteweb","email","fichier","adresse_banque","compte_b","adrs1","adrs2","adrs3","rmq1","rmq2","flag"]
R_AchatsFourniseurForms = frame(root,args=R_AchatsFourniseurNomLabel,db="b_frns",dbField=R_AchatsFourniseurDBField,text="b_frns")
R_AchatsFourniseurOptionsListe = ["/","+","?","*","-","|<<",">>|","<<",">>","T","E","/\\"]
R_AchatsFourniseurCommandsListe = [R_AchatsFourniseurForms.Nouveau,R_AchatsFourniseurForms.Valider,R_AchatsFourniseurForms.Rechercher,R_AchatsFourniseurForms.Modifier,R_AchatsFourniseurForms.Supprimer,R_AchatsFourniseurForms.PremierEnre,R_AchatsFourniseurForms.DernierEnre,R_AchatsFourniseurForms.Arrier,R_AchatsFourniseurForms.Avant,R_AchatsFourniseurForms.AfficherTous,R_AchatsFourniseurForms.Imprimer,R_AchatsFourniseurForms.Quitter]
R_AchatsFourniseurOptions = frame_option(root,options=R_AchatsFourniseurOptionsListe,text="Option",commands=R_AchatsFourniseurCommandsListe)

def displayFournisseur():
	for f in root.winfo_children():
		f.pack_forget()
	R_AchatsFourniseurOptions.display()
	R_AchatsFourniseurForms.display()

#pour unite
R_AchatsUniteNomLabel = ["code Unite","libelle Unite","remu","flag"]
R_AchatsUniteNomDBField = ["code_un","lib_un","remu","flag"]
R_AchatsUniteForms = frame(root,args=R_AchatsUniteNomLabel,db="unite",dbField=R_AchatsUniteNomDBField,text="unite")
R_AchatsUniteOptionsListe = ["/","+","?","*","-","|<<",">>|","<<",">>","T","E","/\\"]
R_AchatsUniteCommandsListe = [R_AchatsUniteForms.Nouveau,R_AchatsUniteForms.Valider,R_AchatsUniteForms.Rechercher,R_AchatsUniteForms.Modifier,R_AchatsUniteForms.Supprimer,R_AchatsUniteForms.PremierEnre,R_AchatsUniteForms.DernierEnre,R_AchatsUniteForms.Arrier,R_AchatsUniteForms.Avant,R_AchatsUniteForms.AfficherTous,R_AchatsUniteForms.Imprimer,R_AchatsUniteForms.Quitter]
R_AchatsUniteOptions = frame_option(root,options=R_AchatsUniteOptionsListe,text="Option",commands=R_AchatsUniteCommandsListe)

def displayUnite():
	for f in root.winfo_children():
		f.pack_forget()
	R_AchatsUniteOptions.display()
	R_AchatsUniteForms.display()
"""
#pour famille produit
R_AchatsFamilleproduitNomLabel = ["code famille","code famille d","famille","remarque","flag"]
R_AchatsFamilleproduitForms = frame_fournisseur(root,args=R_AchatsFamilleproduitNomLabel,text="familleprd")
R_AchatsFamilleproduitOptionsListe = ["/","+","?","*","-","|<<",">>|","<<",">>","T","E","/\\"]
#R_AchatsFamilleproduitOptions = frame_option(root,options=R_AchatsFamilleproduitOptionsListe,text="Option")

def displayFamilleproduit():
	for f in root.winfo_children():
		f.pack_forget()
	R_AchatsFamilleproduitOptions.display()
	R_AchatsFamilleproduitForms.display()
	
#pour produit
R_AchatsProduitNomLabel = ["Refproduit","Nom produit","code famille","prix unitaire","indisponible","status","remarque","flag"]
R_AchatsProduitForms = frame_fournisseur(root,args=R_AchatsProduitNomLabel,text="produit")
R_AchatsProduitOptionsListe = ["/","+","?","*","-","|<<",">>|","<<",">>","T","E","/\\"]
#R_AchatsProduitOptions = frame_option(root,options=R_AchatsProduitOptionsListe,text="Option")
#mise a jour a propos du code famille 
R_AchatsProduitForms.liste_form[2].entre = ttk.Combobox(R_AchatsProduitForms.liste_form[2])

def displayProduit():
	for f in root.winfo_children():
		f.pack_forget()
	R_AchatsProduitOptions.display()
	R_AchatsProduitForms.display()

#pour catalogue fornisseur
R_AchatsCatalogueFournisseurNomLabel = ["RefproduitFournisseu","Nom produitFournisseur","Reference produit","code fournisseur","quantite minimum","prix unitaire","code tva","code rrr","delai approvisionnement","indisponible","remarque","flag"]
R_AchatsCatalogueFournisseurForms = frame_fournisseur(root,args=R_AchatsCatalogueFournisseurNomLabel,text="produit")
R_AchatsCatalogueFournisseurOptionsListe = ["/","+","?","*","-","|<<",">>|","<<",">>","T","E","/\\"]
#R_AchatsCatalogueFournisseurOptions = frame_option(root,options=R_AchatsCatalogueFournisseurOptionsListe,text="Option")
#mise a jour a propos du code famille 
R_AchatsCatalogueFournisseurForms.liste_form[2].entre = ttk.Combobox(R_AchatsCatalogueFournisseurForms.liste_form[2])
R_AchatsCatalogueFournisseurForms.liste_form[3].entre = ttk.Combobox(R_AchatsCatalogueFournisseurForms.liste_form[3])

def displayCatalogueFournisseur():
	for f in root.winfo_children():
		f.pack_forget()
	R_AchatsCatalogueFournisseurOptions.display()
	R_AchatsCatalogueFournisseurForms.display()"""

#pour getionnaire de commande
R_AchatsGestionCommandeEnteteNomLabel = ["Numero de commande","code societe","numero devis","code fournisseur","date comande","date fournisseur2","date livraison","reference marche","destinataire","adresse livraison","ville livraison","status","remarque"]
R_AchatsGestionCommandeEnteteDBField = ["Ncommande","code_societe","ndevis","code_fournisseuri","Date_commande","code_fournisseur","date_livraison","code_marchei","Destinataire","Adresse_livraison","Ville_livraison","code_sts","remarque"] 
R_AchatsGestionCommandeEnteteChange = {3:(ttk.Combobox,["1","2","3"]),5:(ttk.Combobox,["1","2","3"])}
R_AchatsGestionCommandeEnteteForms = frame_ameliorer(root,args=R_AchatsGestionCommandeEnteteNomLabel,db="ent_cmd",dbField=R_AchatsGestionCommandeEnteteDBField,changes=R_AchatsGestionCommandeEnteteChange,text="entete")

R_AchatsGestionCommandeDetailNomLabel = ["N commande","N commandel","reference produit","quantite commandee","code unite","prix unitaire","prix total","date livraison souhaite","Statusd","remarque"]
R_AchatsGestionCommandeDetailChange = {2:(ttk.Combobox,["1","2","3"]),4:((ttk.Combobox,["1","2","3"]))}
R_AchatsGestionCommandeDetailForms = frame_details(root,args=R_AchatsGestionCommandeDetailNomLabel,changes=R_AchatsGestionCommandeDetailChange,text="detail")


def displayDetailCommande():
	for f in root.winfo_children():
		f.pack_forget()
	R_AchatsGestionCommandeDetailOptions.display()
	R_AchatsGestionCommandeDetailForms.display()

R_AchatsGestionCommandeEnteteOptionsListe = ["/","+","?","*","-","|<<",">>|","<<",">>","T","E","/\\","D"]
R_AchatsGestionCommandeEnteteCommandesListe = [R_AchatsGestionCommandeEnteteForms.Nouveau,R_AchatsGestionCommandeEnteteForms.Valider,R_AchatsGestionCommandeEnteteForms.Rechercher,R_AchatsGestionCommandeEnteteForms.Modifier,R_AchatsGestionCommandeEnteteForms.Supprimer,R_AchatsGestionCommandeEnteteForms.PremierEnre,R_AchatsGestionCommandeEnteteForms.DernierEnre,R_AchatsGestionCommandeEnteteForms.Arrier,R_AchatsGestionCommandeEnteteForms.Avant,R_AchatsGestionCommandeEnteteForms.AfficherTous,R_AchatsGestionCommandeEnteteForms.Imprimer,R_AchatsGestionCommandeEnteteForms.Quitter,displayDetailCommande]
R_AchatsGestionCommandeEnteteOptions = frame_option(root,options=R_AchatsGestionCommandeEnteteOptionsListe,commands=R_AchatsGestionCommandeEnteteCommandesListe,text="Option")



def displayGestionCommande():
	for f in root.winfo_children():
		f.pack_forget()
	R_AchatsGestionCommandeEnteteOptions.display()
	R_AchatsGestionCommandeEnteteForms.display()

R_AchatsGestionCommandeDetailOprionsListe = ["+","*","-","E"]
R_AchatsGestionCommandeDetailCommandesListe = [R_AchatsGestionCommandeDetailForms.ajouter,None,None,displayGestionCommande]
R_AchatsGestionCommandeDetailOptions = frame_option(root,options=R_AchatsGestionCommandeDetailOprionsListe,commands=R_AchatsGestionCommandeDetailCommandesListe,text="option")



R_Achats     = Menu(menu)
E_Achats     = Menu(menu)
Informatique = Menu(menu)

liste_R_Achats_Nom = ["Fournisseurs"        ,"Unite"     ,"Status","Famille Produit"    ,"Produits"   ,"Catalogue Fournisseur","Gestion de commande"]
liste_R_Achats_Command = [displayFournisseur,displayUnite,None    ,None,None,None,displayGestionCommande]

for i in range(len(liste_R_Achats_Nom)):
	R_Achats.add_command(label=liste_R_Achats_Nom[i],command=liste_R_Achats_Command[i])

menu.add_command(label="creation",command=creation.display)
menu.add_cascade(menu=R_Achats,label="R_Achats")
menu.add_cascade(menu=E_Achats,label="E_Achats")
menu.add_cascade(menu=Informatique,label="Informatique")


root.mainloop()