import psycopg2

conn = psycopg2.connect(
    dbname="usuarios",
    user="postgres",
    password="", # Tu contraseña de postrgres
    host="localhost"
)

cursor = conn.cursor()

cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'users')")
table_exists = cursor.fetchone()[0]

if not table_exists:
    sql_query = """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            firstname varchar(100) NOT NULL,
            lastname varchar(100) NOT NULL,
            gender varchar(100) NOT NULL,
            age SMALLINT,
            phone varchar(100) NOT NULL,
            address varchar(100) NOT NULL
        )
    """
    cursor.execute(sql_query)

    conn.commit()

def commit():
    conn.commit()

