class Iscrizione:
    def __init__(self, matricola, codins):
        self._matricola = matricola
        self._codins = codins

    def __str__(self):
        return f"{self._matricola} - {self._codins}"
