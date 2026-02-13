"""Phosphorus (P2O5) recommendation tables.

Values are kg P2O5/ha, keyed by (crop, p_index).
P index ranges from 0 (deficient) to 4+ (high).
Based on RB209 9th edition.
"""

# (crop_value, p_index) -> kg P2O5/ha
PHOSPHORUS_RECOMMENDATIONS: dict[tuple[str, int], float] = {
    # Cereals (wheat, barley, oats, rye)
    **{(crop, idx): val
       for crop in [
           "winter-wheat-feed", "winter-wheat-milling", "spring-wheat",
           "winter-barley", "spring-barley",
           "winter-oats", "spring-oats", "winter-rye",
       ]
       for idx, val in [(0, 110), (1, 85), (2, 60), (3, 30), (4, 0)]},

    # Oilseed rape
    **{(crop, idx): val
       for crop in ["winter-oilseed-rape", "spring-oilseed-rape"]
       for idx, val in [(0, 100), (1, 75), (2, 50), (3, 25), (4, 0)]},

    # Linseed
    ("linseed", 0): 80,
    ("linseed", 1): 55,
    ("linseed", 2): 35,
    ("linseed", 3): 15,
    ("linseed", 4): 0,

    # Peas and beans
    **{(crop, idx): val
       for crop in ["peas", "field-beans"]
       for idx, val in [(0, 80), (1, 55), (2, 30), (3, 0), (4, 0)]},

    # Sugar beet
    ("sugar-beet", 0): 120,
    ("sugar-beet", 1): 95,
    ("sugar-beet", 2): 65,
    ("sugar-beet", 3): 35,
    ("sugar-beet", 4): 0,

    # Forage maize
    ("forage-maize", 0): 120,
    ("forage-maize", 1): 95,
    ("forage-maize", 2): 65,
    ("forage-maize", 3): 35,
    ("forage-maize", 4): 0,

    # Potatoes
    ("potatoes-maincrop", 0): 250,
    ("potatoes-maincrop", 1): 200,
    ("potatoes-maincrop", 2): 150,
    ("potatoes-maincrop", 3): 50,
    ("potatoes-maincrop", 4): 0,

    ("potatoes-early", 0): 200,
    ("potatoes-early", 1): 150,
    ("potatoes-early", 2): 100,
    ("potatoes-early", 3): 35,
    ("potatoes-early", 4): 0,

    ("potatoes-seed", 0): 200,
    ("potatoes-seed", 1): 150,
    ("potatoes-seed", 2): 100,
    ("potatoes-seed", 3): 35,
    ("potatoes-seed", 4): 0,

    # Grass (cut - silage and hay)
    **{(crop, idx): val
       for crop in ["grass-silage", "grass-hay"]
       for idx, val in [(0, 120), (1, 80), (2, 50), (3, 20), (4, 0)]},

    # Grass (grazed)
    ("grass-grazed", 0): 80,
    ("grass-grazed", 1): 50,
    ("grass-grazed", 2): 30,
    ("grass-grazed", 3): 0,
    ("grass-grazed", 4): 0,

    # Grass (grazed + 1 cut)
    ("grass-grazed-one-cut", 0): 100,
    ("grass-grazed-one-cut", 1): 65,
    ("grass-grazed-one-cut", 2): 40,
    ("grass-grazed-one-cut", 3): 10,
    ("grass-grazed-one-cut", 4): 0,
}
