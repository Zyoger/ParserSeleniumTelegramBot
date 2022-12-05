import psycopg2


def create():
    conn = psycopg2.connect(dbname='postgresdb', user='egor', host='localhost', password='P5n32esli77')
    cursor = conn.cursor()
    return cursor

# id, url, type teg, name tag, number


def add_task_in_db(id_task, url, type_teg, name_tag, number, verification_period):
    cursor = create()
    cursor.execute("""
    INSERT INTO tasks (task_id, url, type_teg, name_teg, number_teg, verification_period)
    VALUES (%s, %s, %s, %s, %s, %s)
    """,
                   (id_task, url, type_teg, name_tag, number, verification_period))


def read_task():
    cursor = create()
