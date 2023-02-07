import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QDialog, QHBoxLayout, QVBoxLayout, QWidget, QComboBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
import charStats, weapons, shields, helmets, chest, hands, feet, necklace, trinket, potion

def add_button_clicked():
    current_value = int(label.text().split(": ")[1])
    new_value = current_value + 1


     
     

#Amazon Button Click
def button_1_clicked():
    create_character_stats_window("amazon")

#Marksman Button Click
def button_2_clicked():
    create_character_stats_window("get_character")

#Demon Slayer Button Click
def button_3_clicked():
    create_character_stats_window("get_character")

def create_character_stats_window(charClass):
        window.hide()

        #Create charstats window
        stats_window = QDialog()
        stats_window.setWindowTitle("Character Stats")
        stats_window.setFixedHeight(800)
        stats = charStats.__dict__[charClass + "_stats"]()

        #Create temp table and import class info
        temp_table = {}
        for key, value in stats.items():
            temp_table[key] = value
        table = QTableWidget(stats_window)
        table.setFixedWidth(215)
        table.setRowCount(len(stats))
        table.setColumnCount(2)
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setVisible(False)
        row = 0
        for key, value in temp_table.items():
            table.setItem(row, 0, QTableWidgetItem(key))
            table.setItem(row, 1, QTableWidgetItem(str(value)))
            row += 1

        #Create add and subtract buttons
        add_button = QPushButton("+", stats_window)
        add_button.setFixedSize(20, 20)
        subtract_button = QPushButton("-", stats_window)
        subtract_button.setFixedSize(20, 20)
        hbox_buttons = QHBoxLayout()
        hbox_buttons.addWidget(add_button)
        hbox_buttons.addWidget(subtract_button)
        hbox = QHBoxLayout()
        hbox.addWidget(table)
        vboxTable = QVBoxLayout()
        vboxTable.addLayout(hbox_buttons)
        vboxTable.addLayout(hbox)

        #create weap1 dropdown
        weap1Lable = QLabel("Weapon: ")
        weap1 = QComboBox()
        weaponList = weapons.weaps()
        for key in weaponList:
            weap1.addItem(key)
        
        #create weap2 dropdown
        weap2Lable = QLabel("Shield: ")
        weap2 = QComboBox()
        shieldlist = shields.shieldFunc()
        for key in shieldlist:
             weap2.addItem(key)

        #create weap3 dropdown
        helmLable = QLabel("Helm: ")
        helm = QComboBox()
        helm.addItem("Option 1")
        helm.addItem("Option 2")
        helm.addItem("Option 3")

        #create armor dropdown
        armorLable = QLabel("Armor: ")
        armor = QComboBox()
        armor.addItem("Option 1")
        armor.addItem("Option 2")
        armor.addItem("Option 3")

        #create gloves dropdown
        glovesLable = QLabel("Gloves: ")
        gloves = QComboBox()
        gloves.addItem("Option 1")
        gloves.addItem("Option 2")
        gloves.addItem("Option 3")

        #create belt dropdown
        beltLable = QLabel("Belt: ")
        belt = QComboBox()
        belt.addItem("Option 1")
        belt.addItem("Option 2")
        belt.addItem("Option 3")

        #create boots dropdown
        bootsLable = QLabel("Boots: ")
        boots = QComboBox()
        boots.addItem("Option 1")
        boots.addItem("Option 2")
        boots.addItem("Option 3")

        #create neck dropdown
        neckLable = QLabel("Neck: ")
        neck = QComboBox()
        neck.addItem("Option 1")
        neck.addItem("Option 2")
        neck.addItem("Option 3")

        #create amulet dropdown
        amuletLable = QLabel("Amulet: ")
        amulet = QComboBox()
        amulet.addItem("Option 1")
        amulet.addItem("Option 2")
        amulet.addItem("Option 3")

        #create ring dropdown
        ringLable = QLabel("Ring: ")
        ring = QComboBox()
        ring.addItem("Option 1")
        ring.addItem("Option 2")
        ring.addItem("Option 3")

        #create potion dropdown
        potionLable = QLabel("Potion: ")
        potion = QComboBox()
        potion.addItem("Option 1")
        potion.addItem("Option 2")
        potion.addItem("Option 3")

        #drop down layout
        
        hbox = QHBoxLayout()
        hbox.addLayout(vboxTable)
        hbox_combo = QHBoxLayout()
        

        vboxComb = QVBoxLayout()
        vboxComb.addWidget(weap1Lable)
        vboxComb.addWidget(weap1)
        vboxComb.addWidget(weap2Lable)
        vboxComb.addWidget(weap2)
        vboxComb.addWidget(helmLable)
        vboxComb.addWidget(helm)
        vboxComb.addWidget(armorLable)
        vboxComb.addWidget(armor)
        vboxComb.addWidget(glovesLable)
        vboxComb.addWidget(gloves)
        vboxComb.addWidget(beltLable)
        vboxComb.addWidget(belt)
        vboxComb.addWidget(bootsLable)
        vboxComb.addWidget(boots)
        vboxComb.addWidget(neckLable)
        vboxComb.addWidget(neck)
        vboxComb.addWidget(amuletLable)
        vboxComb.addWidget(amulet)
        vboxComb.addWidget(potionLable)
        vboxComb.addWidget(potion)
        


        
        
        hbox.insertLayout(1, hbox_combo)
        hbox.insertLayout(0, vboxTable)
        hbox.insertLayout(1, vboxComb)
        
        
        
        widget = QWidget()
        widget.setLayout(hbox)
        window.setCentralWidget(widget)

        #window things
        stats_window.setLayout(hbox)
        stats_window.exec_()
        window.show()

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Simple UI")

button_1 = QPushButton("Amazon", window)
button_1.clicked.connect(button_1_clicked)
button_1.setGeometry(0, 0, 60, 60)


button_2 = QPushButton("Marksman", window)
button_2.clicked.connect(button_2_clicked)
button_2.setGeometry(60, 0, 60, 60)


button_3 = QPushButton("Demon Slayer", window)
button_3.clicked.connect(button_3_clicked)
button_3.setGeometry(120, 0, 60, 60)



label = QLabel("", window)
label.setGeometry(60, 70, 140, 40)
label.setAlignment(Qt.AlignCenter)


window.setGeometry(0, 0, 180, 110)


window.show()
sys.exit(app.exec_())