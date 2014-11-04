from django.utils.timezone import utc
import datetime


def sign(val):
    if val < 0:
	return -1
    else:
	return 1

def post_score(post, gravity=1.8, timebase=120):
    #delta = post.upvotes - post.downvotes
    sign_score = sign(post.points)
    points = abs(post.points)**(gravity-1)
    
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    total_secs = int((now - post.created).total_seconds())
    age = total_secs/60
    
    return sign_score*points/(age+timebase)**gravity
    

#################
