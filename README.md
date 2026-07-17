# 🛡️ Threat Pulse

Threat Pulse is a Flask-based cybersecurity web application designed to detect phishing URLs and suspicious messages using a rule-based detection engine.

The system analyzes URLs and text, assigns a risk score, classifies threats into different risk levels, stores scan history, and provides an interactive dashboard for monitoring security events.

---

# 🚀 Features

- 🔍 Analyze URLs and messages
- 🛡️ Rule-based phishing detection
- 📊 Risk scoring engine
- 🚨 Threat classification (Safe / Medium / High)
- 📈 Interactive dashboard
- 📝 Scan history
- 💾 SQLite database
- ⚡ Fast real-time analysis
- 🚨 Early Warning System for repeated threats
- 🔄 Automatic detection of repeated malicious URLs and messages

---

# 🧠 Detection Rules

Threat Pulse detects suspicious activity using several indicators, including:

- Suspicious phishing keywords
- Fake login pages
- URL shorteners
- HTTP instead of HTTPS
- IP-based URLs
- Long URLs
- Multiple subdomains
- Special characters
- Fake domains
- Social engineering phrases

Each indicator contributes to a risk score.

---

# 🚨 Early Warning System

Threat Pulse continuously monitors previously scanned URLs and messages.

If the same malicious URL or suspicious message is detected multiple times, the system automatically generates an **Early Warning Alert**, indicating that the threat is becoming more widespread.

This feature helps identify repeated phishing campaigns and improves threat awareness.

---

# 🏗️ Project Structure

```text
threat-pulse/
│
├── analysis/
├── static/
├── templates/
├── images/
│   ├── dashboard-home.png
│   ├── threat-analysis.png
│   └── Second-analysis.png
│
├── app.py
├── auth.py
├── database.py
├── README.md
└── requirements.txt
```

---

# 💻 Technologies

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- Regex
- Rule-Based Detection

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/DimaSec04/threat-pulse.git
```

Move into the project directory

```bash
cd threat-pulse
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

---

# 📊 Detection Process

1. User submits a URL or message.
2. The detection engine analyzes the input.
3. Suspicious indicators are matched.
4. A risk score is calculated.
5. The threat is classified as Safe, Medium, or High.
6. The scan is stored in the database.
7. If the same malicious content is detected repeatedly, an Early Warning Alert is generated.

---

# 📸 Screenshots

## Dashboard

![Dashboard](images/dashboard-home.png)

---

## Threat Analysis

![Threat Analysis](images/threat-analysis.png)

---

## Second Analysis

![Second Analysis](images/Second-analysis.png)

---

# 🔮 Future Improvements

- Machine Learning Detection
- VirusTotal API Integration
- Email Phishing Detection
- User Authentication Enhancements
- Real-time Notifications
- Threat Intelligence Integration
- Advanced Reporting
- PDF Report Export

---

# 👩‍💻 Author

**Dima Raaed**

Cybersecurity Student

Interested in:

- SOC Analysis
- Blue Team
- Threat Detection
- Incident Response
- Digital Forensics

---

# ⭐ Project Purpose

This project was developed as a graduation project to simulate a lightweight Security Operations Center (SOC) platform capable of detecting phishing attempts, analyzing suspicious URLs and messages, classifying threats, and providing early warning alerts for repeated malicious activities.
