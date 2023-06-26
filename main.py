#python program for weather app which takes number of days as input ad gives temperature and sky conditions as output

import streamlit as st
import plotly.express as px
from b_end import get_data

st.title("Weather Forecast for the Next Days")
place=st.text_input("City: ")
days=st.slider("Forecast Days",min_value=1,max_value=5,help="Select the number of forcasted days")
option=st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filtered_data=get_data(place,days)

        if option=="Temperature":
            temperature = [i["main"]["temp"]/10 for i in filtered_data]
            date=[i["dt_txt"] for i in filtered_data]
            figure=px.line(x=date,y=temperature,labels={"x":"Date","y":"Temperature (C)"})
            st.plotly_chart(figure)

        if option=="Sky":
            images={"Clear":"images/clear.png","Clouds":"images/cloud.png","Rain":"images/rain.png","Snow":"images/snow.png"}
            sky_conditions = [j["weather"][0]["main"] for j in filtered_data]
            image_path=[images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_path,width=100)

    except KeyError:
        st.write("Oh! You entered a non-existing place")