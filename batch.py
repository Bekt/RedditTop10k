import praw
from pprint import pprint

co = open('num_comments.data', 'w')
up = open('ups.data', 'w')
do = open('downs.data', 'w')
sc = open('scores.data', 'w')
cr = open('created.data', 'w')

r = praw.Reddit(user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.69 Safari/537.17')

r.login('stats2013', 'stats2013')
subs = r.get_subreddit('all').get_top_from_all(limit=10000)

for s in subs:
	v = vars(s)
	co.write(str(v['num_comments']) + '\n')
	up.write(str(v['ups']) + '\n')
	do.write(str(v['downs']) + '\n')
	sc.write(str(v['score']) + '\n')
	cr.write(str(v['created_utc']) + '\n')

co.close()
up.close()
do.close()
sc.close()
cr.close()

