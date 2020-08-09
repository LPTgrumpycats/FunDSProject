from getCredentials import AppOAuth


def getSubmissionEvents(reddit,
                        subreddit,
                        limit=256):
    subredditDataList = []
    for submission in reddit.subreddit(subreddit).top(limit=limit):
        subredditDataList.append(submission)

    return subredditDataList

def getSubmissionProperties(eventList,
                            property='upvote_ratio'):
    propertyList = []
    for submission in eventList:
        propertyList.append(submission.upvote_ratio)

    return propertyList

def getSubmissionCommentsVotes(eventList):
    commentList = getSubmissionProperties(eventList, 'comments')

    commentUpvoteList = []
    commentDownvoteList = []
    for comment in commentList:
        if type(comment).__name__=='Comment':
            commentUpvoteList.append(comment.ups)
            commentDownvoteList.append(comment.downs)

    return (commentUpvoteList, commentDownvoteList)


if __name__ == '__main__':
    aoa = AppOAuth()

    # test 1
    eventList = getSubmissionEvents(aoa.reddit, 'popular', limit=10)
    upvoteRatioList = getSubmissionProperties(eventList)

    print('Upvote ratios: ', upvoteRatioList)
    # [0.98, 0.97, 0.97, 0.96, 0.97, 0.97, 0.98, 0.96, 0.97, 0.96]
