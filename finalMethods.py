def ffRatio(followers, followings):

    if(followings == 0):
        print("Cannot compute ratio, user follows no one!")
        print("However, here is the number of followers the profile has:", followers)
        ratio = -1
    else:
        ratio = followers/followings
        print("The follower to following ratio is: ", ratio)
    return ratio