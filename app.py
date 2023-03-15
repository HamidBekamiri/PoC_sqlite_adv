import streamlit as st
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create the "users" table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        age INTEGER
    )
''')
conn.commit()

# Define Streamlit app
def app():
    # Title
    st.title("User Database App")

    # Sidebar menu
    menu = ["Add User", "Search Users"]
    choice = st.sidebar.selectbox("Select an action", menu)

    # Add User
    if choice == "Add User":
        # Form to add a new user
        st.header("Add New User")
        name = st.text_input("Name")
        age = st.number_input("Age")
        if st.button("Add User"):
            # Add the user to the database
            c.execute("INSERT INTO users VALUES (?, ?)", (name, age))
            conn.commit()
            st.success("User added successfully!")

    # Search Users
    elif choice == "Search Users":
        # Form to search for users
        st.header("Search Users")
        search_term = st.text_input("Search term")
        if st.button("Search"):
            # Search for users in the database
            c.execute("SELECT * FROM users WHERE name LIKE ?", ('%'+search_term+'%',))
            results = c.fetchall()
            if results:
                st.table(results)
            else:
                st.warning("No users found.")
