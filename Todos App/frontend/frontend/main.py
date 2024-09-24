import streamlit as st
import requests

api_url = "http://localhost:8000/todos/"

def fetch_todos():
    response = requests.get(api_url)
    return response.json()

def create_todo(title, description):
    new_todo = {
        "id": len(fetch_todos()) + 1,
        "title": title,
        "description": description,
        "completed": False
    }
    response = requests.post(api_url, json=new_todo)
    return response.json()

st.title("Todo App")

if st.button("Refresh Todos"):
    todos = fetch_todos()
    for todo in todos:
        st.write(f"{todo['title']}: {todo['description']} - {'Completed' if todo['completed'] else 'Incomplete'}")

with st.form("create_todo"):
    title = st.text_input("Title")
    description = st.text_input("Description")
    submitted = st.form_submit_button("Add Todo")
    if submitted:
        create_todo(title, description)
        st.success("Todo added!")
