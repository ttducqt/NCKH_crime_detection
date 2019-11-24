def safe():
    return

def warn():
    # mainWindow.ui.warnButton.hide()
    print("hello")
    return

def alert():
    return

self.ui.alertButton.clicked.connect(action.safe)
self.ui.warnButton.clicked.connect(action.warn)
self.ui.alertButton.clicked.connect(action.alert)