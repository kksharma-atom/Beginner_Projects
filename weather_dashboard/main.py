import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, sub header widgets
st.title("The Weather Forecast App")

place = st.text_input("Place: ", placeholder="Enter name of a place")

days = st.slider(label="Forecast Days", min_value=1, max_value=5, help="Select the number of forecast days")

option = st.selectbox(label="Select data to view", options=("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Get data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            # Get dates
            date_list = [dict["dt_txt"] for dict in filtered_data]
            # Get temperature values
            temperature_list = [dict["main"]["temp"] / 10 for dict in filtered_data]
            # Create temperature plot
            figure = px.line(x=date_list, y=temperature_list, labels={"x": "Date", "y":"Temperature (C)"} )
            st.plotly_chart(figure)

        if option == "Sky":
                sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
                images = {"Clear":"images/clear.png",
                        "Clouds":"images/cloud.png",
                        "Rain":"images/rain.png",
                        "Snow":"images/snow.png"}
                sky_cond_img_list = [images[sky_condition] for sky_condition in sky_conditions] 
                st.image(sky_cond_img_list, width=115)
    except KeyError:
         st.write("That place does not exist.")
