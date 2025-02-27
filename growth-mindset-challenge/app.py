# Imports
import streamlit as st
import pandas as pd
import os
from io import BytesIO
import openpyxl

st.set_page_config(page_title="Data Sweeper", layout="wide")
st.title("Data Sweeper")
st.write("Convert your data to a different formats")

uploaded_file = st.file_uploader("Upload a file (CSV or Excel)", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_file: 
    for file in uploaded_file:
        file_extension = os.path.splitext(file.name)[-1].lower()

        if file_extension == ".csv":
            df = pd.read_csv(file, encoding="latin1")
        elif file_extension == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error("File format not supported: {file_extension}")
            continue

        # display info for the file
        st.write(f"File: {file.name}")
        st.write(f'File size: {file.size}')

        # display 5 rows of data
        st.write("Preview the Head of the Dataframe")
        st.dataframe(df.head())

        # Options for data cleaning
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Cleaned data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed")
            
            with col2:
                if st.button(f"Fill missing values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing values has been filled")

        # Choose specific columns to keep or convert
        st.subheader("Select Columns to Keep or Convert")
        columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        # Create some visualizations
        st.subheader(" Data Visualizations")
        if st.checkbox(f"Show visualizations for {file.name}"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])

        # Convert the data -> CSV to Excel or Excel to CSV
        st.subheader("Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"): 
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_extension, ".csv")
                mime_type = "text/csv"

            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_extension, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            # Download Button
            st.download_button(
                label=f"Download {file_name}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            ) 

        st.success("All files processed!")