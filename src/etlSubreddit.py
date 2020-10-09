from typing import List, Dict, Tuple

from ..application.getAppCredentials import AppOAuth


def getSubmissionEvents(reddit,
                        subreddit,
                        limit=256) -> List:
    subredditDataList = []
    for submission in reddit.subreddit(subreddit).top(limit=limit):
        subredditDataList.append(submission)

    return subredditDataList

def getEventProperties(eventList,
                       eventProperty='upvote_ratio') -> Dict:
    propertyDict = {}
    for event in eventList:
        propertyDict[event.id] = event.__getattr__(eventProperty)

    return propertyDict

def getEventCommentsVotes(event) -> Tuple[Dict, Dict]:

    commentsList = event.comments.list()

    commentUpvoteDict = {}
    commentDownvoteDict = {}
    for comment in commentsList:
        if type(comment).__name__=='Comment':
            commentUpvoteDict[comment.id] = comment.ups
            commentDownvoteDict[comment.id] = comment.downs

    return commentUpvoteDict, commentDownvoteDict

def getSubredditName(event) -> str:
    subredditName = event.subreddit.__dict__['display_name']

    return subredditName

def getSubredditNames(eventList) -> List[str]:
    subredditNameList = list()
    for event in eventList:
        subredditName = getSubredditName(event)
        subredditNameList.append(subredditName)

    return subredditNameList


if __name__ == '__main__':
    aoa = AppOAuth()

    # test 1
    eventList = getSubmissionEvents(aoa.reddit, 'popular', limit=10)
    upvoteRatioList = getEventProperties(eventList)
    print(eventList)

    print('Upvote ratios: ', upvoteRatioList)
    # [0.98, 0.97, 0.97, 0.96, 0.97, 0.97, 0.98, 0.96, 0.97, 0.96]

    # test 2
    commentUpvoteDict, commentDownvoteDict = getEventCommentsVotes(eventList[0])

    print('Upvote dict: ', commentUpvoteDict)
