from finalMethods import *
import sys

#user profiles = [Number of followers, number of followings, is_verified, number_of_posts, has_profile_picture, created_recently]
#scraped data from instagram public profiles for academic use
userProfiles = {}
userProfiles["cristiano"] = [579384173, 557, True, 3477, True]
userProfiles["asucatholic"] = [1908, 108, False, 336, True]
userProfiles["kyoumb"] = [1, 1, False, 3477, False]
userProfiles["katara"] = [59100, 0, False, 562, True]
userProfiles["zan3"] = [1683, 41, False, 0, False]
userProfiles["cale"] = [690, 238, False, 703, True]
userProfiles["krabby"] = [0, 23, False, 21, True]
userProfiles["slaws"] = [2, 0, False, 0, False]
userProfiles["kane"] = [33600, 975, False, 491, True]

#Get the account to run our algorithm with
print("Enter the Instagram Account ID: ", end="")
instagramID = input()

#check if user is verified and if the user is verified, print verification status and do sys.exit()

#percent chance the passed in profile is a bot
botChance = 0

#Computes follower to following ratio
userRatio = ffRatio(userProfiles[instagramID][0], userProfiles[instagramID][1])

if(userRatio < 2):
    botChance += 25


print("The percent chance the profile is a bot is: ", botChance, "%")






