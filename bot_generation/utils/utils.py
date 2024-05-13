import streamlit as st


def bot_selection():
    """Show a bot selection container"""
    st.subheader('Select a chatbot')
    selected_bot = st.selectbox(
        label='Select a bot',
        options=[bot_name for bot_name in st.session_state['bot_manager'].bots.keys()],
        label_visibility='collapsed',
    )
    if selected_bot:
        return st.session_state['bot_manager'].bots[selected_bot]
    else:
        return None
