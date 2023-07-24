import psycopg2
current_dbname = 'mydb'
current_user = 'zyoger'
current_host = '127.0.0.1'
current_port = '54321'
current_password = 'p5n32esli'


def create_tab():
    """Create table in db"""
    conn = psycopg2.connect(dbname=current_dbname, user=current_user, host=current_host, port=current_port, password=current_password)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE test_tasks_00"
                   "(id serial PRIMARY KEY, url varchar, type_tag varchar, name_tag varchar, number_position int,"
                   " verification_period int, last_prise int, min_prise int, max_prise int);")
    print("Таблица создана")
    conn.commit()
    cursor.close()
    conn.close()


def add_task_in_tab(url, type_teg, name_tag, number_position, verification_period):
    """Add task in table"""
    conn = psycopg2.connect(dbname=current_dbname, user=current_user, host=current_host, port=current_port, password=current_password)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO test_tasks_00 (url, type_tag, name_tag, number_position, verification_period)
    VALUES (%s, %s, %s, %s, %s)
    """,
                   (url, type_teg, name_tag, number_position, verification_period))
    print("Задание добавлено в базу данных")
    conn.commit()
    cursor.close()
    conn.close()


def read_task():
    """Read all tasks in table"""
    conn = psycopg2.connect(dbname=current_dbname, user=current_user, host=current_host, port=current_port, password=current_password)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM test_tasks_00;""")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def dell_task(task_id):
    """Dell task from db"""
    conn = None
    flag = 0
    try:
        conn = psycopg2.connect(dbname=current_dbname, user=current_user, host=current_host, port=current_port, password=current_password)
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM test_tasks_00 WHERE id = %s""", (task_id,))
        flag = cursor.rowcount
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    if flag == 1:
        return True
    else:
        return False


def update_prise(task_id, last_prise):
    """ update vendor name based on the vendor id """
    sql = """ UPDATE test_tasks_00 SET last_prise = %s WHERE id = %s"""
    conn = None
    updated_rows = 0
    try:
        conn = psycopg2.connect(dbname=current_dbname, user=current_user, host=current_host, port=current_port, password=current_password)
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

# for i in range(17, 20):
#    dell_task(i)
