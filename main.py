import streamlit as st
import plotly.express as px

st.title("Weather forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to be forecasted")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky",))
st.subheader(f"{option} for the next {days} day(s) in {place}")

figure = px.line(x="Date", y="Temperature", labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
