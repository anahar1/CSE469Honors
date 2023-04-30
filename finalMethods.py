import sys

def ffratio(followers, followings):
    if(followings == 0):
        print("ERROR: Followings is 0 (User follows no one).")
        print("Followers:", followers)
        ratio = -1
    else:
        ratio = followers/followings
        print("Follower-to-Following Ratio:", ratio)
        
    return ratio

def userVerified(verificationMark):
    if(verificationMark == True):
        print("Profile is verified by Instagram.")
        print("DETERMINATION: Account is 0% likely to be a bot.")
        sys.exit(0)

def userProfileImage(profilePicture):
    if(profilePicture == False):
        print("User does NOT have a profile image linked to their account.")
        return False
    else:
        print("User does have a profile image linked to their account.")
        return True