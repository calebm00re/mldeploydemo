# from itertools import count
# import streamlit as st
# import pandas as pd

# if 'count' not in st.session_state:
#     st.session_state['count'] = 0

# def goUp():
#     st.session_state['count'] += 1


# st.button(str(st.session_state.count), key=None, help=None, on_click=goUp);

# st.write((st.session_state['count']));

import streamlit as st
import numpy as np
import pandas as pd


df = pd.read_csv('penguins.csv')
f = open("demo.txt", "a")

file1 = open('demo.txt', 'r')
Lines = file1.readlines()
# df.head()
# sl= st.slider('Row?', 0, df.index[-1], 25)
# st.title('Penguin data')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

st.write(df.iloc[0:st.session_state.count+1])

comment = st.text_input("write something")

# st.write('comment:', comment)
f.write(comment)
f.write("\n")

Lines.append(comment)

count = 0
for line in Lines:
    count += 1
    st.write(count, line)

