from dataclasses import dataclass

@dataclass
class Hub:
    _id: int
    _nome: str
    _stato: str

    def __str__(self):
        return f'{self.nome} {self.stato}'

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def stato(self):
        return self._stato

    def __hash__(self):
        return hash(self._id)
