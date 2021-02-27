from instapy import InstaPy
from instapy import smart_run

user = 'skyll21'
pwd = '615243'
session = InstaPy(username = user, 
			      password = pwd)

with smart_run(session):
	session.set_do_follow(enabled = True, percentage = 100)
	session.set_do_like(enabled = True, percentage = 100)
	
	#session.like_by_tags(['pizzaria'], amount = 5)
	#session.like_by_feed(amount =2, randomize =True, interact = True, unfollow = False)
	session.like_by_location(['600831993/bangu/'], amount = 3)
	
	comm = []
	session.set_do_comment(enabled = True, percentage = 100)
	session.set_comments(comm, media ='Photo')
	session.join_pods()


