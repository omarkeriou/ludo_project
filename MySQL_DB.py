import mysql.connector
from mysql.connector import errorcode

class MySQL_DB:
    def __init__(self,DB_name,user,password,Table_name):
        self.__DB_name=DB_name
        self.connected=False
        self.user=user
        self.password=password
        self.__cnx=[]
        self.__cursor=[]
        self.Data=[]
        self.__Table_name=Table_name





    def connect(self):
        try:
            self.__cnx = mysql.connector.connect(user=self.user, password=self.password)
            self.__cursor = self.__cnx.cursor()
            self.connected=True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def create_database(self):
        try:
            self.__cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(self.__DB_name))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    def use_DB(self):
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

    def create_Table(self, table):
        query_description = "CREATE TABLE IF NOT EXISTS {} ( ".format(self.__Table_name)
        count = 0
        for i in table:
            count += 1
            if i.upper() == 'PRIMARY KEY' or i == len(table):
                query_description += "{} {} ".format(i, table.get(i))
            else:
                query_description += "{} {} NOT NULL,".format(i, table.get(i))
        query = query_description[:-1] + ") ENGINE=InnoDB"

        try:
            print("Creating table {}: ".format(self.__Table_name), end='')
            self.__cursor.execute(query)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    def select_all(self):
        if self.connected:
            try:
                query=('''SELECT * FROM {}'''.format(self.__Table_name))
                self.__cursor.execute(query)
                self.Data=[l for l in self.__cursor.fetchall()]
            except mysql.connector.Error as err:
                print(err.msg)

    def insert_all(self,table):
        if table.get('PRIMARY KEY'):
            list_of_Primary = table.get('PRIMARY KEY')[1:-1].split(",")

        for i in self.Data:
            try:
                query = '''INSERT INTO {} ({}) VALUES ({})'''.format(self.__Table_name,
                                                                     ''.join(str(j) + " ," for j in list(i))[:-1],
                                                                     ''.join(
                                                                         str(j).join(['"', '"']) + " ," if isinstance(j,
                                                                                                                      str) else str(
                                                                             j) + " ," for j in list(i.values()))[:-1])
                query += " ON DUPLICATE KEY UPDATE "
                query_list = []
                for j in table:
                    if not ((j in list_of_Primary) or (j.upper() == "PRIMARY KEY")):
                        query += "{} = %s ,".format(j)
                        query_list.append(i.get(j))
                query = query[:-1]
                self.__cursor.execute(query, query_list)
                self.__cnx.commit()

            except mysql.connector.Error as err:
                print(err.msg)

    def select_one(self, Condition):
        if self.connected:
            try:
                query = "SELECT * FROM {} WHERE".format(self.__Table_name)
                count=0
                query_list=[]
                for i in Condition[0]:
                    if count==len(Condition):
                        query+=" {}= %s".format(i)
                        query_list.append(Condition[0].get(i))

                    else:
                        query+=" {}= %s AND ".format(i)
                        query_list.append(Condition[0].get(i))
                    count += 1

                self.__cursor.execute(query, query_list)
                data = self.__cursor.fetchone()
                if not data:
                    self.Data = [()]
                else:
                    self.Data = [data]
            except mysql.connector.Error as err:
                print(err.msg)

    def insert_one(self,table):
        if table.get('PRIMARY KEY'):
            list_of_Primary = table.get('PRIMARY KEY')[1:-1].split(",")
        try:
            query = '''INSERT INTO {} ({}) VALUES ({})'''.format(self.__Table_name,
                                                                 ''.join(str(j) + " ," for j in list(self.Data[0]))[:-1],
                                                                 ''.join(
                                                                     str(j).join(['"', '"']) + " ," if isinstance(j,
                                                                                                                  str) else str(
                                                                         j) + " ," for j in list(self.Data[0].values()))[:-1])
            query += " ON DUPLICATE KEY UPDATE "
            query_list = []
            for j in table:
                if not ((j in list_of_Primary) or (j.upper() == "PRIMARY KEY")):
                    query += "{} = %s ,".format(j)
                    query_list.append(self.Data[0].get(j))
            query = query[:-1]
            self.__cursor.execute(query, query_list)
            self.__cnx.commit()

        except mysql.connector.Error as err:
            print(err.msg)
    def delete_one(self,Condition):
        try:
            query = "DELETE FROM {} WHERE".format(self.__Table_name)
            count = 0
            query_list = []
            for i in Condition[0]:
                if count == len(Condition):
                    query += " {}= %s".format(i)
                    query_list.append(Condition[0].get(i))

                else:
                    query += " {}= %s AND ".format(i)
                    query_list.append(Condition[0].get(i))
                count += 1

            self.__cursor.execute(query, query_list)
            self.__cnx.commit()

        except mysql.connector.Error as err:
            print(err.msg)
    def setData(self,data):
        self.Data=data
    def getData(self):
        return self.Data