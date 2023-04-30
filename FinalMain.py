from finalMethods import *

import sys

#below are hard coded Instagram profiles
#dictionary format = [IGID]:[followers, followings, verified, noOfPosts, containsPicture, recentPostLikes1, recentPostComments1, recentPostLikes2, recentPostComments2, recentPostLikes3, recentPostComments3]
#missing: []:[created_recently]
#scraped data from Instagram public profiles for academic use
userProfiles = {}
userProfiles["cristiano"] = [579384173, 557, True, 3477, True, 7677136, 76165, 8152850, 55228, 6371558, 60314]
userProfiles["asucatholic"] = [1908, 108, False, 336, True, 63, 0, 49, 0, 31, 0]
userProfiles["kyoumb"] = [1, 1, False, 3477, False, 0, 0, 0, 0, 0, 0]
userProfiles["katara"] = [59100, 0, False, 562, True, 6145, 9, 3984, 15, 12991, 48]
userProfiles["zan3"] = [1683, 41, False, 0, False, 0, 0, 0, 0, 0, 0]
userProfiles["cale"] = [690, 238, False, 703, True, 18, 9, 13, 1, 19, 1]
userProfiles["krabby"] = [0, 23, False, 21, True, 0, 0, 0, 0, 0, 0]                                                 #ACCOUNT IS PRIVATE
userProfiles["slaws"] = [2, 0, False, 0, False, 0, 0, 0, 0, 0, 0]
userProfiles["kane"] = [33600, 975, False, 491, True, 100, 19, 100, 19, 99, 7]

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
    print("[-]: User's follower-to-following ratio is very low!")
    botPercentage += 25

#determine if user has a profile picture attached to their account
#if user does NOT, increase percentage and inform user
imageCheck = userProfileImage(userProfiles[instagramID][4])

#determine upon result
if imageCheck == False:
    botPercentage += 25

#determine if user has current post to calculate average interaction
if userProfiles[instagramID][3] > 0:
    averageLikes = averageLikes(userProfiles[instagramID][5], userProfiles[instagramID][7], userProfiles[instagramID][9])
    averageComments = averageComments(userProfiles[instagramID][6], userProfiles[instagramID][8], userProfiles[instagramID][10])
    
    if(averageLikes < (userProfiles[instagramID][0] * 0.01) and userProfiles[instagramID][3] < 3):
        print("[-]: User's average 'likes' are lower than 10% of their total followers.")
        botPercentage += 5
    if(averageComments < (userProfiles[instagramID][0] * 0.01) and userProfiles[instagramID][3] < 3):
        print("[-]: User's average 'comments' are lower than 10% of their total followers.")
        botPercentage += 5

#inform user of final calculation
print("DETERMINATION: Account is", botPercentage, "% likely to be a bot.")