import cherrypy

class MonSiteWeb(object): # Classe maîtresse de l’application
    def index(self): # Méthode invoquée comme URL racine (/)
        return "<h1>Bonjour à tous !</h1>"
    index.exposed = True # la méthode doit être ‘publiée’
###### Programme principal : #############
cherrypy.quickstart(MonSiteWeb(), config ="tutoriel.conf")
