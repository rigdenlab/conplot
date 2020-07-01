from enum import Enum
from plotly.colors import diverging, sequential


class Custom_SpectralColorPalette(Enum):
    CUSTOM_1 = diverging.Spectral[0].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_2 = diverging.Spectral[1].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_3 = diverging.Spectral[2].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_4 = diverging.Spectral[3].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_5 = diverging.Spectral[4].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_6 = diverging.Spectral[5].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_7 = diverging.Spectral[6].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_8 = diverging.Spectral[7].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_9 = diverging.Spectral[8].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_10 = diverging.Spectral[9].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_11 = diverging.Spectral[10].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_NAN = 'rgba(255, 255, 255, {})'


class Custom_GrayColorPalette(Enum):
    CUSTOM_1 = sequential.gray[0].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_2 = sequential.gray[1].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_3 = sequential.gray[2].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_4 = sequential.gray[3].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_5 = sequential.gray[4].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_6 = sequential.gray[5].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_7 = sequential.gray[6].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_8 = sequential.gray[7].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_9 = sequential.gray[8].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_10 = sequential.gray[9].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_11 = sequential.gray[10].replace(')', ', {})').replace('rgb', 'rgba')
    CUSTOM_NAN = 'rgba(255, 255, 255, {})'


class Conservation_BlueColorPalette(Enum):
    VARIABLE_1 = sequential.ice[9].replace(')', ', {})').replace('rgb', 'rgba')
    VARIABLE_2 = sequential.ice[8].replace(')', ', {})').replace('rgb', 'rgba')
    VARIABLE_3 = sequential.ice[7].replace(')', ', {})').replace('rgb', 'rgba')
    AVERAGE_4 = sequential.ice[6].replace(')', ', {})').replace('rgb', 'rgba')
    AVERAGE_5 = sequential.ice[5].replace(')', ', {})').replace('rgb', 'rgba')
    AVERAGE_6 = sequential.ice[4].replace(')', ', {})').replace('rgb', 'rgba')
    CONSERVED_7 = sequential.ice[3].replace(')', ', {})').replace('rgb', 'rgba')
    CONSERVED_8 = sequential.ice[2].replace(')', ', {})').replace('rgb', 'rgba')
    CONSERVED_9 = sequential.ice[1].replace(')', ', {})').replace('rgb', 'rgba')


class Conservation_RedColorPalette(Enum):
    VARIABLE_1 = sequential.amp[1].replace(')', ', {})').replace('rgb', 'rgba')
    VARIABLE_2 = sequential.amp[2].replace(')', ', {})').replace('rgb', 'rgba')
    VARIABLE_3 = sequential.amp[3].replace(')', ', {})').replace('rgb', 'rgba')
    AVERAGE_4 = sequential.amp[4].replace(')', ', {})').replace('rgb', 'rgba')
    AVERAGE_5 = sequential.amp[5].replace(')', ', {})').replace('rgb', 'rgba')
    AVERAGE_6 = sequential.amp[6].replace(')', ', {})').replace('rgb', 'rgba')
    CONSERVED_7 = sequential.amp[7].replace(')', ', {})').replace('rgb', 'rgba')
    CONSERVED_8 = sequential.amp[8].replace(')', ', {})').replace('rgb', 'rgba')
    CONSERVED_9 = sequential.amp[9].replace(')', ', {})').replace('rgb', 'rgba')


class MembraneTopology_GreenYellowRed(Enum):
    INSIDE = 'rgba(0, 255, 0,  {})'
    OUTSIDE = 'rgba(255, 255, 0,  {})'
    INSERTED = 'rgba(255, 0, 0,  {})'


class MembraneTopology_BluePurpleGreen(Enum):
    INSIDE = 'rgba(0, 0, 255,  {})'
    OUTSIDE = 'rgba(255, 0, 255,  {})'
    INSERTED = 'rgba(0, 120, 0,  {})'


class Disorder_BrownGreen(Enum):
    DISORDER = 'rgba(120, 0, 0,  {})'
    ORDER = 'rgba(0, 120, 0,  {})'


class Disorder_YellowRed(Enum):
    DISORDER = 'rgba(255, 255, 0,  {})'
    ORDER = 'rgba(255, 0, 0,  {})'


class SecondaryStructure_RedGreenYellow(Enum):
    HELIX = 'rgba(255, 0, 0,  {})'
    COIL = 'rgba(0, 255, 55,  {})'
    SHEET = 'rgba(255, 255, 0,  {})'


class SecondaryStructure_PurpleOrangeBlue(Enum):
    HELIX = 'rgba(255, 0, 255,  {})'
    COIL = 'rgba(255, 162, 0,  {})'
    SHEET = 'rgba(0, 0, 255,  {})'


class MembraneTopology_ColorPalettes(Enum):
    PALETTE_1 = MembraneTopology_GreenYellowRed
    PALETTE_2 = MembraneTopology_BluePurpleGreen


class Conservation_ColorPalettes(Enum):
    PALETTE_1 = Conservation_BlueColorPalette
    PALETTE_2 = Conservation_RedColorPalette


class SecondaryStructure_ColorPalettes(Enum):
    PALETTE_1 = SecondaryStructure_PurpleOrangeBlue
    PALETTE_2 = SecondaryStructure_RedGreenYellow


class Disorder_ColorPalettes(Enum):
    PALETTE_1 = Disorder_BrownGreen
    PALETTE_2 = Disorder_YellowRed


class Custom_ColorPalettes(Enum):
    PALETTE_1 = Custom_SpectralColorPalette
    PALETTE_2 = Custom_GrayColorPalette


class DatasetColorPalettes(Enum):
    membranetopology = MembraneTopology_ColorPalettes
    secondarystructure = SecondaryStructure_ColorPalettes
    disorder = Disorder_ColorPalettes
    conservation = Conservation_ColorPalettes
    custom = Custom_ColorPalettes
