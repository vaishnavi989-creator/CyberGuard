from urllib.parse import urlparse
import re


def extract_ml_features(url):

    parsed = urlparse(url)
    domain = parsed.netloc.split("@")[-1]

    features = {}

    features["URLLength"] = len(url.replace("www.", ""))

    features["DomainLength"] = len(domain)

    features["IsDomainIP"] = 1 if re.match(
        r"^\d+\.\d+\.\d+\.\d+$", domain
    ) else 0

    features["NoOfSubDomain"] = max(0, domain.count(".") - 1)

    features["HasObfuscation"] = 1 if ("%" in url or "@" in url) else 0

    features["NoOfObfuscatedChar"] = url.count("%")

    url_without_www = url.replace("www.", "")

    features["NoOfLettersInURL"] = sum(
      c.isalpha() for c in url_without_www
    )

    features["NoOfDegitsInURL"] = sum(
        c.isdigit() for c in url
    )

    features["NoOfEqualsInURL"] = url.count("=")

    features["NoOfQMarkInURL"] = url.count("?")

    features["NoOfAmpersandInURL"] = url.count("&")

    features["IsHTTPS"] = 1 if parsed.scheme == "https" else 0

    features["NoOfURLRedirect"] = url.count("->")

    features["HasPasswordField"] = 1 if "password" in url.lower() else 0

    features["Bank"] = 1 if "bank" in url.lower() else 0

    payment_words = ["pay", "payment", "checkout", "wallet"]

    features["Pay"] = 1 if any(
        word in url.lower() for word in payment_words
    ) else 0

    crypto_words = ["crypto", "bitcoin", "ethereum", "wallet"]

    features["Crypto"] = 1 if any(
        word in url.lower() for word in crypto_words
    ) else 0

    return features