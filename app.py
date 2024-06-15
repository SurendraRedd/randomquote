import streamlit as st
import requests

# Page Configuration details
st.set_page_config(
    page_title='MotivationQuotes',
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to get a random motivational quote
def get_random_motivational_quote():
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        return f"“{quote}”\n\n— {author}"
    except requests.exceptions.RequestException as e:
        st.error("Failed to fetch a quote")
        return None

# Main function to render the Streamlit app
def main():
    st.title("🌟 Motivational Quotes 🌟")
    st.write("Need a dose of motivation? Click the button below to get inspired!")

    if st.button("✨ Generate Quote ✨"):
        quote = get_random_motivational_quote()
        if quote:
            st.write(f"🚀 👉 {quote}")
        else:
            st.error("Oops! Something went wrong while fetching the quote. Please try again.")

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app fetches random motivational quotes from ZenQuotes API.
        
        Created with ❤️ using [Streamlit](https://streamlit.io).
        """
    )

if __name__ == "__main__":
    main()

