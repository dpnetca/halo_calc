"""
the secondary Legrange points (i.e. crul1a) are probably not needed as
you can not QT directly to them, so they should never be a target, but
gathering as I have it anyway, may be benificial for future use
distance captured bsed on landing spot from QT, depending on angle you 
come from the distance will vary, will lilely round this to nearest 100
"""
distance_to_centre = {
    "arccorp": 28916283,
    "arcl1": 25993364,
    "arcl2": 31776447,
    "arcl3": 28929055,
    "arcl4": 28903572,
    "arcl5": 28884756,
    "crusader": 19156500,
    "crul1": 1720649,
    "crul2": 21031126,
    "crul3": 19181352,
    "crul4": 19129523,
    "crul5": 19167669,
    "hurston": 12851656,
    "hurl1": 11598411,
    "hurl2": 14164425,
    "hurl3": 12848254,
    "hurl4": 12831526,
    "hurl5": 12849981,
    "microtech": 43442152,
    "micl1": 32065901,
    "micl2": 47755719,
    "micl3": 43412592,
    "micl4": 43428760,
    "micl5": 43414965,
    "arcl5a": 28920821,
    "hurl2a": 14139637,
    "hurl5a": 12850305,
    "crul4a": 19144893,
    "crul1a": 17236582,
}

"""
Band distance from Stanton Marker and width of each band as noted by:
https://cstone.space/resources/knowledge-base/65-aaron-halo-detailed-shape-and-density-survey
"""
bands = [
    {"centre": 0, "width": 0},
    {"centre": 19702000, "width": 42000},  # band 1
    {"centre": 19857000, "width": 99000},  # band 2
    {"centre": 19995000, "width": 157000},  # band 3
    {"centre": 20168000, "width": 101000},  # band 4
    {"centre": 20320000, "width": 177000},  # band 5
    {"centre": 20471000, "width": 133000},  # band 6
    {"centre": 20662000, "width": 210000},  # band 7
    {"centre": 20881000, "width": 175000},  # band 8
    {"centre": 21082000, "width": 86000},  # band 9
    {"centre": 21207000, "width": 140000},  # band 10
]
