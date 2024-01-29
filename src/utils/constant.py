from enum import Enum


class DiamondCut(str, Enum):
    """ 
    Class that enumerates the different types of cut of a diamond
    
    Attributes
    ----------
    signature_ideal : str
        The cut is signature ideal
    ideal : str
        The cut is ideal
    very_good : str
        The cut is very good 
    good : str
        The cut is good
    fair : str
        The cut is fair
    """

    signature_ideal = "Signature-Ideal"
    ideal = "Ideal"
    very_good = "Very Good"
    good = "Good"
    fair = "Fair"


class DiamondColor(str, Enum):
    """ 
    Class that enumerates the different types of color of a diamond
    
    Attributes
    ----------
    d : str
        The diamond is of color D, a colorless diamond
    e : str
        The diamond is of color E, a colorless diamond
    f : str
        The diamond is of color F, a colorless diamond
    g : str
        The diamond is of color G, a near colorless diamond
    h : str
        The diamond is of color H, a near colorless diamond
    i : str
        The diamond is of color I, a near colorless diamond
    """

    d = "D"
    e = "E"
    f = "F"
    g = "G"
    h = "H"
    i = "I"


class DiamondClarity(str, Enum):
    """ 
    Class that enumerates the different types of clarity of a diamond
    
    Attributes
    ----------
    flawless : str
        No inclusions in the diamond
    int_flawless : str
        Internally flawless, no inclusions in the diamond
    vvs1 : str
        Very very slighlt inclusions of degree 1
    vvs2 : str
        Very very slighlt inclusions of degree 2
    vs1 : str
        Very slighlt inclusions of degree 1
    vs2 : str
        Very slighlt inclusions of degree 2
    si1 : str
        Slighlt inclusions of degree 1
    """

    flawless = "FL"
    int_flawless = "IF"
    vvs1 = "VVS1"
    vvs2 = "VVS2"
    vs2 = "VS2"
    vs1 = "VS1"
    si1 = "SI1"


class DiamondPolish(str, Enum):
    """ 
    Class that enumerates the different types of polish of a diamond
    
    Attributes
    ----------
    ideal : str
        The polish is ideal
    excellent : str
        the polish is excellent
    very_good : str
        The polish is very good
    good : str
        The polish is good
    """
    ideal = "ID"
    excellent = "EX"
    very_good = "VG"
    good = "G"


class DiamondSymmetry(str, Enum):
    """
    Class that enumerates the different types of symmetry of a diamond

    Attributes
    ----------
    ideal : str
        The symmetry is ideal
    excellent : str
        the symmetry is excellent
    very_good : str
        The symmetry is very good
    good : str
        The symmetry is good
    """
    ideal = "ID"
    excellent = "EX"
    very_good = "VG"
    good = "G"


class DiamondReport(str, Enum):
    """
    Class that enumerates the different types of report of a diamond

    Attributes
    ----------
    agsl : str
        The report was made by the AGSL company
    gia : str
        The report was made by the GIA company

    """
    agsl = "AGSL"
    gia = "GIA"
