from config import MAX_ERRORS


class GameEngine:
    """Класс отвечающий за игровую логику "Виселицы"."""
    def __init__(self, word_data: dict[str, str]) -> None:
        self.word: str = word_data["word"]
        self.hint: str = word_data["hint"]
        
        self.errors: int = 0
        self.guessed_letters: set[str] = set()
        self.wrong_letters: set[str] = set()

    @property
    def is_won(self) -> bool:
        """Проверяет, выиграл ли игрок."""
        return set(self.word).issubset(self.guessed_letters)

    @property
    def is_lost(self) -> bool:
        """Проверяет, проиграл ли игрок."""
        return self.errors >= MAX_ERRORS

    @property
    def is_game_over(self) -> bool:
        """Проверяет, завершена ли игра (победа или поражение)."""
        return self.is_won or self.is_lost
    
    @property
    def masked_word(self) -> str:
        """Возвращает зашифрованное слово."""
        return " ".join(letter if letter in self.guessed_letters else "_" for letter in self.word)

    def guess_letter(self, letter: str) -> str:
        """Обрабатывает попытку угадать букву."""
        if letter in self.guessed_letters or letter in self.wrong_letters:
            return "exists"

        if letter in self.word:
            self.guessed_letters.add(letter)
            return "correct"
        else:
            self.wrong_letters.add(letter)
            self.errors += 1
            return "wrong"

    def guess_word(self, word: str) -> bool:
        """Обрабатывает попытку угадать слово целиком."""
        if word == self.word:
            self.guessed_letters.update(self.word)
            return True
        else:
            self.errors = MAX_ERRORS
            return False