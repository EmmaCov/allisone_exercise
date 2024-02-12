from enum import Enum


class DiamondCut(str, Enum):
    signature_ideal = "Signature-Ideal"
    ideal = "Ideal"
    very_good = "Very Good"
    good = "Good"
    fair = "Fair"


class DiamondColor(str, Enum):
    d = "D"
    e = "E"
    f = "F"
    g = "G"
    h = "H"
    i = "I"


class DiamondClarity(str, Enum):
    flawless = "FL"
    int_flawless = "IF"
    vvs1 = "VVS1"
    vvs2 = "VVS2"
    vs2 = "VS2"
    vs1 = "VS1"
    si1 = "SI1"


class DiamondPolish(str, Enum):
    ideal = "ID"
    excellent = "EX"
    very_good = "VG"
    good = "G"


class DiamondSymmetry(str, Enum):
    ideal = "ID"
    excellent = "EX"
    very_good = "VG"
    good = "G"


class DiamondReport(str, Enum):
    agsl = "AGSL"
    gia = "GIA"
