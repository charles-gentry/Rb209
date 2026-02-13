"""Potassium (K2O) recommendation tables.

Values are kg K2O/ha, keyed by (crop, k_index).
K index ranges from 0 (deficient) to 4+ (high).
For cereals, separate tables for straw removed vs incorporated.
Based on RB209 9th edition.
"""

# Cereals with straw REMOVED
# (crop_value, k_index) -> kg K2O/ha
POTASSIUM_STRAW_REMOVED: dict[tuple[str, int], float] = {
    **{(crop, idx): val
       for crop in [
           "winter-wheat-feed", "winter-wheat-milling", "spring-wheat",
           "winter-barley", "spring-barley",
           "winter-oats", "spring-oats", "winter-rye",
       ]
       for idx, val in [(0, 105), (1, 75), (2, 55), (3, 0), (4, 0)]},
}

# Cereals with straw INCORPORATED
POTASSIUM_STRAW_INCORPORATED: dict[tuple[str, int], float] = {
    **{(crop, idx): val
       for crop in [
           "winter-wheat-feed", "winter-wheat-milling", "spring-wheat",
           "winter-barley", "spring-barley",
           "winter-oats", "spring-oats", "winter-rye",
       ]
       for idx, val in [(0, 65), (1, 40), (2, 25), (3, 0), (4, 0)]},
}

# Non-cereal crops (no straw option)
POTASSIUM_RECOMMENDATIONS: dict[tuple[str, int], float] = {
    # Oilseed rape
    **{(crop, idx): val
       for crop in ["winter-oilseed-rape", "spring-oilseed-rape"]
       for idx, val in [(0, 95), (1, 65), (2, 45), (3, 0), (4, 0)]},

    # Linseed
    ("linseed", 0): 75,
    ("linseed", 1): 50,
    ("linseed", 2): 35,
    ("linseed", 3): 0,
    ("linseed", 4): 0,

    # Peas and beans
    **{(crop, idx): val
       for crop in ["peas", "field-beans"]
       for idx, val in [(0, 75), (1, 50), (2, 35), (3, 0), (4, 0)]},

    # Sugar beet
    ("sugar-beet", 0): 175,
    ("sugar-beet", 1): 130,
    ("sugar-beet", 2): 95,
    ("sugar-beet", 3): 0,
    ("sugar-beet", 4): 0,

    # Forage maize
    ("forage-maize", 0): 175,
    ("forage-maize", 1): 130,
    ("forage-maize", 2): 95,
    ("forage-maize", 3): 0,
    ("forage-maize", 4): 0,

    # Potatoes
    ("potatoes-maincrop", 0): 300,
    ("potatoes-maincrop", 1): 240,
    ("potatoes-maincrop", 2): 180,
    ("potatoes-maincrop", 3): 0,
    ("potatoes-maincrop", 4): 0,

    ("potatoes-early", 0): 250,
    ("potatoes-early", 1): 200,
    ("potatoes-early", 2): 150,
    ("potatoes-early", 3): 0,
    ("potatoes-early", 4): 0,

    ("potatoes-seed", 0): 250,
    ("potatoes-seed", 1): 200,
    ("potatoes-seed", 2): 150,
    ("potatoes-seed", 3): 0,
    ("potatoes-seed", 4): 0,

    # Grass (silage - high offtake)
    ("grass-silage", 0): 150,
    ("grass-silage", 1): 100,
    ("grass-silage", 2): 60,
    ("grass-silage", 3): 0,
    ("grass-silage", 4): 0,

    # Grass (hay)
    ("grass-hay", 0): 120,
    ("grass-hay", 1): 80,
    ("grass-hay", 2): 50,
    ("grass-hay", 3): 0,
    ("grass-hay", 4): 0,

    # Grass (grazed - low offtake, recycling via dung)
    ("grass-grazed", 0): 60,
    ("grass-grazed", 1): 30,
    ("grass-grazed", 2): 0,
    ("grass-grazed", 3): 0,
    ("grass-grazed", 4): 0,

    # Grass (grazed + 1 cut)
    ("grass-grazed-one-cut", 0): 100,
    ("grass-grazed-one-cut", 1): 60,
    ("grass-grazed-one-cut", 2): 30,
    ("grass-grazed-one-cut", 3): 0,
    ("grass-grazed-one-cut", 4): 0,
}
