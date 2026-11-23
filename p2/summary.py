def _number(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def build_summary(a, fa, b, fb):
    phrases = []
    for key, label, prefer_high in [
        ("snowfall_cm", "forecast snowfall", True),
        ("wind_kmh", "forecast wind speed", False),
    ]:
        x, y = fa.get(key), fb.get(key)
        if not (_number(x) and _number(y)):
            phrases.append(f"Not enough data to compare {label}.")
        elif x == y:
            phrases.append(f"Both resorts have the same {label}.")
        else:
            better = a["name"] if (x > y) == prefer_high else b["name"]
            relation = "more" if prefer_high else "lower"
            phrases.append(f"{better} has {relation} {label} for the selected day.")
    return " ".join(phrases)
