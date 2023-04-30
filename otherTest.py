from instaloader import Instaloader, Profile
import sys
import argparse

parser = argparse.ArgumentParser(description='Determine bot chance of an instagram account')

print("Enter the Instagram Account ID: ")
instagramID = input()

PROFILE = instagramID

L = Instaloader()

profile = Profile.from_username(L.context, PROFILE)

botChance = 0

# ffratio = profile.followers/profile.followees
# print(ffratio)

if(profile.is_verified):
    print("The user is verified, end of bot detector")
    print(profile.get_igtv_posts().count)
    sys.exit()

print("Here are some general stats relating to the user inputted")
print("Your input has", profile.followers, "followers and", profile.followees, "people following them")


if(profile.followers < 10):
    print("The low follower count has led this program to increase this input's bot chance")
    botChance = botChance + 25

print(profile.get_igtv_posts().count)

#Method to get likes detailed in Instaloader's documentation... unfortunately, requires an instagram account

# likes = set()
# print("Fetching likes of all posts of profile {}.".format(profile.username))
# for post in profile.get_posts():
#     print(post)
#     likes = likes | set(post.get_likes())


print(botChance)



#print(profile.followers)

#print(profile.get_posts())