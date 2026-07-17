# 🛡️ Threat Pulse

Threat Pulse is a Flask-based web application that detects phishing attempts and suspicious messages using a rule-based analysis engine. The system analyzes URLs and text messages, assigns a risk level, stores scan history, and provides a real-time security dashboard for monitoring detected threats.

---

## ✨ Features

- 🔍 Analyze suspicious URLs
- 💬 Analyze suspicious text messages
- 📊 Rule-based phishing detection
- 🚨 Risk classification (Safe / Medium / High)
- 📈 Dashboard with live security statistics
- 📝 Store scan history
- ⚠️ Display recent detected threats
- 🌐 Detect suspicious domains and keywords
- 🔗 Detect shortened URLs
- 📋 Generate analysis results instantly

---

# Dashboard

The main dashboard allows users to submit URLs or messages for analysis and displays overall system statistics.

![Dashboard](images/dashboard-home1.png)

---

# Threat Analysis

Threat Pulse analyzes suspicious URLs and messages using predefined detection rules and assigns an appropriate risk level.

![Threat Analysis](images/threat-analysis.png)

---

# Detection Results

The system displays detailed analysis results including the detected threat level and the reasons behind the classification.

![Analysis Result](images/Second%20analysis.png)

---

## 📂 Project Structure

```text
Threat-Pulse/
│
├── app.py
├── database.py
├── analyzer.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── login.html
│   └── register.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── images/
    ├── dashboard-home1.png
    ├── threat-analysis.png
    └── Second analysis.png
```

---

## 🛠 Technologies

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- Bootstrap
- Regular Expressions (Regex)

---

## ⚙️ Detection Logic

Threat Pulse evaluates multiple indicators to determine whether a message or URL is suspicious.

Examples include:

- Suspicious phishing keywords
- Fake login pages
- Shortened URLs
- HTTP instead of HTTPS
- Multiple subdomains
- Suspicious symbols
- Fake domains
- URL length
- Rule-based scoring system

Each indicator contributes to the final score, which is classified into:

- 🟢 Safe
- 🟡 Medium Risk
- 🔴 High Risk

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/DimaSec04/Threat-Pulse.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 🔮 Future Improvements

- Machine Learning detection
- VirusTotal API integration
- Email phishing detection
- File attachment scanning
- User authentication enhancements
- Threat intelligence feeds
- Export reports (PDF)

---

## 👩‍💻 Author

**DimaSec04**

Cybersecurity Student

GitHub:
https://github.com/DimaSec04

---

## 📄 License

This project is intended for educational and cybersecurity learning purposes.
