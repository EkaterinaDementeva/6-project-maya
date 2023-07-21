import maya.cmds as cmds
from PySide2 import QtWidgets, QtCore, QtGui



class MyDialog(QtWidgets.QDialog):
    
    def __init__(self, parent = None):
        super(MyDialog, self).__init__() # Initializing all properties and settings of the QDialog class
        
        # set a unique window ID
        self.setObjectName('myTestWindow')
        
        # title window
        self.setWindowTitle('My Test UI')
        
        # specify the minimum size of the window (you cannot make the window smaller)
        self.setMinimumSize(300, 100) # Width , Height in pixels
        
        # create main layout
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout) # set to our QDialog main layout

        #create texte window
        self.title_object = QtWidgets.QLineEdit()
        print(self.title_object)
        self.mainLayout.addWidget(self.title_object)
        #self.name_object = self.title_object.text() or "object"

       

        
        #Create a widget - a group for radio buttons
        self.radio_group = QtWidgets.QGroupBox()
        self.radio_group.setMaximumHeight(50) # set group height- 50px

        # Since we will put inside the widget - other widgets
        # then we have to create and put layout in it first
        self.radio_groupLayout = QtWidgets.QHBoxLayout()
        
        # Creating radio buttons
        self.radio_Sphere = QtWidgets.QRadioButton('Sphere')
        self.radio_Cube = QtWidgets.QRadioButton('Cube')
        self.radio_Cone = QtWidgets.QRadioButton('Cone')
        
        # radio buttons in layout
        self.radio_groupLayout.addWidget(self.radio_Sphere)
        self.radio_Sphere.setChecked( True ) 
        self.radio_groupLayout.addWidget(self.radio_Cube)
        self.radio_groupLayout.addWidget(self.radio_Cone)
        
        # In group - layout
        self.radio_group.setLayout( self.radio_groupLayout)
        
        # The group in main layout
        self.mainLayout.addWidget( self.radio_group )

        #create Layout for Slider and Text
        self.slider_text_layout = QtWidgets.QHBoxLayout()
                
        #create  Slider and Text
        self.slider_x = QtWidgets.QSlider()
        self.slider_x.setOrientation(QtCore.Qt.Horizontal)
        self.slider_x.setMinimum(0)
        self.slider_x.setMaximum(10)
        
        self.value_x = QtWidgets.QLineEdit()
        self.value_x.setFixedSize(40, 30)

        #Call fuction - binding the slider's valueChanged signal to the LineEdit
        self.slider_x.valueChanged[int].connect(self.move_coordinate_x)
       
        #put the slider in Layout
        self.slider_text_layout.addWidget(self.slider_x)
        self.slider_text_layout.addWidget(self.value_x)

        #put layout in the main layout
        self.mainLayout.addLayout(self.slider_text_layout)

               
        # Create horizontal layout for buttons
        self.buttonsLayout = QtWidgets.QHBoxLayout()
       
                
        # Create buttons
        self.button_Create = QtWidgets.QPushButton('Create')
        self.button_Apply = QtWidgets.QPushButton('Apply')
        self.button_Close = QtWidgets.QPushButton('Close')

        # create icon button App;y
        icon = QtGui.QIcon("C:/Users/Admin/Documents/Maya/Уроки/6 неделя июль/apply.png")  # Icon file path
        self.button_Apply.setIcon(icon)

        self.button_Create.clicked.connect( self.create )
        self.button_Apply.clicked.connect( self.apply )
        self.button_Close.clicked.connect( self.close )
        
        # Put the buttons in the appropriate layout
        self.buttonsLayout.addWidget( self.button_Create )
        self.buttonsLayout.addWidget( self.button_Apply )
        self.buttonsLayout.addWidget( self.button_Close )
        
        # Put our additional layout in the main layout
        self.mainLayout.addLayout(self.buttonsLayout)
        


    def apply(self):
        # Creates an object and keeps UI opened
    
        name = self.title_object.text()
        
        if name == None:
            self.name_object = "object"
        else:
            self.name_object = name

        # check which radio button is selected
        if self.radio_Sphere.isChecked():
            name_itog = cmds.polySphere(name = self.name_object + "_Sphere##") [0]     
               
        elif self.radio_Cube.isChecked():
            name_itog = cmds.polyCube(name = self.name_object + "_Cube**")
        else:
           name_itog = cmds.polyCone(name = self.name_object + "_Cone**")

       #Call the other function to move the object
        self.move_object(name_itog)


    def create(self):
        """ Creates a polygonal object and closes UI"""
        
        self.apply()
        # close our UI
        self.close()
        
    def move_coordinate_x(self, coordinate_x):
        """Binding the slider's valueChanged signal to the update_line_edit method"""

        self.slider_x.valueChanged[int].connect(self.value_x.setText(str(coordinate_x)))

    
    
    def move_object(self, name_itog ):
        """Code to move the object using the coordinate_x value"""

        coordinate_x = int(self.value_x.text())
        cmds.xform(name_itog , t=[coordinate_x, 0, 0])


# check if our UI is already created

if cmds.window('myTestWindow', q=1, exists=1):
    cmds.deleteUI('myTestWindow')
    
# check if Maya stores our UI display settings
if cmds.windowPref('myTestWindow', exists = 1):
    cmds.windowPref('myTestWindow', remove = 1)
        
        
myUI = MyDialog()
myUI.show()