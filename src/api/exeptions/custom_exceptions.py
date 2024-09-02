class InputUrlTypeException(Exception):
    def __init__(self, input_url):
        self.input_url = input_url
