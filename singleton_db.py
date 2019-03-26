import psycopg2
import keys

class Database:
    """docstring for Database."""

    class __Database:
        """docstring for __Database."""

        def __init__(self):
            pass

        def connect(self):
            try:
                self.connection = psycopg2.connect(user = keys.user,
                                          password = keys.password,
                                          host = keys.host,
                                          port = keys.port,
                                          database = keys.database)
                self.cursor = self.connection.cursor()
            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PostgreSQL", error)

        def disconnect(self):
            if(self.connection):
                self.cursor.close()
                self.connection.close()
                print("PostgreSQL connection is closed")

        def createTable(self, table_query):
            try:
                '''Query should be of this form

                create_table_query = \'\'\'CREATE TABLE facebooktweets
                (ID INT PRIMARY KEY        NOT NULL,
                TWEET           TEXT       NOT NULL,
                FOLLOWERS_COUNT INT        NOT NULL,
                FAVORITE_COUNT  INT        NOT NULL,
                DATE            TIMESTAMP  NOT NULL); \'\'\'

                '''

                self.cursor.execute(table_query)
                self.connection.commit()
                print("Table created successfully in PostgreSQL ")
            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PostgreSQL", error)

        def insert(self, table_name, tweet):
            try:
                postgres_insert_query = """ INSERT INTO %s (TWEET, FOLLOWER_COUNT, FAVORITE_COUNT, DATE) VALUES (%s,%s,%s,%S)"""
                record_to_insert = (table_name, tweet.text, tweet.user.followers_count, tweet.favorite_count, tweet.created_at)
                self.cursor.execute(postgres_insert_query, record_to_insert)
                self.connection.commit()
                count = self.cursor.rowcount
                print (count, "Record inserted successfully into", table_name)
            except (Exception, psycopg2.Error) as error :
                if(self.connection):
                    print("Failed to insert record into", table_name, error)

        def selectAll(self, table_name):
            self.cursor.execute("""SELECT * from """+ table_name + """;""")
            print (self.cursor.fetchall())

    instance = None

    def __init__(self):
        if not Database.instance:
            Database.instance = Database.__Database()
        else:
            pass
        Database.instance.connect()

    def destroy(self):
        Database.instance.disconnect()

    def createTable(self, table_query):
        Database.instance.createTable(table_query)

    def selectAll(self, table_name):
        Database.instance.selectAll(table_name)

    def insert(self, table_name, tweet):
        Database.instance.insert(table_name, tweet)
