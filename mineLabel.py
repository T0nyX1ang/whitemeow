from PyQt5 import QtWidgets, QtCore


class mineLabel (QtWidgets.QLabel):
    leftRelease = QtCore.pyqtSignal (int, int)  # 定义信号
    rightRelease = QtCore.pyqtSignal (int, int)
    leftPressed = QtCore.pyqtSignal (int, int)
    rightPressed = QtCore.pyqtSignal (int, int)
    leftAndRightPressed = QtCore.pyqtSignal (int, int)
    leftAndRightRelease = QtCore.pyqtSignal (int, int)
    mouseMove = QtCore.pyqtSignal (int, int)

    def __init__(self, i, j, num, parent=None):
        super (mineLabel, self).__init__ (parent)
        self.num = num
        self.i = i
        self.j = j
        self.leftAndRightClicked = False
        self.status = 0  # 0、1、2代表没挖开、挖开、标雷
        self.pixSize=16

    '''def mousePressEvent(self, e):  ##重载一下鼠标点击事件
        if e.buttons () == QtCore.Qt.LeftButton | QtCore.Qt.RightButton:
            self.leftAndRightPressed.emit (self.i, self.j)
            self.leftAndRightClicked = True
        else:
            if e.buttons () == QtCore.Qt.LeftButton:
                self.leftPressed.emit (self.i, self.j)
            elif e.buttons () == QtCore.Qt.RightButton:
                self.rightPressed.emit (self.i, self.j)'''
    
    def mousePressEvent(self, e):  # 重载一下鼠标点击事件
        xx = e.localPos().x()
        yy = e.localPos().y()
        # print('点下位置{}, {}'.format(xx, yy))
        if e.buttons () == QtCore.Qt.LeftButton | QtCore.Qt.RightButton:
            self.leftAndRightPressed.emit (yy//self.pixSize+self.i, xx//self.pixSize+self.j)
            self.leftAndRightClicked = True
        else:
            if e.buttons () == QtCore.Qt.LeftButton:
                self.leftPressed.emit(yy//self.pixSize+self.i, xx//self.pixSize+self.j)
            elif e.buttons () == QtCore.Qt.RightButton:
                self.rightPressed.emit(yy//self.pixSize+self.i, xx//self.pixSize+self.j)

    '''def mouseReleaseEvent(self, e):
        if self.leftAndRightClicked:
            self.leftAndRightRelease.emit (self.i, self.j)
            self.leftAndRightClicked=False
        else:
            if e.button () == QtCore.Qt.LeftButton:
                self.leftRelease.emit (self.i, self.j)
            elif e.button () == QtCore.Qt.RightButton:
                self.rightRelease.emit (self.i, self.j)'''
    
    def mouseReleaseEvent(self, e):
        #每个标签的鼠标事件发射给槽的都是自身的坐标
        #所以获取释放点相对本标签的偏移量，矫正发射的信号
        xx = e.localPos().x()
        yy = e.localPos().y()
        # print('抬起位置{}, {}'.format(xx, yy))
        if self.leftAndRightClicked:
            self.leftAndRightRelease.emit(yy//self.pixSize+self.i, xx//self.pixSize+self.j)
            self.leftAndRightClicked=False
        else:
            if e.button () == QtCore.Qt.LeftButton:
                self.leftRelease.emit(yy//self.pixSize+self.i, xx//self.pixSize+self.j)
            elif e.button () == QtCore.Qt.RightButton:
                self.rightRelease.emit(yy//self.pixSize+self.i, xx//self.pixSize+self.j)

    def mouseMoveEvent(self, e):

        xx = e.localPos().x()
        yy = e.localPos().y()
        #print('移动位置{}, {}'.format(xx, yy))
        self.mouseMove.emit (yy//self.pixSize+self.i, xx//self.pixSize+self.j)