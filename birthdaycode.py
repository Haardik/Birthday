import facebook
import requests

TOKEN = "CAACEdEose0cBAKWXoeR1lE6HLoR05P3JZBjAjBUMfPsxsp6UckjU05IyIbFXP5TMajVhFV9emMllRFN4B0Yc4g9mGi6zjhIW1ZClHDuDdSbQ9VTCOpDOQ9GXIuttH2nZBVAfVZBAGaZA7olUolrJFAwDeOjfH9E8q7KZBizWHDD405SON9MWvAUikOSR8MicBZCteH5HNxR3AZDZD"
def get_wishes(url):
	'''
		Returns the json formatted data of the Birthday Wishes 
	'''
	global TOKEN
	parameters = {'access_token': TOKEN}
	print ("url")
	print ("parameters")
	posts = requests.get(url, params = parameters)
	return posts.json()

def post_like_and_comment(post_id):
	'''
		Automatically liking and commenting on the Posts ;) 
	'''
	global TOKEN
	MESSAGE = "Your wishes were all that was needed, to make my birthday much more special. Thanks a lot! :)"
	parameters = {'access_token': TOKEN}
	requests.post("https://graph.facebook.com/%s/likes/" %(post_id), params = parameters)
	parameters = {'access_token': TOKEN, 'message': MESSAGE}
	requests.post("https://graph.facebook.com/%s/comments" %(post_id), data = parameters)

def main():
	'''
		Main Calling Method to invoke other methods
	'''
	LIMITS = str(123)
	# i = 1
	# wishes = get_wishes("https://graph.facebook.com/me?fields=feed.limit("+LIMITS+"){id,message}")
	# post_likes_and_comments(wishes['feed']['data'][0]['id'])
	for wish in wishes['feed']['data']:
		try:
			post_like_and_comment(wish['id'])
		except:
			print ("Error in POST ID: %s") %(wish['id'],)

if __name__=="__main__":
	main()
