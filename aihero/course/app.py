import streamlit as st
import ingest
import search_agent


# ---------- Initialization ----------
@st.cache_resource
def init_agent():
    repo_owner = "DataTalksClub"
    repo_name = "faq"

    def filter(doc):
        return "data-engineering" in doc["filename"]

    st.write("🔄 Indexing repo...")
    index = ingest.index_data(
        repo_owner,
        repo_name,
        filter=filter,
    )

    return search_agent.init_agent(
        index,
        repo_owner,
        repo_name,
    )


agent = init_agent()


# ---------- UI ----------
st.set_page_config(
    page_title="AI FAQ Assistant",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 AI FAQ Assistant")
st.caption("Ask me anything about the DataTalksClub/faq repository")


# ---------- Session State ----------
if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------- Display History ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# ---------- Chat ----------
if prompt := st.chat_input("Ask your question..."):

    # User message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response_text = search_agent.ask_agent(
                    agent,
                    prompt,
                )

                st.markdown(response_text)

            except Exception as e:
                import traceback
                traceback.print_exc()

                response_text = f"❌ Error: {e}"
                st.error(response_text)

    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response_text,
        }
    )