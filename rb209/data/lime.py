"""Lime requirement data.

Lime factor = tonnes CaCO3 per hectare per pH unit to raise.
Target pH depends on land use and soil type.
Based on RB209 9th edition.
"""

# soil_type -> t CaCO3/ha per pH unit
LIME_FACTORS: dict[str, float] = {
    "light": 4.0,
    "medium": 5.5,
    "heavy": 7.5,
    "organic": 11.0,
}

# Target pH by land use
TARGET_PH: dict[str, float] = {
    "arable": 6.5,
    "grassland": 6.0,
}

# Minimum pH below which lime is recommended
MIN_PH_FOR_LIMING = 5.0

# Maximum single application (t/ha). Apply in splits if more needed.
MAX_SINGLE_APPLICATION = 7.5
