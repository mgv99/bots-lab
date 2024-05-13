import importlib

import numpy as np
import streamlit as st

from pandas import DataFrame

from jinja2 import Environment, FileSystemLoader


def generate_bot(bot_name: str, df: DataFrame):
    st.subheader('Data preview')
    st.dataframe(df)
    data = {}

    ##################
    # YOUR CODE HERE #
    ##################

    env = Environment(loader=FileSystemLoader(''))
    template = env.get_template('bot_generation/generator/bot_generation.py.j2')
    rendered_code = template.render(data)
    with open(f'bot_generation/bots/{bot_name}.py', 'w') as file:
        file.write(rendered_code)

    gen_module = importlib.import_module(f'bot_generation.bots.{bot_name}')
    return gen_module.bot
