class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def get_name(self):
        return self.name + self.last_name