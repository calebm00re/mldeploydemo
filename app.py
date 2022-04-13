import streamlit as st
import numpy as np
import pandas as pd
# import sqlite3
# con = sqlite3.connect('example.db')
# co = con.cursor()

# #create a table if it doesnt exist
# co.execute("CREATE TABLE IF NOT EXISTS example(name TEXT)")

# #get all values from the table into variable
# Lines = co.execute("SELECT * FROM example")

# #have a test input to add a comment to the database
# st.write("Add a comment to the database")
# name = st.text_input("Comment")

# #add the comment to the database
# co.execute("INSERT INTO example VALUES(?)", (name,))

# #add comment to Lines
# Lines = co.execute("SELECT * FROM example")

# #display all comments
# st.write("All comments")
# for line in Lines:
#     st.write(line)




# co.execute("""CREATE TABLE IF NOT EXISTS example(comment text)""")

# Lines = co.execute("""SELECT * FROM example""").fetchall()



df = pd.read_csv('penguins.csv')
f = open("demo.txt", "a")


file1 = open('demo.txt', 'r')
Lines = file1.readlines()

if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

st.write(df.iloc[0:st.session_state.count+1])

comment = st.text_input("write something")
# co.execute("""INSERT INTO example VALUES(?)""", (comment,))
f.write(comment)
f.write("\n")

Lines.append(comment)

count = 0
for line in Lines:
    count += 1
    st.write(count, line)

