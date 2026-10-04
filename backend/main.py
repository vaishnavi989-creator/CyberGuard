from risk_engine import calculate_risk
from url_analyzer import analyze_url

print("CYBERGUARD")
print("================")

url = input("Enter a website URL: ")

# Analyze URL
features = analyze_url(url)

print("\nURL FEATURES")
print("================")

print("URL Length:", features["url_length"])
print("HTTPS:", features["has_https"])
print("@ Symbol:", features["has_at_symbol"])
print("Dots:", features["dot_count"])
print("Hyphens:", features["hyphen_count"])
print("Numbers:", features["digit_count"])

print("\nChecking completed!")
# Calculate Risk
risk_score, result, risk_level, reasons = calculate_risk(features)
print("\nRISK ANALYSIS")
print("================")
print("Risk Score:", risk_score)
print("Result:", result)
print("Risk Level:", risk_level)
print("\nWhy?")
if reasons:
    for reason in reasons:
        print("⚠️", reason)
else:
    print("No suspicious indicators found.")

print("\nChecking completed!")