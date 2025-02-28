import streamlit as st
from pint import UnitRegistry

# Initialize Unit Registry
ureg = UnitRegistry()

# App Title
st.title("Unit Converter App 📏")

# Dropdown for Unit Categories
categories = [
    "Length", "Area", "Data Transfer Rate", "Digital Storage", "Energy", "Frequency",
    "Fuel Economy", "Mass", "Plane Angle", "Pressure", "Speed", "Temperature", "Time", "Volume"
]

category = st.selectbox("Select a category:", categories)

# Unit options based on category
unit_options = {
    "Length": ["meters", "kilometers", "miles", "feet", "inches"],
    "Area": ["square meters", "hectares", "acres", "square feet"],
    "Data Transfer Rate": ["bit/second", "kilobit/second", "megabit/second", "gigabit/second"],
    "Digital Storage": ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes"],
    "Energy": ["joules", "calories", "kilowatt-hours"],
    "Frequency": ["hertz", "kilohertz", "megahertz"],
    "Fuel Economy": ["kilometers/liter", "miles/gallon"],
    "Mass": ["grams", "kilograms", "pounds", "ounces"],
    "Plane Angle": ["degrees", "radians"],
    "Pressure": ["pascals", "atmospheres", "bars", "psi"],
    "Speed": ["meters/second", "kilometers/hour", "miles/hour"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["seconds", "minutes", "hours", "days"],
    "Volume": ["liters", "milliliters", "cubic meters", "gallons"]
}

# User Input
from_unit = st.selectbox("From Unit:", unit_options[category])
to_unit = st.selectbox("To Unit:", unit_options[category])

value = st.number_input("Enter the value to convert:", min_value=0.0, format="%f")

# Conversion Logic
if st.button("Convert"):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
    except Exception as e:
        st.error(f"Conversion error: {e}")

# Friendly Tip
st.info("Tip: Select your units carefully, and input a positive value to get accurate results!")

