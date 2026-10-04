def calculate_risk(features):

    score = 0
    reasons = []

    # HTTPS check
    if not features["has_https"]:
        score += 20
        reasons.append("HTTPS is missing")

    # URL length check
    if features["url_length"] > 75:
        score += 20
        reasons.append("URL is unusually long")

    # @ symbol check
    if features["has_at_symbol"]:
        score += 20
        reasons.append("URL contains @ symbol")

    # Hyphen check
    if features["hyphen_count"] > 3:
        score += 10
        reasons.append("URL contains many hyphens")

    # Number check
    if features["digit_count"] > 5:
        score += 10
        reasons.append("URL contains many numbers")

    # Result
    if score >= 40:
        result = "HIGH RISK"
    elif score >= 20:
        result = "SUSPICIOUS"
    else:
        result = "SAFE"

    # Risk level
    if score >= 40:
        risk_level = "HIGH"
    elif score >= 20:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    # Return all four values
    return score, result, risk_level, reasons