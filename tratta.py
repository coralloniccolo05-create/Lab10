from dataclasses import dataclass


@dataclass
class Tratta:
    _id_hub_1 : int
    _id_hub_2 : int
    _valore_totale_merce : float
    _numero_totale_spedizioni : int

    @property
    def id_hub_1(self):
        return self._id_hub_1

    @property
    def id_hub_2(self):
        return self._id_hub_2

    @property
    def valore_totale_merce(self):
        return self._valore_totale_merce

    @property
    def numero_totale_spedizioni(self):
        return self._numero_totale_spedizioni

    def __str__(self):
        return f'{self._id_hub_1}, {self._id_hub_2}, {self._valore_totale_merce}, {self._numero_totale_spedizioni}'

    def __hash__(self):
        return hash((self._id_hub_1, self._id_hub_2))


