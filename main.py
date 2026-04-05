from game_loop import GameLoop
import locale_ru as lang


def main():
    """Точка входа в приложение."""
    try:
        app = GameLoop()
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{lang.MSG_GOODBYE}")


if __name__ == "__main__":
    main()