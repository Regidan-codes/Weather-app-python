import streamlit as st
import plotly.express as px
from backend import get_data

# Added title, slider, text input-box, sub-header
st.title("Weather forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to be forecasted")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky",))
st.subheader(f"{option} for the next {days} day(s) in {place}")


# Get date and temperature/sky data from openweather api


# Plot using plotly
if place:
    try:

        filtered_data = get_data(place, days)
        if option == 'Temperature':
            temperatures = [i['main']['temp'] / 10 for i in filtered_data]
            dates = [i['dt_txt'] for i in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == 'Sky':
            images = {"Clear": "Images/clear.png", "Clouds": "Images/cloud.png",
                      "Rain": "Images/rain.png", "Snow": "Images/snow.png"}
            sky_conditions = [i['weather'][0]['main'] for i in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)

    except KeyError:

        st.write("That place is not available. Please try again.")
