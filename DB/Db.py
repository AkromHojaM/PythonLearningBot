# import os
# import psycopg2
#
#
# from dotenv import load_dotenv
# load_dotenv()
#
#
# class PG:
#     con = psycopg2.connect(dbname=os.getenv("DB_NAME"),
#                            user=os.getenv("DB_USER"),
#                            password=os.getenv("DB_PASSWORD"),
#                            host=os.getenv("DB_HOST"),
#                            port=os.getenv("DB_PORT"),)
#     cur = con.cursor()
#     query = """
#     CREATE TABLE IF NOT EXISTS Users(
#     id serial PRIMARY KEY,
#     user_id bigint unique,
#     lastname varchar(255),
#     firstname varchar(255));"""
#
#     alterin = "alter table users add column age integer"
#     cur.execute(query,alterin)
#     con.commit()
#
#     def add(self, user_id, lastname, firstname):
#         query = "insert into users (user_id, lastname, firstname) values (%s, %s, %s);"
#         params = (user_id, lastname, firstname)
#         self.cur.execute(query, params)
#         self.con.commit()
#     def checked_user(self, user_id):
#         query = "select * from users where id = %s"
#         params = (user_id,)
#         self.cur.execute(query, params)
#         return self.cur.fetchall()
