import streamlit as st
import requests

# Page Config details
st.set_page_config(
        page_title = 'MotivationQuotes',
        page_icon = "Ⓜ",
        layout = "wide",
        initial_sidebar_state = "expanded"
    )

def get_random_motivational_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        return f"{quote} - {author}"
    return "Failed to fetch a quote"

def main():
    st.title("Random Motivational Quote Generator")
    st.write("Click the button below to get a dose of motivation!")

    if st.button("Generate Quote"):
        quote = get_random_motivational_quote()
        st.write(f"🚀👉 {quote}")

if __name__ == "__main__":
    main()
