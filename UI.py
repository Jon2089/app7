import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select the data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        data, times = get_data(place, days, option)
        if option == "Temperature":
            data = [t / 10 for t in data]
            figure = px.line(x=times, y=data, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            image_paths = [f"images/{weather.lower()}" + ".png" for weather in data]
            st.image(image_paths, width=115, caption=times)
    except KeyError:
        st.info("Please enter a real city!")