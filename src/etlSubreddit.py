from ..application.getAppCredentials import AppOAuth


def getSubmissionEvents(reddit,
                        subreddit,
                        limit=256):
    subredditDataList = []
    for submission in reddit.subreddit(subreddit).top(limit=limit):
        subredditDataList.append(submission)

    return subredditDataList

def getEventProperties(eventList,
                       eventProperty='upvote_ratio'):
    propertyDict = {}
    for event in eventList:
        propertyDict[event.id] = event.__getattr__(eventProperty)

    return propertyDict

def getEventCommentsVotes(event):

    commentsList = event.comments.list()

    commentUpvoteDict = {}
    commentDownvoteDict = {}
    for comment in commentsList:
        if type(comment).__name__=='Comment':
            commentUpvoteDict[comment.id] = comment.ups
            commentDownvoteDict[comment.id] = comment.downs

    return (commentUpvoteDict, commentDownvoteDict)


if __name__ == '__main__':
    aoa = AppOAuth()

    # test 1
    eventList = getSubmissionEvents(aoa.reddit, 'popular', limit=10)
    upvoteRatioList = getEventProperties(eventList)

    print('Upvote ratios: ', upvoteRatioList)
    # [0.98, 0.97, 0.97, 0.96, 0.97, 0.97, 0.98, 0.96, 0.97, 0.96]

    # test 2
    commentUpvoteDict, commentDownvoteDict = getEventCommentsVotes(eventList[0])

    print('Upvote dict: ', commentUpvoteDict)
