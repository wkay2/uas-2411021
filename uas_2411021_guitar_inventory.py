from enum import Enum

class Builder(Enum):
    FENDER = "Fender"
    MARTIN = "Martin"
    GIBSON = "Gibson"
    COLLINGS = "Collings"
    ANY = "Any"

class Type(Enum):
    ACOUSTIC = "Acoustic"
    ELECTRIC = "Electric"

class Wood(Enum):
    MAHOGANY = "Mahogany"
    MAPLE = "Maple"
    ALDER = "Alder"
    SITKA = "Sitka"