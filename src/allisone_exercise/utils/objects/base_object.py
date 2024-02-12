from pydantic import BaseModel

from allisone_exercise.utils.objects.constant import (DiamondCut, DiamondClarity, DiamondColor, DiamondPolish, DiamondReport, DiamondSymmetry)

class Diamond(BaseModel):
    carat_weight: float
    cut: DiamondCut
    color: DiamondColor
    clarity: DiamondClarity
    polish: DiamondPolish
    symmetry: DiamondSymmetry
    report: DiamondReport