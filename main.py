import streamlit as st
import plotly.express as px
import pandas as pd

# adaugam un titlu
st.title("In Search for Happiness")

#  daugam casute de selectare
option_x = st.selectbox("Select the data for the X-axis",
                        ("GDP", "Happiness", "Generosity"))
option_y = st.selectbox("Select the data for the Y-axis",
                        ("GDP", "Happiness", "Generosity"))

# aplicam dateframe pt a obtine datele din happy csv
df = pd.read_csv("happy.csv")

match option_x:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

match option_y:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]

# adaugam subantetul
st.subheader(f"{option_x} and {option_y}")

# cream si adaugam graficul
figure1 = px.scatter(x=x_array, y=y_array,
                     labels={"x": option_x, "y":option_y})
st.plotly_chart(figure1)