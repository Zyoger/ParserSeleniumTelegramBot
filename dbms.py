import psycopg2


def create_tab():
    """"""
    conn = psycopg2.connect(dbname='postgresdb', user='egor', host='localhost', password='P5n32esli77')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE test_tasks_2 "
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
    INSERT INTO test_tasks_2 (url, type_tag, name_tag, number_position, verification_period)
    VALUES (%s, %s, %s, %s, %s)
    """,
                   (url, type_teg, name_tag, number_position, verification_period))
    print("Задание добавлено в базу данных")
    conn.commit()
    cursor.close()
    conn.close()


def read_task():
    """"""
    conn = psycopg2.connect(dbname='postgresdb', user='egor', host='localhost', password='P5n32esli77')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_tasks_2;")
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
        cursor.execute("""DELETE FROM test_tasks_2 WHERE id = %s""", (task_id,))
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


def update_prise(task_id, last_prise):
    """ update vendor name based on the vendor id """
    sql = """ UPDATE test_tasks_2
                SET last_prise = %s
                WHERE id = %s"""
    conn = None
    updated_rows = 0
    try:
        conn = psycopg2.connect(dbname='postgresdb', user='egor', host='localhost', password='P5n32esli77')
        cur = conn.cursor()
        cur.execute(sql, (last_prise, task_id))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return updated_rows


# create_tab()
# p = read_task()
# print(p)
# print(len(p))
# dell_task(16)

# for i in range(11, 16):
#     dell_task(i)
