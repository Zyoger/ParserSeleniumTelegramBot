import psycopg2


def create_tab():
    """"""
    conn = psycopg2.connect(dbname='postgresdb', user='egor', host='localhost', password='P5n32esli77')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE test_tasks_1 "
                   "(id serial PRIMARY KEY, url varchar, type_tag varchar, name_tag varchar, number_position int,"
                   " verification_period int, last_prise int, min_prise int, max_prise int);")
    conn.commit()
    cursor.close()
    conn.close()


def add_task_in_tab(url, type_teg, name_tag, number_position, verification_period):
    """"""
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
    """"""
    conn = psycopg2.connect(dbname='postgresdb', user='egor', host='localhost', password='P5n32esli77')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_tasks_1;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def dell_task(task_id):
    """"""
    conn = None
    flag = 0
    try:
        conn = psycopg2.connect(dbname='postgresdb', user='egor', host='localhost', password='P5n32esli77')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM test_tasks_1 WHERE id = %s", (task_id,))
        flag = cursor.rowcount
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    if flag == 1:
        return print(f"Удалено: {flag} задача.")
    else:
        print("Ошибка удаления!!! Задача не найдена!!!")


def update_prise(last_prise, min_prise, max_prise):  # переписать, должен приниматься один аргумент (текущая цена), после обновлять нужное значение.
    """"""
    conn = psycopg2.connect(dbname='postgresdb', user='egor', host='localhost', password='P5n32esli77')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO test_tasks_1 (last_prise, min_prise, max_prise)
        VALUES (%s, %s, %s)
        """,
                   (last_prise, min_prise, max_prise))
    conn.commit()
    cursor.close()
    conn.close()


# create_tab()
# p = read_task()
# print(p)
# print(len(p))
# dell_task(1)
