from app.app_main import App
from app.core.language_manager import Languages

if __name__ == "__main__":
    app = App(Languages.ru)
    app.run()
