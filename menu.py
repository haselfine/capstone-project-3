class Menu:

    def __init__(self):
        self.text_descriptions = {}
        self.functions = {}

    def add_option(self, key, description, func):
        self.text_descriptions[key] = description
        self.functions[key] = func