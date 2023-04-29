from instagramy import InstagramUser, InstagramPost, InstagramHashTag 
from Posts import *
from Followers import *
import os
import sys

#import language_check

session_id = "38566737751%3Ah7JpgePGAoLxJe%334"
#session_id = "48239853725%3AtMLROwfiPVhLFP%3A56"

print("Enter the Instagram Account ID: ")
instagramID = input()
botChance = 0


# Connecting the profile
user = InstagramUser(instagramID, sessionid=session_id)

# printing the basic details like
# followers, following, bio
if(user.is_verified == True):
    print("The user is verified and is not a bot")
    sys.exit()

print("Number of followers: " + str(f'{user.number_of_followers:,}'))
print("Number of followings: " + str(f'{user.number_of_followings:,}'))
print("Followers to following ratio: " + str(f'{user.number_of_followers/user.number_of_followings}'))

if(user.number_of_followers < 10):
    print("User has too few followers")
    botChance = botChance + 10


#Unfortunately, there is an inability with instagramy to determine whether a user has a profile picture. In every scenario, Instagramy returns the url for 
#the profile picture, even if there is a default image. However, instagramy will return multiple different image url's for the default image. This may be due 
#to changes in the default image design on Instagram's part
#print(user.profile_picture_url)
print("User has joined recently: " + str(user.is_joined_recently))

if(user.is_joined_recently != False):
    botChance = botChance + 5

print("This is the number of the user's recent posts (12 being the instagramy max): ", end='')
print(postInfo(user.posts))

if(postInfo(user.posts) != 0):
    print("These are the dates for the user's twelve most recent posts")
    postDate(user.posts)
else:
    botChance = botChance + 25

#print(user.posts)
#prints all post-related info in one giant text blurb


#post = InstagramPost('CLGkNCoJkcM', sessionid=session_id)
#print(post.upload_time)

score1 = followers(instagramID=instagramID)
score2 = creation_date(instagramID=instagramID)
score3 = like_comment_check(instagramID=instagramID)
score4 = post_error_frequency(instagramID=instagramID)
score5 = post_content_standard(instagramID=instagramID)
score6 = advertizing(instagramID=instagramID)

final_score = score1 * 0.1 + score2 * 0.2 + score3 * 0.3 + score4 * 0.1 + score5 * 0.1 + score6 * 0.2

user.posts_display_urls

print("This is the final score:", botChance)