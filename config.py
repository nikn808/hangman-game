from pathlib import Path

# --- Путь к файлу со словами ---
BASE_DIR = Path(__file__).resolve().parent

WORDS_FILE = BASE_DIR / "words.json"

# --- Количество ошибок ---
MAX_ERRORS = 6
ERRORS_FOR_HINT = 3