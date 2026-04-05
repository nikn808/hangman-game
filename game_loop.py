from word_provider import WordProvider
from game_core import GameEngine
from ui import ConsoleUI
import locale_ru as lang


class GameLoop:
    """Класс управляет основным циклом, меню и созданием игровых сессий."""
    def __init__(self) -> None:
        self.ui = ConsoleUI()
        self.provider = WordProvider()

    def _play_game_session(self):
        """Запускает и управляет одной игровой сессией."""
        word_data = self.provider.get_random_word()
        game = GameEngine(word_data)
        turn_status = ""

        while not game.is_game_over:
            self.ui.draw_game_interface(game, turn_status)
            user_input, error = self.ui.get_user_input()
            
            if error:
                turn_status = error
                continue

            if len(user_input) == 1:
                result = game.guess_letter(user_input)
                if result == "correct":
                    turn_status = lang.STATUS_CORRECT
                elif result == "wrong":
                    turn_status = lang.STATUS_WRONG
                elif result == "exists":
                    turn_status = lang.STATUS_ALREADY_GUESSED
            else:
                game.guess_word(user_input)
                turn_status = ""
        
        self.ui.draw_game_interface(game, turn_status)
        self.ui.show_game_result(game)

    def run(self):
        """Запускает главный цикл приложения с меню."""
        while True:
            choice = self.ui.show_main_menu()
            
            if choice == '1':
                self._play_game_session()
                self.ui.wait_for_enter()
            elif choice == '2':
                print(f"\n{lang.MSG_GOODBYE}")
                break
            else:
                self.ui.wait_for_enter(lang.MENU_INVALID_CHOICE)

    