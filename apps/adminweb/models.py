from datetime import datetime

class ExampleClass():
    def __init__(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.currentTime = "no data"

    def giveMeTime(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.currentTime = dt_string
