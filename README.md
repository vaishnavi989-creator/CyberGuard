# 🛡️ CyberGuard
## AI-Powered Real-Time Phishing Detection & Threat Monitoring System

CyberGuard is a cybersecurity project designed to analyze URLs and identify potentially suspicious or phishing websites using URL-based security features, risk scoring, and machine-learning concepts.

## 🚀 Live Project

**Live API:** https://cyberguard-npc8.onrender.com

## ✨ Features

- 🔍 Real-time URL scanning
- 🛡️ Phishing/threat risk detection
- 📊 Risk score generation
- 🟢 SAFE / 🟡 SUSPICIOUS / 🔴 HIGH RISK classification
- ⚠️ Detection reasons for risky URLs
- 📋 Scan history
- 🔎 Search and risk filtering
- 🗄️ SQLite database
- 🌐 FastAPI backend
- 💻 Web dashboard
- 🐳 Docker support
- ☁️ Cloud deployment using Render
- 🤖 Machine-learning component for phishing URL classification

## 🧠 How CyberGuard Works

The user enters a website URL into CyberGuard.

The system then:

1. Extracts security-related URL features.
2. Analyzes the URL using rule-based security logic.
3. Calculates a risk score.
4. Assigns a risk level.
5. Displays the reasons for the detected risk.
6. Stores the scan information in the database.
7. Displays previous scans in the dashboard.

## 🛠️ Technologies Used

### Programming
- Python

### Backend
- FastAPI
- Uvicorn

### Database
- SQLite

### Machine Learning
- NumPy
- Pandas
- Scikit-learn
- Joblib

### Frontend
- HTML
- CSS
- JavaScript

### Deployment & Tools
- Docker
- Git
- GitHub
- Render
- VS Code

## 📁 Project Structure

```text
CyberGuard/
│
├── backend/
│   ├── api.py
│   ├── database.py
│   ├── url_analyzer.py
│   ├── risk_engine.py
│   ├── ml_model.py
│   ├── ml_feature_extractor.py
│   └── ...
│
├── frontend/
│   └── index.html
│
├── dataset/
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔐 Risk Detection

CyberGuard checks URL characteristics such as:

- HTTPS availability
- URL length
- `@` symbol
- Number of hyphens
- Number of digits

Based on these characteristics, the system generates a risk score.

### Risk Levels

| Score | Risk Level |
|---:|---|
| 0–19 | 🟢 LOW |
| 20–39 | 🟡 MEDIUM |
| 40+ | 🔴 HIGH |

## 🧪 Example

### Safe URL

```text
https://google.com
```

Result:

```text
Risk Score: 0
Result: SAFE
Risk Level: LOW
```

### Suspicious / Risky URL

```text
http://secure-login-account-123456789.com/@verify
```

The system can identify indicators such as:

- Missing HTTPS
- `@` symbol
- Many numbers

and assign a higher risk score.

## 📊 Dashboard

The CyberGuard dashboard provides:

- Total scans
- Safe scans
- Suspicious scans
- High-risk scans
- Risk distribution
- Scan results
- Scan history
- Search functionality
- Risk filtering

## 🐳 Docker

CyberGuard can also be run using Docker.

Build the image:

```bash
docker build -t cyberguard .
```

Run the container:

```bash
docker run -p 8000:8000 cyberguard
```

The API can then be accessed at:

```text
http://127.0.0.1:8000
```

## 🌐 API Endpoints

### Home

```text
GET /
```

Returns:

```json
{
  "message": "CyberGuard API is running!"
}
```

### Scan URL

```text
GET /scan?url=https://google.com
```

### Scan History

```text
GET /history
```

## 🎯 Project Objective

The main objective of CyberGuard is to demonstrate how cybersecurity, Python programming, machine learning, databases, APIs, web development, Docker, and cloud deployment can be combined to build a practical security application.

## 🔮 Future Improvements

- Advanced phishing detection using a larger ML model
- Real-time blacklist checking
- Domain reputation APIs
- WHOIS information
- SSL certificate analysis
- DNS security analysis
- Email phishing detection
- Authentication and user accounts
- Persistent cloud database
- Advanced security dashboard
- Automated threat intelligence

## 👩‍💻 Developer

**Vaishnavi Meena**

B.Tech CSE

Cybersecurity & AI Project

## 📌 Disclaimer

CyberGuard is an educational and portfolio project. Its results should not be considered a guarantee that a website is safe or malicious.