import json
import random

from config import WORDS_FILE
import locale_ru as lang


class WordProvider:
    def __init__(self) -> None:
        self.words = self._load_words()

    def _load_words(self) -> list[dict[str, str]]:
        """Читает JSON, валидирует структуру."""
        try:
            with open(WORDS_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                
            if not isinstance(data, list):
                return [lang.FALLBACK_WORD]
                
            valid_words =[]
            
            for item in data:
                if not isinstance(item, dict):
                    continue
                word_raw = item.get("word")
                hint_raw = item.get("hint")
                if not isinstance(word_raw, str) or not isinstance(hint_raw, str):
                    continue
                word = word_raw.strip().upper()
                for old_char, new_char in lang.REPLACE_LETTERS.items():
                    word = word.replace(old_char, new_char)
                if not word or not all(char in lang.ALPHABET for char in word):
                    continue
                valid_words.append({
                    "word": word,
                    "hint": hint_raw.strip()
                })
            
            if not valid_words:
                return [lang.FALLBACK_WORD]
            return valid_words
            
        except (FileNotFoundError, json.JSONDecodeError):
            return [lang.FALLBACK_WORD]

    def get_random_word(self) -> dict[str, str]:
        """Возвращает случайное слово в формате словаря с ключами 'word' и 'hint'"""
        return random.choice(self.words)