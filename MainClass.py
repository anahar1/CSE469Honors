from instagramy import InstagramUser, InstagramPost, InstagramHashTag 
from Posts import *
from Followers import *

session_id = "38566737751%3Ah7JpgePGAoLxJe%334"

print("Enter the Instagram Account ID: ")
instagramID = input()

# Connecting the profile
user = InstagramUser(instagramID, sessionid=session_id)

# printing the basic details like
# followers, following, bio
print(user.is_verified)
print(user.number_of_followers)
print(user.number_of_followings)

score1 = followers(instagramID=instagramID)
score2 = creation_date(instagramID=instagramID)
score3 = like_comment_check(instagramID=instagramID)
score4 = post_error_frequency(instagramID=instagramID)
score5 = post_content_standard(instagramID=instagramID)
score6 = advertizing(instagramID=instagramID)

final_score = score1 * 0.1 + score2 * 0.2 + score3 * 0.3 + score4 * 0.1 + score5 * 0.1 + score6 * 0.2

print(final_score)