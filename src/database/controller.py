def read_user(self, query, params=None):
        cursor = self.mysql.connection.cursor()
        cursor.execute(query, params or ())
        results = cursor.fetchall()
        cursor.close()
        return results

def verify_user(self, query, params):
        cursor = self.mysql.connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result is not None

def add_user(self, query, params):
        cursor = self.mysql.connection.cursor()
        cursor.execute(query, params)
        self.mysql.connection.commit()
        cursor.close()
        return True
        
