from typing import List

import psycopg2
from psycopg2.extras import execute_values

from .getDbCredentials import DatabaseConnect


def getSchema(dc, table) -> List:
    query = '''
    SELECT column_name
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE table_name = '{}'
    '''.format(table)

    results = getQuery(dc, query)

    return results

def getQuery(dc,
             query) -> List:
    cur = dc.conn.cursor()
    cur.execute(query)
    results = cur.fetchall()
    cur.close()

    return results

def insertQuery(dc,
                table,
                dataTuple,
                numCols) -> bool:
    cur = dc.conn.cursor()

    schemaList = getSchema(dc, table)
    schemaTuple = (colName[0] for colName in schemaList)
    schemaStr = str(tuple(schemaTuple)).replace("'", '')

    query = 'INSERT INTO {} {} VALUES %s'.format(table, schemaStr)
    execute_values(cur, query, dataTuple)
    dc.conn.commit()

    return True



if __name__ == '__main__':
    dc = DatabaseConnect()

    #TODO unit tests for these
    # test 1
    query = 'SELECT version()'
    results = getQuery(dc, query)
    print(results)

    # test 2
    query = '''
    SELECT * FROM test_table
    '''
    results = getQuery(dc, query)
    print(results)

    # test 3
    table = 'test_table'
    dataTuple = [(6, 'vinny', 'vinny@gmail.com'),
                 (7, 'vinny2', 'vinny2@gmail.com')]
    insertQuery(dc, table, dataTuple, numCols=3)

    # test 4
    table = 'test_table'
    schemaList = getSchema(dc, table)
    print(schemaList)

    dc.conn.close()
