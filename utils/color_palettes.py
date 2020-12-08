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


class Conservation_GreenColorPalette(Enum):
    VARIABLE_1 = 'rgba(216, 243, 220,{})'
    VARIABLE_2 = 'rgba(183, 228, 199,{})'
    VARIABLE_3 = 'rgba(149, 213, 178,{})'
    AVERAGE_4 = 'rgba(116, 198, 157,{})'
    AVERAGE_5 = 'rgba(82, 183, 136,{})'
    AVERAGE_6 = 'rgba(64, 145, 108,{})'
    CONSERVED_7 = 'rgba(45, 106, 79,{})'
    CONSERVED_8 = 'rgba(27, 67, 50,{})'
    CONSERVED_9 = 'rgba(8, 28, 21,{})'


class MembraneTopology_GreenYellowRed(Enum):
    INSIDE = 'rgba(112, 193, 179,  {})'
    OUTSIDE = 'rgba(255, 224, 102,  {})'
    INSERTED = 'rgba(242, 95, 92,  {})'


class MembraneTopology_BluePurpleGreen(Enum):
    INSIDE = 'rgba(102, 46, 155,  {})'
    OUTSIDE = 'rgba(67, 188, 205,  {})'
    INSERTED = 'rgba(234, 53, 70,  {})'


class MembraneTopology_BlueRedOrange(Enum):
    INSIDE = 'rgba(46, 196, 182, {})'
    OUTSIDE = 'rgba(231, 29, 54,{})'
    INSERTED = 'rgba(255, 159, 28,{})'


class Disorder_BrownGreen(Enum):
    DISORDER = 'rgba(188, 71, 73,  {})'
    ORDER = 'rgba(106, 153, 78, {})'


class Disorder_YellowRed(Enum):
    DISORDER = 'rgba(244, 211, 94,  {})'
    ORDER = 'rgba(249, 87, 56, {})'


class Disorder_PinkBlue(Enum):
    DISORDER = 'rgba(222, 170, 255,{})'
    ORDER = 'rgba(192, 253, 255, {})'


class SecondaryStructure_RedGreenYellow(Enum):
    HELIX = 'rgba(255, 0, 0,  {})'
    COIL = 'rgba(0, 255, 55,  {})'
    SHEET = 'rgba(255, 255, 0,  {})'


class SecondaryStructure_PurpleOrangeBlue(Enum):
    HELIX = 'rgba(255, 0, 255,  {})'
    COIL = 'rgba(255, 162, 0,  {})'
    SHEET = 'rgba(0, 0, 255,  {})'


class SecondaryStructure_GreenBrownPink(Enum):
    HELIX = 'rgba(46, 196, 182, {})'
    COIL = 'rgba(214, 104, 83,{})'
    SHEET = 'rgba(255, 112, 166,{})'


class MembraneTopology_ColorPalettes(Enum):
    PALETTE_1 = MembraneTopology_GreenYellowRed
    PALETTE_2 = MembraneTopology_BluePurpleGreen
    PALETTE_3 = MembraneTopology_BlueRedOrange


class Conservation_ColorPalettes(Enum):
    PALETTE_1 = Conservation_BlueColorPalette
    PALETTE_2 = Conservation_RedColorPalette
    PALETTE_3 = Conservation_GreenColorPalette


class SecondaryStructure_ColorPalettes(Enum):
    PALETTE_1 = SecondaryStructure_PurpleOrangeBlue
    PALETTE_2 = SecondaryStructure_RedGreenYellow
    PALETTE_3 = SecondaryStructure_GreenBrownPink


class Disorder_ColorPalettes(Enum):
    PALETTE_1 = Disorder_BrownGreen
    PALETTE_2 = Disorder_YellowRed
    PALETTE_3 = Disorder_PinkBlue


class Custom_ColorPalettes(Enum):
    PALETTE_1 = Custom_SpectralColorPalette
    PALETTE_2 = Custom_GrayColorPalette


class Heatmap_ColorPalettes(Enum):
    PALETTE_1 = 'Greys'
    PALETTE_2 = 'viridis'
    PALETTE_3 = 'balance'
    PALETTE_4 = 'Inferno'


class DatasetColorPalettes(Enum):
    membranetopology = MembraneTopology_ColorPalettes
    secondarystructure = SecondaryStructure_ColorPalettes
    disorder = Disorder_ColorPalettes
    conservation = Conservation_ColorPalettes
    custom = Custom_ColorPalettes
    heatmap = Heatmap_ColorPalettes
