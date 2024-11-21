import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random
form_class = uic.loadUiType("lunch.ui")[0]
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        # 밥  , 국  , 반찬 ...
        self.밥 = {"쌀밥" : 600 ,"잡곡밥" : 750 , "강화쌀밥" : 700}
        self.국 = {"무국" : 500 , "된장국" : 600 , "김치찌개" : 600 , "미역국": 500}
        self.반찬1 = {"제육" : 1000 , "닭볶음" : 1000 , "치킨" : 900 , "스테이크" : 1200}
        self.반찬2 = {"배추김치" : 500 , "겉절이" : 600  , "열무김치" : 550}
        self.반찬3 = {"고사리" : 600 , "시금치" : 600, "콩나물" : 300, "고구마나물" : 400}
        self.기타 = {"아이스림" : 800 , "초코릿" : 600 , "푸딩" : 700 , "음류수" : 500 , "화채" : 700 , "과일" : 500}
        self.pushButton.clicked.connect(self.menu)
        self.price = 0

    def choice(self , menu , n , i ):
        rice = random.choice(list(menu.keys()))
        item = QTableWidgetItem(rice)
        self.tableWidget.setItem(n, i, item)
        return  menu[rice]

    def menu(self):
        for i in range(5):
            self.price = 0
            rice = random.choice(list(self.밥.keys()))
            item = QTableWidgetItem(rice)
            self.tableWidget.setItem(0,i,item)

            soup = random.choice(list(self.국.keys()))
            item = QTableWidgetItem(soup)
            self.tableWidget.setItem(1, i, item)

            반1 = random.choice(list(self.반찬1.keys()))
            item = QTableWidgetItem(반1)
            self.tableWidget.setItem(2, i, item)

            반2 = random.choice(list(self.반찬2.keys()))
            item = QTableWidgetItem(반2)
            self.tableWidget.setItem(3, i, item)

            반3 = random.choice(list(self.반찬3.keys()))
            item = QTableWidgetItem(반3)
            self.tableWidget.setItem(4, i, item)

            기 = random.choice(list(self.기타.keys()))
            item = QTableWidgetItem(기)
            self.tableWidget.setItem(5, i, item)


            self.price += self.밥[rice] + self.국[soup] + self.반찬1[반1] + self.반찬2[반2]  + self.반찬3[반3] + self.기타[기]

            item1 = QTableWidgetItem(str( self.price))
            self.tableWidget.setItem(6, i, item1)
            if self.price > 4200:
                print("다시")
                self.menu()

if __name__ == "__main__" :

    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
