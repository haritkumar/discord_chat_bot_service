from mysql.connector import connect, Error

db_conn = connect(
    host='localhost',
    user='root',
    password='',
    database='discord_bot'
)



def add_history(discord_user, term, results):
    print("adding history")
    insert_query = "INSERT INTO search_history (discord_user, term, results, created_date) VALUES (%s , %s , %s , NOW())"

    try:
        cursor = db_conn.cursor()
        cursor.execute(insert_query, (str(discord_user), str(term), str(results)))
        db_conn.commit()
    except Error as e:
        print(e)
