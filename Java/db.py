import psycopg2


class Database:

    def __init__(self, query_string):
        self.conn = psycopg2.connect(
            'postgres://aukbceisiqwvzi:3dca5d80da6b1f1ebe4df94392f48585f3a1fc7664df111c714130a420eb7478@ec2-18-210-214-86.compute-1.amazonaws.com:5432/d4i3umesprntm1',
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
