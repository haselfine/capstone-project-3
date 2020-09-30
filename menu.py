class Menu:

    def __init__(self):
        self.text_descriptions = {}
        self.functions = {}

    def add_option(self, key, description, func):
        self.text_descriptions[key] = description
        self.functions[key] = func

    def is_valid(self, choice):
        return choice in self.text_descriptions

    def get_action(self, choice):
        return self.functions.get(choice)

    def __str__(self):
        texts = [f'{key}: {self.text_descriptions[key]}' for key in self.text_descriptions.keys()]
        return '\n'.join(texts)