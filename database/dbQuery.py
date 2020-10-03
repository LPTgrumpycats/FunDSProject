import psycopg2
from .getDbCredentials import DatabaseConnect


def getQuery(dc,
             query):
    cur = dc.conn.cursor()
    cur.execute(query)
    results = cur.fetchall()
    cur.close()

    return results


if __name__ == '__main__':
    dc = DatabaseConnect()

    # test 1
    query = 'SELECT version()'
    results = getQuery(dc, query)
    print(results)
    dc.conn.close()
