import tweepy

ckey = "YFRciOp6noAoDzcDEGyr5OUT6"
csecret = "Hr9pmIr2gs6xVz5FEfuHhOMALt8EzykLwFBu9RQlna7AWSX3Oz"
atoken = "22205652-EBqkkUSToEUU3rob6HmoL0lA4FDoAD0biyyz2dhAM"
asecret = "G4AjMyExVCbXWysWms0ir40f8Tp5eJRKqsEfzyNq1gcwF"



auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)


api = tweepy.API(auth)
swtrains_profile = api.get_user("SW_Trains")
sw_trains_id = swtrains_profile.id
sw_trains_tweets =  api.user_timeline("SW_Trains",count=200)

i = 0;
apologies = 0;
tweets_list = []

while i < len(sw_trains_tweets):
	tweets_list.append(sw_trains_tweets[i].text.encode("utf8"))
	i+=1

for i in tweets_list:
	if "sorry" in i:
		apologies+=1

print "South West Trains have apologised %s times in their last 200 tweets" %apologies










#fetch current trends in London 
# api = tweepy.API(auth)
# london_trends =  api.trends_place("44418")[0]["trends"]
# for i in london_trends:
# 	print i["name"]