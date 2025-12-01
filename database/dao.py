import UI
from database.DB_connect import DBConnect
from hub import Hub

from tratta import Tratta


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    @staticmethod
    def read_hub():
        conn = DBConnect.get_connection()
        lista_hub = []
        query = '''
                select id, nome, stato 
                from Hub
                '''
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            hub = Hub(row['id'], row['nome'], row['stato'])
            lista_hub.append(hub)
        conn.close()
        cursor.close()
        return lista_hub


    @staticmethod
    def calola_tratta():
        conn = DBConnect.get_connection()
        result = []
        query = """
                    select LEAST(id_hub_origine, id_hub_destinazione) as hub_1,
                           GREATEST(id_hub_origine, id_hub_destinazione) as hub_2,
                           SUM(valore_merce) AS valore_totale_merce,
                           COUNT(*) AS numero_totale_spedizioni
                            
                    FROM    spedizione
                    
                    GROUP BY hub_1, 
                             hub_2
                             
                    ORDER BY hub_1,
                             hub_2
                     """
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            tratta = Tratta(row['hub_1'], row['hub_2'], row['valore_totale_merce'], row['numero_totale_spedizioni'])
            result.append(tratta)
        cursor.close()
        conn.close()
        return result

