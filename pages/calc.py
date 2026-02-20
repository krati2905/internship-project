import streamlit as st
st.sidebar.title('BMI CALCULATOR APP')
st.sidebar.subheader('navigation')

st.title('BMI CALCULATOR APP')
h = st.number_input('enter your height in cm')
w = st.number_input('enter your weight in kg')
if st.button("calculate bmi"):
    bmi =w/(h/100)**2
    st.success(f'your BMI is{bmi:.2f}')