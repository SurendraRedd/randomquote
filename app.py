import streamlit as st
import requests
import random

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
    # Background color
    page_bg_img = '''
    <style>
    body {
        background-image: url("https://www.transparenttextures.com/patterns/cubes.png");
        background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Title with animation
    st.markdown(
        f"""
        <h1 style='text-align: center; color: #ff6347; font-size: 60px;'>
            <span class="wave">🌟</span> Motivational Quotes <span class="wave">🌟</span>
        </h1>
        <style>
        @keyframes wave {{
            0% {{ transform: rotate(0.0deg) }}
            10% {{ transform: rotate(14deg) }}
            20% {{ transform: rotate(-8deg) }}
            30% {{ transform: rotate(14deg) }}
            40% {{ transform: rotate(-4deg) }}
            50% {{ transform: rotate(10.0deg) }}
            60% {{ transform: rotate(0.0deg) }}
            100% {{ transform: rotate(0.0deg) }}
        }}
        .wave {{
            display: inline-block;
            animation: wave 2s infinite;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.write("Need a dose of motivation? Click the button below to get inspired!")

    if st.button("✨ Generate Quote ✨"):
        quote = get_random_motivational_quote()
        if quote:
            st.markdown(
                f"""
                <div style='text-align: center; font-size: 30px; color: #6a5acd;'>
                    🚀 👉 {quote}
                </div>
                """,
                unsafe_allow_html=True,
            )
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
