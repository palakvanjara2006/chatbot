import logging
import os

# Make sure 'logs' directory exists
os.makedirs('logs', exist_ok=True)

# Setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create file handler
handler = logging.FileHandler("logs/rasa_actions.log")
handler.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(handler)
