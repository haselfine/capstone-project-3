class Menu:
    def __init__(self):
        self.text_descriptions = {}

    def add_option(self, key, description):
        self.text_descriptions[key] = description

    def is_valid(self, choice):
        return choice in self.text_descriptions

    def __str__(self):
        texts = [f'{key}: {self.text_descriptions[key]}' for key in self.text_descriptions.keys()]
        return '\n'.join(texts)