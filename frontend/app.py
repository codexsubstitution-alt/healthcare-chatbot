import requests
import streamlit as st

API_ROOT = "http://127.0.0.1:8000"
CHAT_URL = f"{API_ROOT}/chat"
FEEDBACK_URL = f"{API_ROOT}/feedback"
BLUEPRINT_URL = f"{API_ROOT}/blueprint"


def load_blueprint():
    try:
        response = requests.get(BLUEPRINT_URL, timeout=30)
        response.raise_for_status()
        return response.json(), None
    except requests.RequestException as exc:
        return None, str(exc)


blueprint, blueprint_error = load_blueprint()

if not blueprint:
    st.set_page_config(page_title="Generated Project", layout="wide")
    st.title("Generated Project")
    st.error(f"Could not load backend blueprint: {blueprint_error}")
    st.info("Start the backend first with: python -m uvicorn backend.main:app --reload")
    st.stop()

st.set_page_config(page_title=blueprint["project_name"], layout="wide")
st.title(blueprint["project_name"])
st.caption(blueprint["tagline"])
st.write(blueprint["primary_goal"])

tabs = st.tabs(["Assistant", "Blueprint", "Feedback"])

with tabs[0]:
    left, right = st.columns([1.3, 1])
    with left:
        message = st.text_area(
            "Message",
            placeholder=blueprint["sample_inputs"][0],
            height=160,
        )

        if st.button("Generate Response", use_container_width=True):
            if not message.strip():
                st.warning("Enter a message first.")
            else:
                response = requests.post(CHAT_URL, json={"message": message}, timeout=30)
                if response.status_code == 200:
                    data = response.json()
                    st.success(data["answer"])
                    st.subheader("Suggested Follow-ups")
                    for item in data["suggestions"]:
                        st.write(f"- {item}")
                    st.subheader("Next Steps")
                    for item in data["next_steps"]:
                        st.write(f"- {item}")
                else:
                    st.error("Backend request failed.")

    with right:
        st.subheader("Sample Inputs")
        for item in blueprint["sample_inputs"]:
            st.write(f"- {item}")

        st.subheader("Core Features")
        for item in blueprint["core_features"]:
            st.write(f"- {item}")

with tabs[1]:
    st.json(blueprint)

with tabs[2]:
    name_input = st.text_input("Name", value="Anonymous")
    rating = st.slider("Rating", min_value=1, max_value=5, value=5)
    comment = st.text_area("Comment", height=120)
    if st.button("Save Feedback", use_container_width=True):
        response = requests.post(
            FEEDBACK_URL,
            json={"name": name_input, "rating": rating, "comment": comment},
            timeout=30,
        )
        if response.status_code == 200:
            st.success("Feedback saved.")
        else:
            st.error("Could not save feedback.")
