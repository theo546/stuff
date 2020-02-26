# coding: iso-8859-15

"""

alors les putain de libraries c'est tweepy voila abonne toi
sinon pour installer les putain de libraries c'est sudo pip install tweepy

et pour faire en sorte que le putain de script se lance au démarrage d'un terminal faut
éditer le putain de fichier .bashrc au root du dossier home de l'user courant
et mettre "python3 /lien/vers/paulok.py"

pis faut créer une app sur https://apps.twitter.com/app lol

bien cordialement, la direction

"""

# On importe les libraries.
import tweepy, random

# On met les truc hyper secret ici.
consumer_token, consumer_secret = "", ""
access_key, access_secret = "", ""

# Ici, le script va tenter de se connecter a Twitter, si il n'y arrive pas il se coupe.
try:
	auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	stuff = api.user_timeline(screen_name = 'PaulokHF', count = 200, include_rts = True, tweet_mode="extended")
	tweets = [[tweet.full_text] for tweet in stuff]
except: quit()

# La loop ici va chercher un tweet random, regarde son contenue et regarde s'il y a un lien d'image, une mention ou un lien YouTube, si oui, la loop se relance afin de trouver ze tweet parfait.
while True:
	superrandomdetesmort = random.randint(0, 200)
	text = tweets[superrandomdetesmort]
	if "t.co" in text[0] or "@" in text[0] or "youtu.be" in text[0]: continue
	else: break

# Ça vous imprime le message sur l'imprimante la plus proche comme print ça veux dire imprimer mdr
print(text[0])