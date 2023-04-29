def like_comment_check(instagramID):
    like_comment_score = 0
    return like_comment_score

def post_error_frequency(instagramID):
    post_error_score = 0
    return post_error_score
    
def post_content_standard(instagramID):
    post_content_score = 0
    return post_content_score

def advertizing(instagramID):
    advertizing_score = 0
    return advertizing_score

def postInfo(allData):
    data = str(allData)
    recentPostCount = data.count('Post')
    #print(recentPostCount)
    #print(data)
    return recentPostCount

def postDate(allData):
    data = str(allData)
    #print(data)

    while data != ']':
        temp = data[data.index('taken_at_timestamp=datetime.datetime'):data.index('))')]
        #print(temp)
        year = temp[temp.index('(') + 1:temp.index(',')]
        temp = temp[temp.index(',') + 2:]
        month = temp[0:temp.index(',')]
        temp = temp[temp.index(',') + 2:]
        day = temp[0:temp.index(',')]
        date = month + day + year
        print(month, day, year, sep="/")
        data = data[data.index('))') + 2:]
        #print(data)
    #temp3 = temp[]
