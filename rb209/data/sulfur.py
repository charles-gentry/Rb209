"""Sulfur (SO3) recommendation tables.

Values are kg SO3/ha for crops likely to respond to sulfur.
Based on RB209 9th edition. Recommendations are for S-responsive
situations (most of England and Wales now considered responsive).
"""

# crop_value -> kg SO3/ha (for responsive situations)
SULFUR_RECOMMENDATIONS: dict[str, float] = {
    # Cereals
    "winter-wheat-feed": 30,
    "winter-wheat-milling": 40,
    "spring-wheat": 25,
    "winter-barley": 30,
    "spring-barley": 25,
    "winter-oats": 25,
    "spring-oats": 20,
    "winter-rye": 25,

    # Oilseeds - high S demand
    "winter-oilseed-rape": 75,
    "spring-oilseed-rape": 50,
    "linseed": 25,

    # Pulses
    "peas": 0,
    "field-beans": 0,

    # Root/forage
    "sugar-beet": 35,
    "forage-maize": 25,

    # Potatoes
    "potatoes-maincrop": 35,
    "potatoes-early": 30,
    "potatoes-seed": 25,

    # Grassland
    "grass-grazed": 30,
    "grass-silage": 40,
    "grass-hay": 30,
    "grass-grazed-one-cut": 35,
}
