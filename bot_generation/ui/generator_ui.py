import pandas as pd
import streamlit as st

from bot_generation.generator.bot_generator import generate_bot


def generator_ui():
    st.header('Chatbot generator')
    with st.form('upload_data', clear_on_submit=True):
        st.subheader('Import a csv file')
        bot_name = st.text_input(label='Bot name', placeholder='Example: sales_bot')
        uploaded_file = st.file_uploader(label="Choose a file", type='csv')
        # if uploaded_file is not None:
        submitted = st.form_submit_button(label="Create bot", type='primary')
        if submitted:
            if uploaded_file is None:
                st.error('Please add a dataset')
            else:
                if bot_name is None or bot_name == '':
                    bot_name = uploaded_file.name[:-4]  # remove .csv file extension
                if bot_name in st.session_state['bot_manager'].bots:
                    st.error(f"The bot name '{bot_name}' already exists. Please choose another one")
                else:
                    with st.spinner('Generating the bot'):
                        bot = generate_bot(bot_name, pd.read_csv(uploaded_file))
                    if bot:
                        st.info(f'The bot **{bot.name}** has been created!')
                        with st.spinner('Training the bot'):
                            st.session_state['bot_manager'].add_bot(bot)
                            bot.run(sleep=False)
                        st.info(f'The bot **{bot.name}** is now running!')
                    else:
                        st.error('The bot was not generated')
