import psycopg2


def create_tab():
    conn = psycopg2.connect(dbname='postgresdb', user='egor', host='localhost', password='P5n32esli77')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE test_tasks_1 (id serial PRIMARY KEY, url varchar, type_tag varchar, name_tag varchar, number_position int, verification_period int);")
    conn.commit()
    cursor.close()
    conn.close()


def add_task_in_tab(url, type_teg, name_tag, number_position, verification_period):
    conn = psycopg2.connect(dbname='postgresdb', user='egor', host='localhost', password='P5n32esli77')
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO test_tasks_1 (url, type_tag, name_tag, number_position, verification_period)
    VALUES (%s, %s, %s, %s, %s)
    """,
                   (url, type_teg, name_tag, number_position, verification_period))
    conn.commit()
    cursor.close()
    conn.close()


def read_task():
    conn = psycopg2.connect(dbname='postgresdb', user='egor', host='localhost', password='P5n32esli77')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_tasks_1;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


# create_tab()
# p = read_task()
# print(p)
# print(len(p))
