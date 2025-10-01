def consultar(self, query, params=None):
        cursor = self.mysql.connection.cursor()
        cursor.execute(query, params or ())
        results = cursor.fetchall()
        cursor.close()
        return results
