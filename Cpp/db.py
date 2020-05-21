import psycopg2


class Database:

    def __init__(self, query_string):
        self.conn = psycopg2.connect(
            'postgres://hgzusbitssgbao:0086bfa1dc7c81ee3b7ebace7abebc33ee405b195798cec088c716a1b3de36a0@ec2-34-194-198-176.compute-1.amazonaws.com:5432/dfkklebvpgkoue',
            sslmode='require')
        self.cur = self.conn.cursor()
        self.query = query_string
        self.result = self.run()

    def run(self):
        try:
            self.cur.execute(self.query)
            result = self.cur.fetchall()
            # self.conn.close()
            return result
        except(Exception, psycopg2.Error) as error:
            if self.conn:
                print("Error ", error)
                return error
