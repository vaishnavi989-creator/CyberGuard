def analyze_url(url):

    features = {}

    features["url_length"] = len(url)

    features["has_https"] = url.startswith("https://")

    features["has_at_symbol"] = "@" in url

    features["dot_count"] = url.count(".")

    features["hyphen_count"] = url.count("-")

    features["digit_count"] = sum(char.isdigit() for char in url)

    return features