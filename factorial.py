def factorial(n):
    if n < 0:
        return "No factorial for negative numbers"
    if n == 0 or n == 1:
        return 1
    result = n
    for i in range(1, n):
        result *= i
    return result
def main():
    import streamlit as st
    st.title("Factorial Calculator")
    number = st.number_input("Enter a number", min_value = 0, max_value = 900)
    if st.button("Calculate Factorial"):
        result = factorial(number)
        st.write(f"The factorial of {number} is: {result}")
if __name__ == "__main__":
    main()