/*creation de base de donnée*/
CREATE DATABASE location
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

/*creation T_Societe*/

create table  IF NOT EXISTS T_Societe  (code_societe Integer not null ,
										nom_societe character varying(10) not null,
										adrs character varying(50) not null,
										tel character varying(13) not null,
										fax character varying(13) not null,
										email character varying(30) not null,
										util_T_Societe character varying(50) not null,
										flag_T_Societe character varying(10) not null,
										remarque_T_Societe character varying(50) not null,
										PRIMARY KEY (code_societe)
) ;

/*creation T_Unite*/

create table  IF NOT EXISTS T_UNITE  (code_unite Integer not null ,
									  libelle_unite character varying(50) not null,
									  remu character varying(50) not null,
									  flag character varying(3) not null,
									  util_T_UNITE character varying(50) not null,
									  flag_T_UNITE character varying(10) not null,
									  remarque_T_UNITE character varying(50) not null,
									  PRIMARY KEY (code_unite)
) ;

/*creation T_FRNS*/

create table  IF NOT EXISTS T_FRNS  (code_frnsi Integer not null ,
									 nom_frns character varying(40) not null,
									 code_centre_rc Integer not null ,
									 code_ice character varying(50) not null,
									 regc character varying(15) not null,
									 tel character varying(50) not null,
									 fax character varying(50) not null,
									 Date_deb DATE,adrs1 character varying(50) not null,
									 rmq1 character varying(80) not null,
									 util_T_FRNS character varying(50) not null,
									 flag_T_FRNS character varying(10) not null,
									 remarque_T_FRNS character varying(50) not null,
									 PRIMARY KEY (code_frnsi)
) ;

/*creation T_Couleur*/

create table  IF NOT EXISTS T_couleur  (code_couleur Integer not null ,
										libelle_couleur character varying(50) not null,
										remu character varying(50) not null,
										flag character varying(3) not null,
										util_T_couleur character varying(50) not null,
										flag_T_couleur character varying(10) not null,
										remarque_T_couleur character varying(50) not null,
										PRIMARY KEY (code_couleur)
) ;

/*creation T_Marque*/

create table  IF NOT EXISTS T_marque  (code_marque Integer not null ,
									   libelle_marque character varying(50) not null,
									   remu character varying(50) not null,
									   flag character varying(3) not null,
									   util_T_marque character varying(50) not null,
									   flag_T_marque character varying(10) not null,
									   remarque_T_marque character varying(50) not null,
									   PRIMARY KEY (code_marque)
) ;

/*creation T_type_action*/

create table  IF NOT EXISTS T_type_action  (code_type_action Integer not null ,
											libelle_type_action character varying(50) not null,
											util_T_type_action character varying(50) not null,
											flag_T_type_action character varying(10) not null,
											remarque_T_type_action character varying(50) not null,
											PRIMARY KEY (code_type_action)
) ;

/*creation T_Agence*/

create table  IF NOT EXISTS T_Agence  (code_agence Integer not null ,
									   nom_agence character varying(20) not null,
									   adresse character varying(30) not null,
									   code_societe Integer not null ,
									   tel character varying(13) not null,
									   fax character varying(13) not null,
									   horaire_ouverture DATE,
									   nom_responsable character varying(15) not null,
									   email character varying(20) not null,
									   util_T_Agence character varying(50) not null,
									   flag_T_Agence character varying(10) not null,
									   remarque_T_Agence character varying(50) not null,
									   PRIMARY KEY (code_agence),
									   FOREIGN KEY (code_societe) REFERENCES T_Societe(code_societe)
) ;

/*creation T_Produit*/

create table  IF NOT EXISTS T_PRODUITS  (code_produit Integer not null ,
										 Nom_produit character varying(80) not null,
										 code_famille Integer not null ,
										 code_unite Integer not null ,
										 Prx_uni real  not null,
										 Indisponible character varying(50) not null,
										 flag character varying(10) not null,
										 code_societe Integer not null ,
										 remarque character varying(50) not null,
										 util_T_PRODUITS character varying(50) not null,
										 flag_T_PRODUITS character varying(10) not null,
										 remarque_T_PRODUITS character varying(50) not null,
										 PRIMARY KEY (code_produit),
										 FOREIGN KEY (code_unite) REFERENCES T_UNITE(code_unite),
										 FOREIGN KEY (code_societe) REFERENCES T_Societe(code_societe)
) ;


/*creation T_Vehicule*/

create table  IF NOT EXISTS T_Vehicule  (code_vehicule Integer not null ,
										 matricule character varying(10) not null,
										 matricule_www character varying(10) not null,
										 date_mise_en_service DATE,
										 nbr_de_cheveaux Integer not null ,
										 pu_location real  not null,
										 code_couleur Integer not null ,
										 type character varying(10) not null,
										 code_marque Integer not null ,
										 remarque character varying(50) not null,
										 kilometrage real  not null,
										 categorie character varying(30) not null,
										 nbr_passagers Integer not null ,
										 nbr_portes Integer not null ,
										 nombre_valises Integer not null ,
										 boite_vitesse character varying(1) not null,
										 climatisation character varying(1) not null,
										 code_agence Integer not null ,
										 util_T_Vehicule character varying(50) not null,
										 flag_T_Vehicule character varying(10) not null,
										 remarque_T_Vehicule character varying(50) not null,
										 PRIMARY KEY (code_vehicule),
										 FOREIGN KEY (code_agence) REFERENCES T_Agence(code_agence),
										 FOREIGN KEY (code_couleur) REFERENCES T_Couleur(code_couleur),
										 FOREIGN KEY (code_marque) REFERENCES T_Marque(code_marque)
) ;


/*creation T_Client*/

create table  IF NOT EXISTS T_Client  (code_client Integer not null ,
									   nom_client character varying(8) not null,
									   prenom_client character varying(8) not null,
									   code_ice character varying(30) not null,
									   code_agence Integer not null ,
									   cin_passeport character varying(20) not null,
									   adresse character varying(30) not null,
									   code_postal Integer not null ,
									   ville character varying(10) not null,
									   tel character varying(13) not null,
									   gsm character varying(80) not null,
									   email character varying(13) not null,
									   util_T_Client character varying(50) not null,
									   flag_T_Client character varying(10) not null,
									   remarque_T_Client character varying(50) not null,
									   PRIMARY KEY (code_client),
									   FOREIGN KEY (code_agence) REFERENCES T_Agence(code_agence)
) ;

/*creation du table H_Reservation*/

create table  IF NOT EXISTS H_Reservation  (code_reservation Integer not null,
											info_reservation character varying(50) not null,
											code_client Integer not null ,
											code_vehicule Integer not null ,
											code_agence Integer not null ,
											date_reservation DATE,
											date_depart DATE,
											date_arrive DATE,
											code_paiement Integer not null ,
											code_type_reservation Integer not null ,
											util_T_Reservation character varying(50) not null,
											flag_T_Reservation character varying(10) not null,
											remarque_T_Reservation character varying(50) not null,
											PRIMARY KEY (code_reservation),
											FOREIGN KEY (code_client) REFERENCES T_Client(code_client),
											FOREIGN KEY (code_vehicule) REFERENCES T_Vehicule(code_vehicule),
											FOREIGN KEY (code_agence) REFERENCES T_Agence(code_agence)

);

/*creation de table H_Contrat*/

create table  IF NOT EXISTS H_Contrat  (code_contrat Integer not null,
										terme_contrat character varying(80) not null,
										code_reservation Integer not null ,
										date_creation DATE,date_depart DATE,
										date_arrive DATE,
										code_client Integer not null ,
										code_agence Integer not null ,
										montant_pu_location real  not null,
										nbr_jours Integer not null ,
										montant_total real  not null,
										util_H_Contrat character varying(50) not null,
										flag_H_Contrat character varying(10) not null,
										remarque_H_Contrat character varying(50) not null,
										PRIMARY KEY (code_contrat),
										FOREIGN KEY (code_client) REFERENCES T_Client(code_client),
										FOREIGN KEY (code_agence) REFERENCES T_Agence(code_agence),
										FOREIGN KEY (code_reservation) REFERENCES H_Reservation(code_reservation)
);

/*creation du table G_Assurance*/
create table  IF NOT EXISTS H_Assurance  (code_H_Assurance Integer not null, 
										  info_H_Assurance character varying(30) not null,
										  code_vehicule Integer not null ,
										  montant_H_Assurance real  not null,
										  date_creation DATE,
										  date_debut DATE,
										  date_fin DATE,
										  code_agence Integer not null ,
										  util_H_Assurance character varying(50) not null,
										  flag_H_Assurance character varying(10) not null,
										  remarque_H_Assurance character varying(50) not null,
										  PRIMARY KEY (code_H_Assurance),
										  FOREIGN KEY (code_vehicule) REFERENCES T_Vehicule(code_vehicule),
										  FOREIGN KEY (code_agence) REFERENCES T_Agence(code_agence)
										  );

/*creation du table H_Viste_av*/

create table  IF NOT EXISTS H_visite_av  (code_visite_av Integer not null,
										  terme_visite_av character varying(80) not null,
										  code_reservation Integer not null ,
										  date_creation DATE,
										  code_agence Integer not null ,
										  util_H_visite_av character varying(50) not null,
										  flag_H_visite_av character varying(10) not null,
										  remarque_H_visite_av character varying(50) not null,
										  PRIMARY KEY (code_visite_av),
										  FOREIGN KEY (code_agence) REFERENCES T_Agence(code_agence),
										  FOREIGN KEY (code_reservation) REFERENCES H_Reservation(code_reservation)
);

/*creation du table H_Visite_ap*/

create table  IF NOT EXISTS H_visite_ap  (code_visite_ap Integer not null,
										  terme_visite_ap character varying(80) not null,
										  code_reservation Integer not null ,
										  date_creation DATE,
										  code_agence Integer not null ,
										  util_H_visite_ap character varying(50) not null,
										  flag_H_visite_ap character varying(10) not null,
										  remarque_H_visite_ap character varying(50) not null,
										  PRIMARY KEY (code_visite_ap),
										  FOREIGN KEY (code_agence) REFERENCES T_Agence(code_agence),
										  FOREIGN KEY (code_reservation) REFERENCES H_Reservation(code_reservation)
);

/*creation du table H_Reglement*/

create table  IF NOT EXISTS H_reglement  (code_reglement Integer not null ,
										  terme_reglement character varying(80) not null,
										  code_contrat Integer not null ,
										  date_creation DATE,
										  code_client Integer not null ,
										  code_agence Integer not null ,
										  montant_pu_location real  not null,
										  nbr_jours Integer not null ,
										  montant_total real  not null,
										  util_H_reglement character varying(50) not null,
										  flag_H_reglement character varying(10) not null,
										  remarque_H_reglement character varying(50) not null,
										  PRIMARY KEY (code_reglement),
										  FOREIGN KEY (code_client) REFERENCES T_Client(code_client),
										  FOREIGN KEY (code_agence) REFERENCES T_Agence(code_agence),
										  FOREIGN KEY (code_contrat) REFERENCES H_Contrat(code_contrat)
);

/*creation du table ENT_cmd*/

create table  IF NOT EXISTS ENT_cmd  (code_cmd Integer not null ,
									  refmarche character varying(20) not null,
									  code_frnsi Integer not null ,
									  code_societe Integer not null ,
									  date_cmd DATE,
									  flag character varying(10) not null,
									  remarques character varying(50) not null,
									  util_ENT_cmd character varying(50) not null,
									  flag_ENT_cmd character varying(10) not null,
									  remarque_ENT_cmd character varying(50) not null,
									  PRIMARY KEY (code_cmd),
									  FOREIGN KEY (code_frnsi) REFERENCES T_FRNS(code_frnsi),
									  FOREIGN KEY (code_societe) REFERENCES T_Societe(code_societe)
) ;

/*creation du table DET_cmd*/

create table  IF NOT EXISTS DET_cmd  (ld_cmd Integer not null ,
									  code_produit Integer not null ,
									  Quantitedemd Integer not null ,
									  prix_unitaire real  not null,
									  dat_liv_souhaitee DATE,
									  code_unite Integer not null ,
									  prix_global real  not null,
									  remarq character varying(50) not null,
									  util_DET_cmd character varying(50) not null,
									  flag_DET_cmd character varying(10) not null,
									  remarque_DET_cmd character varying(50) not null,
									  FK_cmd Integer not null ,
									  PRIMARY KEY (ld_cmd,FK_cmd),
									  FOREIGN KEY (FK_cmd) REFERENCES ENT_cmd (code_cmd),
									  FOREIGN KEY (code_produit) REFERENCES T_PRODUITS(code_produit),
									  FOREIGN KEY (code_unite) REFERENCES T_UNITE(code_unite)
) ;

/*creation H_Action*/

create table  IF NOT EXISTS H_Action  (code_H_Action Integer not null ,
									   info_H_Action character varying(30) not null,
									   code_frnsi Integer not null ,
									   code_vehicule Integer not null ,
									   code_type_action Integer not null ,
									   montant_H_Action real  not null,
									   date_creation DATE,date_debut DATE,
									   date_fin DATE,
									   code_agence Integer not null ,
									   util_H_Action character varying(50) not null,
									   flag_H_Action character varying(10) not null,
									   remarque_H_Action character varying(50) not null,
									   PRIMARY KEY (code_H_Action),
									   FOREIGN KEY (code_vehicule) REFERENCES T_Vehicule(code_vehicule),
									   FOREIGN KEY (code_agence) REFERENCES T_Agence(code_agence),
									   FOREIGN KEY (code_frnsi) REFERENCES T_FRNS(code_frnsi),
									   FOREIGN KEY (code_type_action) REFERENCES T_type_action(code_type_action)

) ;

/*creation T_Option*/

create table  IF NOT EXISTS T_Option  (code_option Integer not null ,
									   nom_option character varying(10) not null,
									   unite character varying(10) not null,
									   prix real  not null,
									   util_T_Option character varying(50) not null,
									   flag_T_Option character varying(10) not null,
									   remarque_T_Option character varying(50) not null,
									   PRIMARY KEY (code_option)
) ;

/*creation T_Assurance*/

create table  IF NOT EXISTS T_Assurance  (code_assurance Integer not null ,
										  nom_assurance character varying(10) not null,
										  nite character varying(10) not null,
										  prix real  not null,
										  util_T_Assurance character varying(50) not null,
										  flag_T_Assurance character varying(10) not null,
										  remarque_T_Assurance character varying(50) not null,
										  PRIMARY KEY (code_assurance)
) ;

/*creation H_Option*/

create table  IF NOT EXISTS H_Option  (code_H_option Integer not null ,
									   info_H_Option character varying(80) not null,
									   code_option Integer not null ,
									   code_reservation Integer not null ,
									   util_H_Option character varying(50) not null,
									   flag_H_Option character varying(10) not null,
									   remarque_H_Option character varying(50) not null,
									   PRIMARY KEY (code_H_option,code_reservation),
									   FOREIGN KEY (code_option) REFERENCES T_Option(code_option),
									   FOREIGN KEY (code_reservation) REFERENCES H_Reservation(code_reservation)
) ;

/*creation T_Type_Client*/

create table  IF NOT EXISTS T_type_client  (code_type_client Integer not null ,
											libelle_type_client character varying(50) not null,
											util_T_type_client character varying(50) not null,
											flag_T_type_client character varying(10) not null,
											remarque_T_type_client character varying(50) not null,
											PRIMARY KEY (code_type_client)
) ;

