import streamlit as st
st.title(":zap: pytopia dashboard")
st.write("Welcome to the pytopia dashboard! Here you can monitor and manage your pytopia applications.")
import pandas as pd
from io import StringIO
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as image
import os

login_option = st.sidebar.radio("Login/Signup", ("Login", "Signup"))
if login_option == "Login":
    st.sidebar.subheader("Login to your account")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    
    submited = st.form_submit_button("Login")
    if submited:
        pass
else:
    st.sidebar.subheader("Create a new account")
    new_username = st.sidebar.text_input("Username")
    new_email = st.sidebar.text_input("Email")
    new_password = st.sidebar.text_input("Password", type="password")
    
    submited = st.form_submit_button("Signup")
    if submited:
        pass   
banner = image.open("/home/emadleo/new-project/git-practice/pytopia-dashboard/src/1.png")
st.image(banner, caption="pytopia banner")

with st.expander("Show seaborn pairplot"):
    fig, ax = plt.subplots(1,1, figsize=(10,6))
    sns.histplot(np.random.randn(100),ax=ax)
    st.pyplot(fig)
    

with st.expander("user Profile:"):
    col1, col2, col3 = st.columns(3)
    col1.text_input("Name:")
    col2.text_input("Email:")
    col3.text_input("Location:")  
enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)
