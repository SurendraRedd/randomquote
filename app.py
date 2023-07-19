import streamlit as st
import random

def get_random_motivational_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "The future starts today, not tomorrow. - Pope John Paul II"
    ]
    return random.choice(quotes)

def main():
    st.title("Random Motivational Quote Generator")
    st.write("Click the button below to get a dose of motivation!")

    if st.button("Generate Quote"):
        quote = get_random_motivational_quote()
        st.write(f"🚀 {quote}")

if __name__ == "__main__":
    main()
