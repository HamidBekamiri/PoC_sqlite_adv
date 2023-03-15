import streamlit as st
import pandas as pd
import altair as alt

# load data
@st.cache
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
    return df

df = load_data()

# create sidebar
st.sidebar.header("Iris Dataset Explorer")
species = st.sidebar.selectbox("Select a species", df.species.unique())

# filter data by species
df_species = df[df.species == species]

# display statistics and plot
st.write(f"## {species} Statistics")
st.write(df_species.describe())

chart = alt.Chart(df_species).mark_point().encode(
    x='petal_length',
    y='petal_width',
    color='species',
    tooltip='species'
).properties(
    width=400,
    height=400
)
st.altair_chart(chart, use_container_width=True)

# allow user to add data
st.write("## Add New Data")
new_data = st.text_input("Enter new data as comma separated values (sepal_length, sepal_width, petal_length, petal_width, species)")
if st.button("Add Data"):
    new_data = new_data.split(",")
    if len(new_data) != 5:
        st.warning("Please enter all five values")
    else:
        try:
            new_data[0] = float(new_data[0])
            new_data[1] = float(new_data[1])
            new_data[2] = float(new_data[2])
            new_data[3] = float(new_data[3])
            df = df.append({
                "sepal_length": new_data[0],
                "sepal_width": new_data[1],
                "petal_length": new_data[2],
                "petal_width": new_data[3],
                "species": new_data[4]
            }, ignore_index=True)
            st.success("Data added successfully!")
        except:
            st.error("Please enter valid numerical values for sepal_length, sepal_width, petal_length, and petal_width")

# display full dataset
st.write("## Full Dataset")
st.write(df)
