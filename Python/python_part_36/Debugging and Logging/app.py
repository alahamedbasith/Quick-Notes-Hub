# To-Do List Application with Debugging
import streamlit as st

# Initialize tasks list in session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("📝 Simple To-Do List")

# Input for new task
new_task = st.text_input("Enter a new task:")

if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"Task added: {new_task}")
    else:
        st.error("Please enter a task!")

# Display tasks
st.subheader("Your Tasks:")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])
        col1.write(f"{i+1}. {task}")
        if col2.button("❌", key=f"del{i}"):
            st.session_state.tasks.pop(i)
            st.session_state['rerun'] = True

else:
    st.write("No tasks yet! 🎉")
