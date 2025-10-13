import re
from typing import List
from Person import Person
from Email import Email

class PersonDAO:
    _storage: List[Person] = []

    @staticmethod
    def isValidToInclude(p: Person) -> List[str]:
        erros: List[str] = []
        partes = [parte for parte in (p.name or "").strip().split(" ") if parte]
        if len(partes) < 2:
            erros.append("Nome deve conter ao menos duas partes.")
        for parte in partes:
            if not parte.isalpha():
                erros.append("Nome deve conter apenas letras em cada parte.")
                break
        if not isinstance(p.age, int) or p.age < 1 or p.age > 200:
            erros.append("Idade deve estar no intervalo [1, 200].")
        if not p.emails:
            erros.append("Pessoa deve possuir ao menos um e-mail associado.")
        email_regex = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
        for e in p.emails:
            if not email_regex.match(e.name or ""):
                erros.append(f"E-mail inválido: {e.name!r}. Formato esperado: parte@parte.parte.")
        return erros

    def save(self, p: Person) -> None:
        erros = self.isValidToInclude(p)
        if erros:
            raise ValueError(f"Objeto Person inválido: {erros}")
        self._storage.append(p)

    @classmethod
    def clear_storage(cls) -> None:
        cls._storage.clear()

    @classmethod
    def all(cls) -> List[Person]:
        return list(cls._storage)
