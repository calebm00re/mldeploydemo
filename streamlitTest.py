import streamlit as st
import pandas as pd

if 'count' not in st.session_state:
    st.session_state['count'] = 0

def goUp():
    st.session_state['count'] += 1


st.button(str(st.session_state.count), key=None, help=None, on_click=goUp);


df = pd.read_csv("penguins.csv");

st.write(df[st.session_state.count:st.session_state.count+1]);