from enum import Enum


class MembraneStates(Enum):
    INSIDE = 1
    OUTSIDE = 2
    INSERTED = 3

class ConservationStates(Enum):
    CONSERVED = 1
    AVERAGE = 2
    VARIABLE = 3

class SecondaryStructureStates(Enum):
    HELIX = 1
    COIL = 2
    SHEET = 3
