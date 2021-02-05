
class CFile:
    def __init__(self, maxi):
        self.__file = []
        self.__taillemax = maxi

    def enfile(self, element):
        if len(self.__file) < self.__taillemax:
            return self.__file.append(element)
        else:
            return 'la file est pleine'

    def defile(self):
        if len(self.__file) != 0:
            return self.__file.pop(0)
        else:
            return 'la file est vide'
