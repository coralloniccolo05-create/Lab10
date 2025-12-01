from database.dao import DAO
from model.model import Model

m = Model()
h =m.costruisci_grafo(300)
print(h)