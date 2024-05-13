# You may need to add your working directory to the Python path. To do so, uncomment the following lines of code
# sys.path.append("/Users/mgomez/Desktop/MARCOS/Git/uni-course-bots")  # Replace with your directory path
import logging
import operator

from besser.bot.core.bot import Bot
from besser.bot.core.entity.entity_entry import EntityEntry
from besser.bot.core.session import Session
from besser.bot.library.entity.base_entities import number_entity
from besser.bot.library.intent.intent_classifier_configuration_library import hf_api_config
from besser.bot.nlp.intent_classifier.intent_classifier_prediction import IntentClassifierPrediction
from pandas import DataFrame

# Configure the logging module
logging.basicConfig(level=logging.INFO, format='{levelname} - {asctime}: {message}', style='{')


class Product:

    def __init__(self, name: str, tags: list[str], price: float):
        self.name = name
        self.tags = tags
        self.price = price


products: dict[str, Product] = {
    'TV Q600': Product('TV Q600', ['Samsung', 'tv', '4k'], 699),
    'iPhone 15': Product('iPhone 15', ['Apple', 'smartphone', 'usb-c'], 1299),
    'Macbook': Product('Macbook', ['Apple', 'laptop', '16 inches'], 1599)
}


# Create the bot
bot = Bot('shop_bot')
# Load bot properties stored in a dedicated file
bot.load_properties('config.ini')
# Define the platform your chatbot will use
websocket_platform = bot.use_websocket_platform(use_ui=True)


product_entity = bot.new_entity('product_entity', entries={product.name: [] for product in products.values()})
tag_entity = bot.new_entity('tag_entity')
for product in products.values():
    tag_entity.entries.extend([EntityEntry(tag) for tag in product.tags])

# STATES

initial_state = bot.new_state('initial_state', initial=True)
awaiting_state = bot.new_state('awaiting_state')
search_state = bot.new_state('search_state')
show_cart_state = bot.new_state('show_cart_state')
add_to_cart_state = bot.new_state('add_to_cart_state')
set_num_units_state = bot.new_state('set_num_units_state')
proceed_payment_state = bot.new_state('proceed_payment_state')
receive_name_state = bot.new_state('receive_name_state')
receive_address_state = bot.new_state('receive_address_state')


# INTENTS


# ...


# STATES BODIES DEFINITION + TRANSITIONS


# ...


# RUN APPLICATION

if __name__ == '__main__':
    bot.run()
