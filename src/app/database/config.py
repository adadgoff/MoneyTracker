from os.path import abspath

TRANSLATION_PATH = abspath("resources/translations")

DATABASE_PATH = abspath("resources/databases")
ENTRY_DATABASE_PATH = DATABASE_PATH + r"\entry.csv"
USER_DATABASE_PATH: str = DATABASE_PATH + r"\user.csv"

DELIMITER = ','
