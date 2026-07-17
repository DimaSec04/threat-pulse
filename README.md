# 🛡️ Threat Pulse

## Overview

Threat Pulse is a community-driven phishing and scam detection platform developed using **Python**, **Flask**, **SQLite**, **HTML**, **CSS**, and **JavaScript**.

The system analyzes suspicious URLs and messages using a rule-based detection engine to identify phishing attempts, calculate a risk score, classify threats, and display the results through an interactive dashboard.

---

## ✨ Features

- Analyze suspicious URLs
- Analyze suspicious messages
- Rule-based phishing detection
- Risk classification (Safe / Medium / High)
- Dashboard statistics
- Recent threat activity
- Scan history
- SQLite database integration
- Responsive web interface

---

## 🖥️ Screenshots

### Dashboard

![Dashboard](images/dashboard-home.png)

---

### Threat Analysis

![Threat Analysis](images/threat-analysis.png)

---

### Analysis Result

![Analysis Result](images/Second-analysis.png)

## 📂 Project Structure

```text
Threat-Pulse/
│
├── app.py
├── analyzer.py
├── database.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── images/
    ├── dashboard-home1.png
    ├── threat-analysis.png
    └── second analysis.png
```

---

## 🛠️ Technologies

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- Regular Expressions (Regex)

---

## 🔍 Detection Logic

Threat Pulse analyzes URLs and messages by checking multiple phishing indicators, including:

- Suspicious keywords
- Fake domains
- URL shorteners
- HTTP instead of HTTPS
- Long URLs
- Multiple subdomains
- Special characters
- Social engineering phrases

Each indicator contributes to a final score that determines the overall risk level.

### Risk Levels

- 🟢 Safe
- 🟡 Medium Risk
- 🔴 High Risk

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/DimaSec04/Threat-Pulse.git
```

Move to the project directory:

```bash
cd Threat-Pulse
```

Install the required packages:

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
- Email phishing analysis
- PDF report generation
- Real-time threat intelligence
- User authentication improvements

---

## 👩‍💻 Author

**Dima Raaed**

Cybersecurity Student

GitHub: https://github.com/DimaSec04

---

## 📄 License

This project was developed for educational purposes.
