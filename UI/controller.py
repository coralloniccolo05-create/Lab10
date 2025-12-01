import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO

        soglia_input = self._view.guadagno_medio_minimo.value


        try:
            soglia = float(soglia_input)
        except Exception as e:
            self._view.lista_visualizzazione.controls.clear()
            self._view.show_alert(e)
            self._view.update()
            return

        self._model.costruisci_grafo(soglia)

        n_nodi = self._model.get_num_nodes()
        n_archi = self._model.get_num_edges()
        all_edges = self._model.get_all_edges()

        self._view.lista_visualizzazione.controls.clear()

        self._view.lista_visualizzazione.controls.append(ft.Text(f"Grafo correttamente creato."))
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Nodi (Hub): {n_nodi}"))
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Archi (Tratte): {n_archi}"))

        for u, v, peso in all_edges:
            nome_partenza = u.nome
            stato_partenza = u.stato
            nome_arrivo = v.nome
            stato_arrivo = v.stato
            riga = f"{nome_partenza} ({stato_partenza}) -> {nome_arrivo} ({stato_arrivo}) | Guadagno: {peso:.2f} €"
            self._view.lista_visualizzazione.controls.append(ft.Text(riga))

        self._view.update()
