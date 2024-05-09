import json
import os

from app.database.config import TRANSLATION_PATH


class Languages:
    ru = "ru"
    en = "en"


class LanguageManager:
    def __init__(self, init_language: Languages):
        self.language = init_language

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, new_language):
        self._language = new_language
        self.translations = self.load_language_data()

    def load_language_data(self) -> dict:
        with open(os.path.join(TRANSLATION_PATH, f"{self.language}.json"), 'r', encoding="utf-8") as f_translation:
            return json.load(f_translation)

    def get_translation(self, key: str) -> str:
        return self.translations.get(key, f"Translation not found for key: {key}")
