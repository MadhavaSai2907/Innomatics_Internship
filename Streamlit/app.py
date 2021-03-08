import streamlit as st
import pandas as pd
import numpy as np
from pickle import load

st.markdown("<h1 style='text-align:center;color:red;'>Output Prediction</h1>",unsafe_allow_html=True)

def main():
    col1=st.number_input("col1")
    st.write('your number',col1)
    col2=st.number_input("col2")
    st.write('your number',col2)

    classifier=load(open('pickle/svmrbf.pkl','rb'))


    if st.button('Submit'):
        predicted_value=classifier.predict(np.array([[col1,col2]]))
        st.write('output',predicted_value)
    # click= st.button('Submit')
    # if click:
    #     # st.write('output',predicted_value)
    #     if predicted_value==0:
    #         st.write('zro')

if __name__ == '__main__':
    main()
