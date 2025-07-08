import streamlit as st
import openai

# 🌈 Set up Streamlit page config
st.set_page_config(page_title="Indian Event Post Generator", page_icon="🎉", layout="centered")

# 🎨 Custom CSS styling for blue & yellow UI
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;
    }
    .stApp {
        background-color: #fdfdfd;
        color: #333;
    }
    .title-style {
        color: #1f77b4;
        text-align: center;
        font-size: 32px;
        font-weight: bold;
    }
    .subheader-style {
        color: #ffcc00;
        font-size: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 🎉 App Title
st.markdown('<div class="title-style">🎨 Indian Event Social Media Post Generator 🎭</div>', unsafe_allow_html=True)
st.markdown("###")

# 🔐 Step 1: Ask for OpenAI API Key
api_key = st.text_input("🔐 Step 1: Enter your OpenAI API Key", type="password")

if api_key:
    # ✅ Setup OpenAI client (compatible with v1.0.0+)
    client = openai.OpenAI(api_key=api_key)

    # 📅 Step 2: Show dropdown of upcoming events
    upcoming_events = [
        "Diwali",
        "Holi",
        "Raksha Bandhan",
        "Independence Day",
        "Ganesh Chaturthi",
        "Navratri",
        "Eid-ul-Fitr",
        "Christmas"
    ]

    selected_event = st.selectbox("👇 Step 2: Choose an upcoming event in India", upcoming_events)

    # 📝 Step 3: Confirm/edit event text input (autofilled)
    event_name = st.text_input("🎯 Step 3: Confirm or edit your event name", value=selected_event)

    # 🚀 Step 4: Generate Button
    if st.button("✨ Generate Fun Social Media Posts"):
        prompt = f"""
        Generate 3 fun, witty, and sarcastic social media posts for the event '{event_name}'.
        One for LinkedIn, one for Twitter, and one for WhatsApp. Keep each post platform-appropriate.

        Also, include a humorous or surprising anecdote about how people celebrate '{event_name}' in different cultures.
        Make it entertaining, clever, and punchy – something people would enjoy reading or sharing.
        """

        try:
            with st.spinner("Crafting posts with AI magic... 💫"):
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.9
                )

                output = response.choices[0].message.content
                st.markdown("## 🧠 AI-Generated Posts")
                st.success(output)

        except Exception as e:
            st.error(f"Oops! Something went wrong:\n\n{str(e)}")
else:
    st.warning("🔑 Please enter your OpenAI API key to begin.")
