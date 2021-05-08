import mysql.connector
from mysql.connector import errorcode
from threading import Lock

class DataBaseMeta(type):
    _instances = {}
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class Ludo_Database(DataBaseMeta):
    def __new__(self):
        self.__DB_name='Ludo_DB'
        self.__user='root'
        self.__password='#######'
        self.__cnx=[]
        self.__cursor=[]
        self.connected=False
        self.List_of_Players=[['Omar','SDFSASS',28,'Tun',1540,100],['Cyrine','dsss',25,'Tun',1504,100]]
        self.__Tables=(
            '''CREATE TABLE IF NOT EXISTS users (
            Nickname varchar(14) NOT NULL,
            Password varchar(60) NOT NULL,
            Age int(3) NOT NULL,
            Nationality varchar(20) NOT NULL,
            score int(4),
            Trophies int(3),
            PRIMARY KEY (Nickname,Password)
            ) ENGINE=InnoDB''')
        self.__connect(self)
        self.__create_database(self)
        self.__enter_DB(self)
        self.__create_Table(self)
        self.insert_Player_list(self)
        self.load_Player_list(self)
        s=1


    def __create_database(self):
        try:
            self.__cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(self.__DB_name))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
    def __connect(self):
        try:
            self.__cnx = mysql.connector.connect(user=self.__user, password=self.__password)
            self.__cursor = self.__cnx.cursor()
            self.connected=True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
    def __enter_DB(self):
        try:
            self.__cursor.execute("USE {}".format(self.__DB_name))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(self.__DB_name))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database()
                print("Database {} created successfully.".format(self.__DB_name))
                self.__cnx.database = self.__DB_name
            else:
                print(err)
                exit(1)
    def __create_Table(self):
        table_description = self.__Tables
        try:
            print("Creating table {}: ".format('users'), end='')
            self.__cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
    def load_Player_list(self):
        if self.connected:
            try:
                query=('''SELECT * FROM users''')
                self.__cursor.execute(query)
                self.List_of_Players=[list(l) for l in self.__cursor.fetchall()]

            except mysql.connector.Error as err:
                print(err.msg)

    def insert_Player_list(self):
        for i in self.List_of_Players:
            try:
                query = ('''INSERT INTO users (Nickname, Password, Age, Nationality, score, Trophies) VALUES (%s, %s, %s, %s, %s, %s)''')
                self.__cursor.execute(query, i)
                self.__cnx.commit()
                a=1
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_DUP_ENTRY:
                    try:
                        query = ('''UPDATE users SET Age = %s , Nationality = %s, score = %s, Trophies = %s WHERE Nickname = %s AND Password = %s''')
                        self.__cursor.execute(query, [i[j] for j in [2,3,4,5,0,1]])
                        self.__cnx.commit()
                    except mysql.connector.Error as err:
                        print(err.msg)
                else:
                    print(err.msg)

