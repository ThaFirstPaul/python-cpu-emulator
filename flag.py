class flag():
    def __init__(self):
        self.state = 0

        print("Flag register created.")

    def reset(self):
        self.state = 0

    def set(self, value):
        if value in (0,1):
            self.state = value
            
