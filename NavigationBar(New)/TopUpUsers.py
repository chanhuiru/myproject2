class Users():
    def __init__(self, date, child_Name, camount, tamount):
        self.__date = date
        self.__child_Name = child_Name
        self.__camount = camount
        self.__tamount = tamount

    def get_date(self):
        return self.__date
    def get_child_Name(self):
        return self.__child_Name
    def get_camount(self):
        return self.__camount
    def get_tamount(self):
        return self.__tamount

    def set_date(self, date):
        self.__date = date
    def set_child_Name(self, child_Name):
        self.__child_Name = child_Name
    def set_camount(self, camount):
        self.__camount = camount
    def set_tamount(self, tamount):
        self.__tamount = tamount