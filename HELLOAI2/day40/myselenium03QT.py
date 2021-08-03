from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
import time

 
class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(180, 234)
 
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 160, 141, 61))
        self.listWidget.setObjectName("textBrowser")
 
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 10, 16, 16))
        self.label.setObjectName("label")
 
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 70, 21, 16))
        self.label_2.setObjectName("label_2")
 
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(50, 130, 75, 23))
        self.startButton.setObjectName("startButton")
 
        self.lineEdit_ID = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ID.setGeometry(QtCore.QRect(30, 30, 113, 20))
        self.lineEdit_ID.setObjectName("lineEdit_ID")
 
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        # startButton 클릭시 autoExcute 함수 수행
        self.startButton.clicked.connect(self.autoExcute)
 
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Naver Login"))
        self.label.setText(_translate("Dialog", "ID"))
        self.label_2.setText(_translate("Dialog", "PW"))
        self.startButton.setText(_translate("Dialog", "시작"))
 
 # 셀레니움 동작 코드 함수 autoExcute 생성
    def autoExcute(self):
        driver = webdriver.Chrome('chromedriver')
#         driver.implicitly_wait(3)
        driver.get('http://127.0.0.1:5000/')
        # html = driver.page_source
        driver.find_element_by_xpath('/html/body/a[7]').click()
        
        login_box = driver.find_element_by_id("user_id")
        login_box.send_keys("s00001")
        
        login_box = driver.find_element_by_id("pwd")
        login_box.send_keys("1")
        
        driver.find_element_by_xpath('/html/body/form/input[3]').click()
        driver.get('http://127.0.0.1:5000/survey')
        
        driver.find_element_by_class_name('lg_local_btn').click()

        
#         
        objs_table = driver.find_element_by_css_selector("body>table>tbody>tr>td:nth-child(1)>table")
        print(objs_table)
# 
#         obj_trs = objs_table.find_elements_by_tag_name("tr")
#         for i, tr in enumerate(obj_trs):
#             if i > 0:
#             print(tr.find_elements_by_tag_name("td")[1].text, end="\t")
#             print(tr.find_elements_by_tag_name("td")[2].text)
#         
#         driver.find_element_by_id('id').send_keys(id)
#         driver.find_element_by_id('pw').send_keys(pw)
#         driver.find_element_by_class_name('btn_global').click()
#         time.sleep(3)
#         driver.close()
#         # listWidget에 로그인 성공 표시
#         self.listWidget.addItem('로그인 성공')
#         # self.addItem()
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

