import importlib

import numpy as np
import streamlit as st

from pandas import DataFrame

from jinja2 import Environment, FileSystemLoader


def generate_bot(bot_name: str, df: DataFrame):
    st.subheader('Data preview')
    st.dataframe(df)
    # EXERCISE

    data = {
        'bot_name': bot_name,
        'intents': [],
    }
    intent_index = 0
    current_intent = None
    for index, row in df.iterrows():
        question = row['question']
        answer = row['answer']
        if answer is not np.nan:  # Next intent
            intent_index += 1
            current_intent = {
                'name': f'question_{intent_index}',
                'sentences': [question],
                'answer': answer
            }
            data['intents'].append(current_intent)
        else:
            current_intent['sentences'].append(question)

    env = Environment(loader=FileSystemLoader(''))
    template = env.get_template('bot_generation/generator/bot_generation.py.j2')
    rendered_code = template.render(data)
    with open(f'bot_generation/bots/{bot_name}.py', 'w') as file:
        file.write(rendered_code)

    gen_module = importlib.import_module(f'bot_generation.bots.{bot_name}')
    return gen_module.bot
