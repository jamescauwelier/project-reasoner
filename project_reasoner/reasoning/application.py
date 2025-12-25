class ReasoningApplication:
    def __init__(self, name: str):
        self.__name: str = name

    @property
    def name(self):
        return self.__name
