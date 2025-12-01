from networkx.algorithms import threshold

from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()
        self.lista_hub = []
        self.lista_tratte = []
        self.dizionario_id_hub_nome = {}


    def costruisci_grafo(self,threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        self.G.clear()
        self.lista_hub = DAO.read_hub()
        for hub in self.lista_hub:
            self.dizionario_id_hub_nome[hub.id] = hub  # Chiave: ID, Valore: Oggetto Hub
            self.G.add_node(hub.id)
        self.lista_tratte = DAO.calola_tratta()
        for tratta in self.lista_tratte:
            u_nodo = tratta.id_hub_1
            v_nodo = tratta.id_hub_2
            if tratta.numero_totale_spedizioni > 0:
                guadagno_medio = tratta.valore_totale_merce / tratta.numero_totale_spedizioni
            else:
                guadagno_medio = 0
            if guadagno_medio >= threshold:
                self.G.add_edge(u_nodo, v_nodo, peso=guadagno_medio)
                print(f"Arco aggiunto: {tratta.id_hub_1} - {tratta.id_hub_2} (Peso: {guadagno_medio})")
        return self.G

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges()


    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        lista_archi_con_peso = []
        for u, v, data in self.G.edges(data=True):  # data= true restituisce anche il dizionario dei dati che ho inserito nell'arco
            hub_u = self.dizionario_id_hub_nome[u]
            hub_v = self.dizionario_id_hub_nome[v]
            peso = data['peso']
            lista_archi_con_peso.append((hub_u, hub_v, peso))
        return lista_archi_con_peso


