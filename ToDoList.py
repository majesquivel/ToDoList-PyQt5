from PyQt5 import QtWidgets, uic

class ToDoList(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ToDoList.ui", self)
        
        self.btnAgregar.clicked.connect(self.AgregarTarea)
        self.btnEliminar.clicked.connect(self.EliminarTarea)
        self.btnEditar.clicked.connect(self.EditarTarea)
        self.lstTareas.itemClicked.connect(self.CargarTarea)

    def AgregarTarea(self):
        tarea = self.edtTarea.text().strip()
        
        if tarea != "":  #validación de campo no vacío
            self.lstTareas.addItem(tarea)
            self.edtTarea.clear() 
            self.edtTarea.setFocus()

#Código de majo ;)

    def EliminarTarea(self):
        indiceTareaBorrar = self.lstTareas.currentRow() 
        
        if indiceTareaBorrar != -1:  #(-1 significa que no hay selección)
            self.lstTareas.takeItem(indiceTareaBorrar)
            self.edtTarea.clear()

    def CargarTarea(self):
        tareaSeleccionada = self.lstTareas.currentItem()
        if tareaSeleccionada is not None:
            self.edtTarea.setText(tareaSeleccionada.text())

    def EditarTarea(self):
        indiceTareaEditar = self.lstTareas.currentRow()
        nuevoTexto = self.edtTarea.text().strip()
        
        #Es para validar que haya una tarea seleccionada y que el nuevo texto no esté vacío
        if indiceTareaEditar != -1 and nuevoTexto != "":
            self.lstTareas.currentItem().setText(nuevoTexto)
            self.edtTarea.clear()

#Desarrollado por MJET 