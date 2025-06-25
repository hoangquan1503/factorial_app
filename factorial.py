import os
import streamlit as st

def load_users():
    try:
        if os.path.exists("users.txt"):
            with open("users.txt", "r", encoding = "utf-8") as f:
                users = [line.strip() for line in f.readlines() if line.strip()]
            return users
        else:
            st.error("Users file not found.")
            return []
    except Exception as e:
        st.error(f"An error occurred while reading file users: {e}")
        return []
def login_page():
    st.title("Login Page")
    username = st.text_input("Username: ")
    if username:
        if st.button("Login"):
            users = load_users()
            if username in users:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else :
                st.session_state.show_greeting  = True
                st.session_state.username = username
                st.rerun()
    else :
        st.warning("Please enter a username.")
        
    
def factorial(n):
    if n < 0:
        return "No factorial for negative numbers"
    if n == 0 or n == 1:
        return 1
    result = n
    for i in range(1, n):
        result *= i
    return result
def factorial_page():
    
    st.title("Factorial Calculator")
    st.write("Hi, " + st.session_state.username + "! Welcome to the Factorial Calculator.")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()
    st.divider()
    number = st.number_input("Enter a number", min_value = 0, max_value = 900)
    if st.button("Calculate Factorial"):
        result = factorial(number)
        st.write(f"The factorial of {number} is: {result}")
def greeting_page():
    st.title("Hi, " + st.session_state.username )
    st.write("You do not have permission to access the calculator")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.show_greeting = False
        st.session_state.username = ""
        st.rerun()
def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "show_greeting" not in st.session_state:
        st.session_state.show_greeting = False

    if st.session_state.logged_in:
        factorial_page()
    elif st.session_state.show_greeting:
        greeting_page()
    else:
        login_page()
if __name__ == "__main__":
    main()
    