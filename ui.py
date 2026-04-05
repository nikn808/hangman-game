import os
import locale_ru as lang
from config import ERRORS_FOR_HINT, MAX_ERRORS
from arts import HANGMAN_STAGES
from game_core import GameEngine


class ConsoleUI:
    """Класс отвечает за пользовательский интерфейс."""
    @staticmethod
    def clear_screen() -> None:
        """Очищает консоль."""
        os.system("cls" if os.name == "nt" else "clear")

    def show_main_menu(self) -> str:
        """Отображает главное меню."""
        self.clear_screen()
        menu_text = (
            f"{lang.MENU_TITLE}\n"
            f"{lang.MENU_PLAY}\n"
            f"{lang.MENU_EXIT}"
        )
        print(menu_text)
        return input(lang.MENU_PROMPT).strip()
    
    def draw_game_interface(self, game: GameEngine, turn_status: str = "") -> None:
        """Отрисовывает текущее состояние игры."""
        self.clear_screen()
        wrong_letters_str = ", ".join(sorted(game.wrong_letters)) if game.wrong_letters else lang.LABEL_NONE
        
        interface_parts = [
            lang.TITLE,
            HANGMAN_STAGES[game.errors],
            f"{lang.LABEL_WORD} {game.masked_word}\n",
            f"{lang.LABEL_ERRORS} {game.errors}/{MAX_ERRORS}",
            f"{lang.LABEL_WRONG_LETTERS} {wrong_letters_str}"
        ]
        
        if game.errors >= ERRORS_FOR_HINT:
            interface_parts.append(f"\n{lang.LABEL_HINT} {game.hint}")
        
        print("\n".join(interface_parts))
        
        if turn_status:
            print(f"\n{turn_status}")
    
    def get_user_input(self) -> tuple[str | None, str | None]:
        """Запрашивает ввод у пользователя и проводит его валидацию и нормализацию."""
        user_input = input(lang.PROMPT_INPUT).strip().upper()

        for old_char, new_char in lang.REPLACE_LETTERS.items():
            user_input = user_input.replace(old_char, new_char)
            
        if not user_input:
            return None, lang.ERR_EMPTY_INPUT
            
        if not all(char in lang.ALPHABET for char in user_input):
            return None, lang.ERR_INVALID_CHAR
            
        return user_input, None
    
    def show_game_result(self, game: GameEngine) -> None:
        """Выводит сообщение о победе или поражении."""
        if game.is_won:
            print(lang.MSG_WIN)
        else:
            print(lang.MSG_LOSS)
            print(lang.MSG_HIDDEN_WORD.format(game.word))
        
    def wait_for_enter(self, message: str = lang.MSG_PRESS_ENTER_TO_CONTINUE):
        """Ожидает нажатия Enter."""
        input(message)
            