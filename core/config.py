import json
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Config:
    """Class for managing application settings using a JSON file."""

    DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config_default.json')
    USER_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config_user.json')

    def __init__(self):
        self.default_config = self.load_default_config()
        self.user_config = self.load_user_config()

    def load_default_config(self):
        """Load default config or create it"""
        return self._load_json(self.DEFAULT_CONFIG_PATH, {})

    def load_user_config(self):
        """Load user config or return empty object"""
        return self._load_json(self.USER_CONFIG_PATH, {})

    @staticmethod
    def _load_json(path, default):
        """Load configuration from file or create a default config."""
        if not os.path.exists(path):
            logging.warning(f"File {path} not found. Use empty value")
            return default
        try:
            with open(path, "r", encoding="UTF-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            logging.error(f'Error reading {path}. Use empty config.')
            return default

    def save_user_config(self):
        """Save user config file(only changed value)."""
        with open(self.USER_CONFIG_PATH, "w", encoding="UTF-8") as file:
            json.dump(self.user_config, file, indent=4)
        logging.info(f'User settings saved.')

    def get(self, key):
        """Get value of setting: user config first"""
        return self.user_config.get(key, self.default_config.get(key))

    def set(self, key, value):
        """Update user setting and save changes"""
        self.user_config[key] = value
        self.save_user_config()
        logging.info(f'Setting updated: {key} -> {value}.')
