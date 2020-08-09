import configparser
import praw


class AppOAuth:
    def __init__(self,
                 configFile='config.ini',
                 authSection='REDDIT'):
        self.configFile = configFile
        self.authSection = authSection

        self.getConfig()
        self.getSecrets()
    
    def getConfig(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.configFile)
    
    def getSecrets(self):
        self.clientId = self.config[self.authSection]['clientId']
        self.clientSecret = self.config[self.authSection]['clientSecret']
        self.userName = self.config[self.authSection]['userName']
        self.password = self.config[self.authSection]['password']
        self.userAgent = self.config[self.authSection]['userAgent']


if __name__ == '__main__':
    aoa = AppOAuth()

    reddit = praw.Reddit(client_id=aoa.clientId,
                         client_secret=aoa.clientSecret,
                         password=aoa.password,
                         user_agent=aoa.userAgent,
                         username=aoa.userName)
    
    # test1 oauth
    # reddit.subreddit('test').submit('Test Submission', url='https://reddit.com')

    # test2 retrieve data
    submissionScoreList = []
    for submission in reddit.subreddit('popular').hot(limit=256):
        submissionScoreList.append(submission.score)

    print('Length of list: ', len(submissionScoreList))
    print('Scores: ', submissionScoreList)
