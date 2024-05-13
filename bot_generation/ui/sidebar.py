import streamlit_antd_components as sac


def sidebar_menu():
    page = sac.menu([
        sac.MenuItem('Generator', icon='file-earmark-arrow-up'),
        sac.MenuItem('Chatbots', icon='robot'),
    ], open_all=True)
    return page

