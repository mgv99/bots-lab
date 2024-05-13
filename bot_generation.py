import streamlit as st
import sys
from streamlit.web import cli as stcli

from bot_generation.generator.bot_manager import BotManager
from bot_generation.ui.chatbot_ui import chatbot_ui
from bot_generation.ui.generator_ui import generator_ui
from bot_generation.ui.sidebar import sidebar_menu
from bot_generation.utils.utils import bot_selection

st.set_page_config(layout="wide")

if __name__ == "__main__":
    if st.runtime.exists():
        if 'bot_manager' not in st.session_state:
            st.session_state['bot_manager'] = BotManager()
        with st.sidebar:
            page = sidebar_menu()
        if page == 'Generator':
            generator_ui()
        elif page == 'Chatbots':
            with st.sidebar:
                bot = bot_selection()
            if bot:
                chatbot_ui(bot)
            else:
                st.info('Go to the Generator tab to create a bot')
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
