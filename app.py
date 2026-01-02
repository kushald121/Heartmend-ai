from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.media import Image as AgnoImage
from pathlib import Path
import streamlit as st
import tempfile
import os
import logging

# Logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Page config
st.set_page_config(
    page_title="💔 Breakup Recovery Squad",
    page_icon="💔",
    layout="wide"
)

# Title
st.title("💔 Breakup Recovery Squad")
st.markdown("""
### Your AI-powered breakup recovery team is here to help!
Share your feelings and chat screenshots, and we'll guide you through this.
""")

# ---------------- AGENT INITIALIZATION ---------------- #

with st.sidebar:
    st.title("API Key:")
    
    with st.expander("Enter you OpenRouter API Key:"):
        OPENROUTER_API_KEY=st.text_area("Enter the key",height=100, placeholder="Openrouter Api key")

def initialize_agents():
    try:
        if not OPENROUTER_API_KEY:
            st.error("Please enter your OpenRouter API Key.")
            return None,None,None,None
        model = OpenRouter(id="mistralai/devstral-2512:free",
                           api_key=OPENROUTER_API_KEY)

        therapist_agent = Agent(
            model=model,
            name="Therapist Agent",
            instructions=[
                "You are an empathetic therapist.",
                "Validate feelings and offer gentle comfort.",
                "Analyze both text and image inputs."
            ],
            markdown=True
        )

        closure_agent = Agent(
            model=model,
            name="Closure Agent",
            instructions=[
                "Help express unsent emotions.",
                "Create heartfelt closure messages."
            ],
            markdown=True
        )

        routine_planner_agent = Agent(
            model=model,
            name="Routine Planner Agent",
            instructions=[
                "Create a 7-day emotional recovery plan.",
                "Include self-care and healing activities."
            ],
            markdown=True
        )

        try:
            # Initialize DuckDuckGoTools and extract the required tool names
            duckduckgo_tools = DuckDuckGoTools()
            tools_list = ["duckduckgo_search", "duckduckgo_news"]  # Pass tool names as strings
            brutal_honesty_agent = Agent(
                model=model,
                tools=tools_list,
                name="Brutal Honesty Agent",
                instructions=[
                    "Give honest, objective relationship feedback.",
                    "Explain why moving on is necessary."
                ],
                markdown=True
            )
        except Exception as e:
            st.warning(f"DuckDuckGoTools failed to initialize: {e}. Brutal Honesty Agent will be disabled.")
            brutal_honesty_agent = None

        return therapist_agent, closure_agent, routine_planner_agent, brutal_honesty_agent

    except Exception as e:
        st.error(f"Agent initialization failed: {e}")
        return None, None, None, None


# ---------------- IMAGE PROCESSING ---------------- #

def process_images(files):
    processed_images = []

    for file in files:
        try:
            temp_dir = tempfile.gettempdir()
            temp_path = os.path.join(temp_dir, f"temp_{file.name}")

            with open(temp_path, "wb") as f:
                f.write(file.getvalue())

            agno_image = AgnoImage(filepath=Path(temp_path))
            processed_images.append(agno_image)

        except Exception as e:
            logger.error(f"Error processing image {file.name}: {e}")

    return processed_images


# ---------------- INPUT UI ---------------- #

col1, col2 = st.columns(2)

with col1:
    st.subheader("💬 Share your feelings")
    user_input = st.text_area(
        "What happened?",
        height=150,
        placeholder="Tell your story..."
    )

with col2:
    st.subheader("🖼 Upload Chat Screenshots")
    uploaded_files = st.file_uploader(
        "Upload images (optional)",
        type=["jpg", "png", "jpeg"],
        accept_multiple_files=True
    )

    if uploaded_files:
        for file in uploaded_files:
            st.image(file, caption=file.name, use_container_width=True)


# ---------------- MAIN ACTION ---------------- #

if st.button("Get Recovery Plan 💖", type="primary"):

    if not user_input and not uploaded_files:
        st.warning("Please share your feelings or upload screenshots.")
        st.stop()

    therapist_agent, closure_agent, routine_planner_agent, brutal_honesty_agent = initialize_agents()

    if not all([therapist_agent, closure_agent, routine_planner_agent, brutal_honesty_agent]):
        st.stop()

    all_images = process_images(uploaded_files) if uploaded_files else []

    try:
        # Therapist
        with st.spinner("🤗 Providing emotional support..."):
            response = therapist_agent.run(
                input=f"User feelings: {user_input}",
                images=all_images
            )
            st.subheader("🤗 Emotional Support")
            st.markdown(response.content)

        # Closure
        with st.spinner("✍️ Crafting closure messages..."):
            response = closure_agent.run(
                input=f"Help create closure for: {user_input}",
                images=all_images
            )
            st.subheader("✍️ Finding Closure")
            st.markdown(response.content)

        # Routine
        with st.spinner("📅 Creating recovery plan..."):
            response = routine_planner_agent.run(
                input=f"Create a 7-day recovery plan for: {user_input}",
                images=all_images
            )
            st.subheader("📅 Your Recovery Plan")
            st.markdown(response.content)

        # Brutal honesty
        with st.spinner("💪 Getting honest perspective..."):
            response = brutal_honesty_agent.run(
                input=f"Give honest advice for: {user_input}",
                images=all_images
            )
            st.subheader("💪 Honest Perspective")
            st.markdown(response.content)

    except Exception as e:
        logger.error(e)
        st.error("Something went wrong during analysis.")


# ---------------- FOOTER ---------------- #

st.markdown("---")
st.markdown(
    "<div style='text-align:center'>💖 You are not alone. Healing takes time.</div>",
    unsafe_allow_html=True
)
