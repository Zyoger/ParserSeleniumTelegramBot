import psycopg2

"""
cursor.execute('''SELECT datname from pg_database''')
rows = cursor.fetchall()
print("\nShow me the databases:\n")
for row in rows:
    print("   ", row[0])
"""


def create():
    conn = psycopg2.connect(dbname='postgres', user='egor', host='localhost', password='P5n32esli77')
    cursor = conn.cursor()
    return cursor


def add_task_in_db():
    cursor = create()


def read_task():
    cursor = create()
