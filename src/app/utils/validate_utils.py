import calendar

from inquirer import errors

from app.core.language_manager import LanguageManager


def get_days_in_month(year: int, month: int) -> int:
    return calendar.monthrange(year=year, month=month)[1]


def validate_amount(amount: str, language_manager: LanguageManager) -> bool:
    min_border = 1
    if not (amount.isdecimal() and min_border <= int(amount)):
        raise errors.ValidationError("", reason=f"{language_manager.get_translation("number-input-error")}")
    return True


def validate_year(year: str, language_manager: LanguageManager) -> bool:
    min_border, max_border = 1, 9999
    if not (year.isdecimal() and min_border <= int(year) <= max_border):
        raise errors.ValidationError("", reason=f"{language_manager.get_translation("number-input-in-range-error")} " +
                                                f"[{min_border}; {max_border}].")
    return True


def validate_month(month: str, language_manager: LanguageManager) -> bool:
    min_border, max_border = 1, 12
    if not (month.isdecimal() and min_border <= int(month) <= max_border):
        raise errors.ValidationError("", reason=f"{language_manager.get_translation("number-input-in-range-error")} " +
                                                f"[{min_border}; {max_border}].")
    return True


def validate_day(year: int, month: int, day: str, language_manager: LanguageManager) -> bool:
    min_border, max_border = 1, get_days_in_month(year, month)
    if not (day.isdecimal() and min_border <= int(day) <= max_border):
        raise errors.ValidationError("", reason=f"{language_manager.get_translation("number-input-in-range-error")} " +
                                                f"[{min_border}; {max_border}].")
    return True
