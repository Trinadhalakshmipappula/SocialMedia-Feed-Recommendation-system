
import streamlit as st
import requests
API_URL = "https://socialmedia-feed-recommendation-system.onrender.com"


st.set_page_config(page_title="Personalized Feed", layout="centered")

# ----------------- Custom CSS -----------------
st.markdown("""
<style>
            
            
/* Post titles */
.stContainer h3 {
    margin-bottom: 5px;
}

/* Post details */
.stContainer p {
    margin: 2px 0;
}

/* Page background */
body {
    background: linear-gradient(to right, #fbc2eb, #a6c1ee);
}

/* Title styling */
h1 {
    color: #4B0082;
    font-family: 'Arial Black', sans-serif;
    text-align: center;
}

/* Text input box styling */
input[type="text"] {
    border: 2px solid #4B0082;
    border-radius: 10px;
    padding: 10px;
    font-size: 16px;
}

/* Button styling */
.stButton>button {
    background: linear-gradient(to right, #ff7e5f, #feb47b);
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    background: linear-gradient(to right, #6a11cb, #2575fc);
    transform: scale(1.05);
}

/* Recommendation container */
.stContainer {
    background: #ffffff90;
    border-radius: 15px;
    padding: 15px;
    margin-bottom: 10px;
    box-shadow: 3px 3px 10px rgba(0,0,0,0.2);
}

/* Divider styling */
hr {
    border: 1px solid #4B0082;
}
</style>
""", unsafe_allow_html=True)

# ----------------- App Title -----------------
st.title("📱 Personalized Feed Recommendation System")

# ----------------- User Input -----------------
user_id = st.number_input("Enter User ID", min_value=1, step=1)

# ----------------- Get Recommendations -----------------
if st.button("Get Recommendations"):

    try:
        response = requests.get(f"{API_URL}/feed/{user_id}")
        data = response.json()

        if data["status"] == "success":
            results = data["recommended_posts"]
        else:
            results = []

    except:
        st.error("API not responding. Please wait 30 seconds and try again.")
        results = []


    if results:
        st.success(f"Show Recommendations for user {user_id}")

        for post in results:
            with st.container():
                st.markdown(f"""
                <div class="stContainer">
                    <h3>📌 Post ID: {post['post_id']}</h3>
                    <p>🏷 <b>Topic:</b> {post['topic']}</p>
                    <p>🎬 <b>Content Type:</b> {post['content_type']}</p>
                </div>
                """, unsafe_allow_html=True)
                st.divider()

    else:
        st.error("No recommendations found.")
