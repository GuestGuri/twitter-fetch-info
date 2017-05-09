from re import findall
from sys import argv, exit
from urllib2 import urlopen



def fetch(twitter):
    """Fetch account information from a given Twitter profile"""
    try:
        data = urlopen(twitter).read()
        s = data.decode('utf-8')
        details = []
        [details.append(value) for value in findall('data-count=(.*?)\s', s)]
        following = details[1]
        name      = findall(b'<title>(.*?) \(', data)[0].decode('utf-8')
        tweets    = details[0]
        followers = details[2]
        likes     = details[3]
	#loc       = findall(b'<span class="ProfileHeaderCard-locationText u-dir" dir="ltr">(.*?)', data)[0].decode('utf-8')
        pic       = findall(b'href="https://pbs.twimg.com/profile_images(.*?)"', data)[0].decode('utf-8')
        date      = findall(b'<span class="ProfileHeaderCard-joinDateText js-tooltip u-dir" dir="ltr" title="(.*?)"', data)[0].decode('utf-8')
        print('''
        Name: {0}
        Tweets: {1}
        Following: {2}
        Followers: {3}
        Likes: {4}
        Joined in: {5}
        Profile picture link: {6}
        '''.format(name, tweets, following, followers, likes, date, "https://pbs.twimg.com/profile_images"+pic))
    except: print("Invalid link or username"); exit(0)

if __name__ == "__main__":
	try: u = argv[1]
	except: print(" [*] Hint: python fetch.py <profile_link>/<username>"); exit(0)
	if "twitter.com" not in u: fetch("http://twitter.com/" + u)
	else: fetch(u)
