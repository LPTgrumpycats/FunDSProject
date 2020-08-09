import configparser
import psycopg2


class DatabaseConnect:
    def __init__(self,
                 configFile='config.ini',
                 authSection='POSTGRES'):
        self.configFile = configFile
        self.authSection = authSection

        self.getConfig()
        self.getSecrets()
        self.getConnection()

    def getConfig(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.configFile)

    def getSecrets(self):
        self.host = self.config[self.authSection]['host']
        self.database = self.config[self.authSection]['database']
        self.username = self.config[self.authSection]['user']
        self.password = self.config[self.authSection]['password']

    def getConnection(self):
        self.conn = psycopg2.connect(host=self.host,
            database=self.database,
            user=self.username,
            password=self.password)


if __name__ == '__main__':
    dc = DatabaseConnect()

    # test 1
    cur = dc.conn.cursor()
    cur.execute('SELECT version()')
    dbVersion = cur.fetchone()
    print('Database Version: ', dbVersion)
