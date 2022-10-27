from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox,QTableWidgetItem
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particula import Particula
from particulas import Particulas

#pyside2-uic mainwindow.ui para pasar de .ui a python
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.particulas= Particulas()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Agregar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.Agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.Mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)
    @Slot()
    def buscar_id(self):
        id=self.ui.buscar_lineEdit.text()
        encontrado=False
        for particula in self.particulas:
            if id==particula.id:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                id_widget= QTableWidgetItem(str(particula.id))
                origen_x_widget= QTableWidgetItem(str(particula.origen_x))
                origen_y_widget= QTableWidgetItem(str(particula.origen_y))
                destino_x_widget= QTableWidgetItem(str(particula.destino_x))
                destino_y_widget= QTableWidgetItem(str(particula.destino_y))
                velocidad_widget= QTableWidgetItem(str(particula.destino_y))
                red_widget= QTableWidgetItem(str(particula.red))
                green_widget= QTableWidgetItem(str(particula.green))
                blue_widget= QTableWidgetItem(str(particula.blue))
                distancia_widget= QTableWidgetItem(str(particula.distancia))

                self.ui.tabla.setItem(0,0,id_widget)
                self.ui.tabla.setItem(0,1,origen_x_widget)
                self.ui.tabla.setItem(0,2,origen_y_widget)
                self.ui.tabla.setItem(0,3,destino_x_widget)
                self.ui.tabla.setItem(0,4,destino_y_widget)
                self.ui.tabla.setItem(0,5,velocidad_widget)
                self.ui.tabla.setItem(0,6,red_widget)
                self.ui.tabla.setItem(0,7,green_widget)
                self.ui.tabla.setItem(0,8,blue_widget)
                self.ui.tabla.setItem(0,9,distancia_widget)
                encontrado=True
                return
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atencion",
                f'La particula"{id}"no fue encontrada'
            )

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers=["Id","Origen_x","Origen_y","Destino_x","Destino_y","Velocidad","Red","Green","Blue","Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.particulas))
        row=0
        for particula in self.particulas:
            id_widget= QTableWidgetItem(str(particula.id))
            origen_x_widget= QTableWidgetItem(str(particula.origen_x))
            origen_y_widget= QTableWidgetItem(str(particula.origen_y))
            destino_x_widget= QTableWidgetItem(str(particula.destino_x))
            destino_y_widget= QTableWidgetItem(str(particula.destino_y))
            velocidad_widget= QTableWidgetItem(str(particula.destino_y))
            red_widget= QTableWidgetItem(str(particula.red))
            green_widget= QTableWidgetItem(str(particula.green))
            blue_widget= QTableWidgetItem(str(particula.blue))
            distancia_widget= QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row,0,id_widget)
            self.ui.tabla.setItem(row,1,origen_x_widget)
            self.ui.tabla.setItem(row,2,origen_y_widget)
            self.ui.tabla.setItem(row,3,destino_x_widget)
            self.ui.tabla.setItem(row,4,destino_y_widget)
            self.ui.tabla.setItem(row,5,velocidad_widget)
            self.ui.tabla.setItem(row,6,red_widget)
            self.ui.tabla.setItem(row,7,green_widget)
            self.ui.tabla.setItem(row,8,blue_widget)
            self.ui.tabla.setItem(row,9,distancia_widget)
            row+=1
    @Slot()
    def action_abrir_archivo(self):
        #print("abrir")
        ubicacion=QFileDialog.getOpenFileName(
            self,
            "Abrir Archivo",
            ".",
            "JSON (*.json)"
        )[0]
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se abrio el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo abrir el archivo"
            )
    @Slot()
    def action_guardar_archivo(self):
        #print("guardar")
        ubicacion=QFileDialog.getSaveFileName(
            self,
            "Guardar Archivo",
            ".",
            "JSON (*.json)"

        )[0]
        print(ubicacion)
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo"
            )
    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particulas))
    
    @Slot()
    def click_agregar(self):
        id=self.ui.Id_spinBox.text()
        origen_x=self.ui.Origen_x_spinBox.value()
        origen_y=self.ui.Origen_y_spinBox.value()
        destino_x=self.ui.Destino_x_spinBox.value()
        destino_y=self.ui.Destino_y_spinBox.value()
        velocidad=self.ui.Velocidad_spinBox.value()
        red=self.ui.Red_spinBox.value()
        green=self.ui.Green_spinBox.value()
        blue=self.ui.Blue_spinBox.value()

        Particula1=Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        self.particulas.agregar_final(Particula1)

    @Slot()
    def click_agregar_inicio(self):
        id=self.ui.Id_spinBox.text()
        origen_x=self.ui.Origen_x_spinBox.value()
        origen_y=self.ui.Origen_y_spinBox.value()
        destino_x=self.ui.Destino_x_spinBox.value()
        destino_y=self.ui.Destino_y_spinBox.value()
        velocidad=self.ui.Velocidad_spinBox.value()
        red=self.ui.Red_spinBox.value()
        green=self.ui.Green_spinBox.value()
        blue=self.ui.Blue_spinBox.value()

        Particula1=Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,green,blue)
        self.particulas.agregar_inicio(Particula1)
