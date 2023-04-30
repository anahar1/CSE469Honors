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

#prompt user to input Instagram handle to run verification
print("Enter Instagram Account ID: ", end = "")

#store user input
instagramID = input()

#determine if user is verified
#if user is verified, inform user and exit
userVerified(userProfiles[instagramID][2])

#variable will update to determine the likelihood an Instagram account is a bot
botPercentage = 0

#compute follower-to-following ratio
userRatio = ffratio(userProfiles[instagramID][0], userProfiles[instagramID][1])

#determine cutline
if(userRatio < 2 and userRatio != -1):
    botPercentage += 25

#determine if user has a profile picture attached to their account
#if user does NOT, increase percentage and inform user
imageCheck = userProfileImage(userProfiles[instagramID][4])

#determine upon result
if imageCheck == False:
    botPercentage += 25

#inform user of final calculation
print("DETERMINATION: Account is", botPercentage, "% likely to be a bot.")