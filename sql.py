import asyncio, random, os, psycopg2, discord

async def open():
    global con, cur
    dburl = os.environ["HEROKU_POSTGRESQL_COBALT_URL"]
    con = psycopg2.connect(dburl, sslmode="require")
    cur = con.cursor()
    return cur

async def run(task):
    cur.execute(task)

async def read():
    cur.execute("SELECT * FROM people")
    return cur.fetchall()

async def add(eyedee):
    cur.execute("INSERT INTO payday (id) VALUES (%s)",(eyedee))
    return

async def close():
    con.commit()
    cur.close()
    con.close()

    
    
