# coding: iso-8859-15

"""

alors les putain de libraries c'est tweepy voila abonne toi
sinon pour installer les putain de libraries c'est sudo pip install tweepy

et pour faire en sorte que le putain de script se lance au démarrage d'un terminal faut
éditer le putain de fichier .bashrc au root du dossier home de l'user courant
et mettre "python3.6 /lien/vers/paulok.py"

pis faut créer une app sur https://apps.twitter.com/app lol

bien cordialement, la direction

"""

import tweepy, random

consumer_token, consumer_secret = "", ""
access_key, access_secret = "", ""

try:
	auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	stuff = api.user_timeline(screen_name = 'PaulokHF', count = 200, include_rts = True, tweet_mode="extended")
	tweets = [[tweet.full_text] for tweet in stuff]
except: quit()

while True:
	superrandomdetesmort = random.randint(0, 200)
	text = str(tweets[superrandomdetesmort])
	if "t.co" in text or "@" in text or "youtu.be" in text: continue
	else: break

text = text.replace('\\n', '\n')
text = text.replace('["', '', 1)
text = text.replace('"]', '', 1)
text = text.replace("['", '', 1)
text = text.replace("']", '', 1)

print(text)
