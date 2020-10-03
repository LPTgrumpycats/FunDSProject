import configparser
import praw


class AppOAuth:
    def __init__(self,
                 configFile='FunDSProject/config.ini',
                 authSection='REDDIT'):
        self.configFile = configFile
        self.authSection = authSection

        self.getConfig()
        self.getSecrets()
        self.getReddit()

    def getConfig(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.configFile)

    def getSecrets(self):
        self.clientId = self.config[self.authSection]['clientId']
        self.clientSecret = self.config[self.authSection]['clientSecret']
        self.userName = self.config[self.authSection]['userName']
        self.password = self.config[self.authSection]['password']
        self.userAgent = self.config[self.authSection]['userAgent']

    def getReddit(self):
        self.reddit = praw.Reddit(client_id=self.clientId,
            client_secret=self.clientSecret,
            password=self.password,
            user_agent=self.userAgent,
            username=self.userName)


if __name__ == '__main__':
    aoa = AppOAuth()

    # test 1 oauth
    # aoa.reddit.subreddit('test').submit('Test Submission', url='https://reddit.com')

    # test 2 retrieve data
    submissionScoreList = []
    for submission in aoa.reddit.subreddit('popular').hot(limit=256):
        submissionScoreList.append(submission.score)

    print('Length of list: ', len(submissionScoreList))
    print('Scores: ', submissionScoreList)
