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


class Heatmap_GreyColorPalette(Enum):
    BIN_10 = 'rgb(255,255,255)'
    BIN_9 = 'rgb(229,229,229)'
    BIN_8 = 'rgb(204,204,204)'
    BIN_7 = 'rgb(179,179,179)'
    BIN_6 = 'rgb(153,153,153)'
    BIN_5 = 'rgb(127,127,127)'
    BIN_4 = 'rgb(102,102,102)'
    BIN_3 = 'rgb(77,77,77)'
    BIN_2 = 'rgb(51,51,51)'
    BIN_1 = 'rgb(25,25,25)'
    BIN_0 = 'rgb(0,0,0)'


class Heatmap_Viridis(Enum):
    BIN_10 = sequential.Viridis[0]
    BIN_9 = sequential.Viridis[0]
    BIN_8 = sequential.Viridis[1]
    BIN_7 = sequential.Viridis[2]
    BIN_6 = sequential.Viridis[3]
    BIN_5 = sequential.Viridis[4]
    BIN_4 = sequential.Viridis[5]
    BIN_3 = sequential.Viridis[6]
    BIN_2 = sequential.Viridis[7]
    BIN_1 = sequential.Viridis[8]
    BIN_0 = sequential.Viridis[9]


class Heatmap_BuRd(Enum):
    BIN_10 = diverging.RdYlBu[10]
    BIN_9 = diverging.RdYlBu[9]
    BIN_8 = diverging.RdYlBu[8]
    BIN_7 = diverging.RdYlBu[7]
    BIN_6 = diverging.RdYlBu[6]
    BIN_5 = diverging.RdYlBu[5]
    BIN_4 = diverging.RdYlBu[4]
    BIN_3 = diverging.RdYlBu[3]
    BIN_2 = diverging.RdYlBu[2]
    BIN_1 = diverging.RdYlBu[1]
    BIN_0 = diverging.RdYlBu[0]


class Heatmap_Inferno(Enum):
    BIN_10 = sequential.Inferno[0]
    BIN_9 = sequential.Inferno[0]
    BIN_8 = sequential.Inferno[1]
    BIN_7 = sequential.Inferno[2]
    BIN_6 = sequential.Inferno[3]
    BIN_5 = sequential.Inferno[4]
    BIN_4 = sequential.Inferno[5]
    BIN_3 = sequential.Inferno[6]
    BIN_2 = sequential.Inferno[7]
    BIN_1 = sequential.Inferno[8]
    BIN_0 = sequential.Inferno[9]


class Heatmap_ColorPalettes(Enum):
    PALETTE_1 = Heatmap_GreyColorPalette
    PALETTE_2 = Heatmap_Viridis
    PALETTE_3 = Heatmap_BuRd
    PALETTE_4 = Heatmap_Inferno


class DatasetColorPalettes(Enum):
    membranetopology = MembraneTopology_ColorPalettes
    secondarystructure = SecondaryStructure_ColorPalettes
    disorder = Disorder_ColorPalettes
    conservation = Conservation_ColorPalettes
    custom = Custom_ColorPalettes
    heatmap = Heatmap_ColorPalettes


def get_heatmap_colorscale(selected_palette):
    palette = Heatmap_ColorPalettes.__getattr__(selected_palette).value
    return [
        (0, palette.__getitem__('BIN_10').value),
        (.1, palette.__getitem__('BIN_9').value),
        (.2, palette.__getitem__('BIN_8').value),
        (.3, palette.__getitem__('BIN_7').value),
        (.4, palette.__getitem__('BIN_6').value),
        (.5, palette.__getitem__('BIN_5').value),
        (.6, palette.__getitem__('BIN_4').value),
        (.7, palette.__getitem__('BIN_3').value),
        (.8, palette.__getitem__('BIN_2').value),
        (.9, palette.__getitem__('BIN_1').value),
        (1, palette.__getitem__('BIN_0').value)
    ]
