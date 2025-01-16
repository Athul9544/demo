import pickle
import streamlit as st
from os import path
import numpy as np

st.title("flower classification app")

filename="lr.pk"
with open(path.join(filename),'rb') as f:
    lr=pickle.load(f)
    
sl=st.number_input("insert a sepel length")
sw=st.number_input("insert a sepel width")
pl=st.number_input("insert a petal lemgth")
pw=st.number_input("insert a petal length")
    
if st.button("predict"):
    pred=lr.predict(np.array([[sl,sw,pl,pw]]))
    st.write("the flower is:",pred[0])
