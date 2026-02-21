class ValidUser:
    """ЗАДАЧА: Сеттер пароля с проверкой длины >= 8 и наличия цифр"""
    def __init__(self, user, pwd): self.username, self._password = user, pwd
    @property

    def password(self): return "********"

    @password.setter
    def password(self, val):
        if len(val) < 8:
            return
        if not any(ch.isdigit() for ch in val):
            return
        self._password = val