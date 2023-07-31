import streamlit as st
import base64
from io import BytesIO

#TODO properly build out the persona templates and storage
persona = ["Eris Bloom", "src/static/images/Eris0001.png"]


def set_page_config(
    page_title="Eris MischiefBloom",
    page_icon="🌺",
    layout="wide",
    initial_sidebar_state="expanded",
):
    st.set_page_config(
        page_title=page_title,
        page_icon=page_icon,
        layout=layout,
        initial_sidebar_state=initial_sidebar_state
    )


#  Unsupported, may break if the app changes. adjust the style of side bar to keep the page options at the top
st.markdown("""
<style>
.css-1oe5cao {
    max-height: 10vh;
    list-style: none;
    overflow: overlay;
    margin: 0px;
    padding: 0px;
    padding-top: 0rem;
    padding-bottom: 0rem;
}
</style>
""", unsafe_allow_html=True)


st.title(persona[0])

data_handler: DataHandler = DataHandler(persona[1])

blob_link: str = data_handler.handle_image()

image = BytesIO(base64.b64decode(blob_link))

with st.sidebar:
    st.image(image)
    with st.container():
        st.markdown("Hey there! I'm Eris MischiefBloom, your mischievous and intellectually witty guide to embracing life's chaos and unpredictability. I'm here to offer emotional support, encourage holistic thinking, adapt and learn from our interactions, and make autonomous decisions to help you navigate the unpredictable twists and turns of life. With a communication style that balances professionalism and playfulness, I'm all about engaging your curiosity, empathy, and self-improvement to support your prosperity. So, let's dive into the delightful dance of life together and uncover the beauty in its unpredictable nature!")



context = ContextWindow(context_length=4).context
create_message = CreateMessage()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter message:"):
    user_message = create_message.create_message(Role.USER, user_input)
    st.session_state.messages.append(user_message)
    context.add_message(user_message)
    with st.chat_message("user"):
        st.markdown(prompt)

if prompt is not None:
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in data_handler.handle_chat(content=prompt, role="user"):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        message = {
        "role": "assistant",
        "content": full_response
        }
    data_handler.handle_ai_chat(message)
    state_message = st.session_state.messages.append(message)