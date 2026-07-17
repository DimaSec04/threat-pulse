# 🛡️ Threat Pulse

A lightweight web-based phishing and scam detection platform developed using **Python**, **Flask**, **SQLite**, **HTML**, **CSS**, and **JavaScript**.

Threat Pulse analyzes suspicious URLs and text messages using rule-based detection techniques to identify phishing attempts, calculate a risk score, classify threats, and present the results through an interactive dashboard.

---

# 📖 Overview

Threat Pulse was developed as a cybersecurity project to simulate an intelligent phishing detection system.

The platform scans URLs and messages for common phishing indicators such as:

- Suspicious keywords
- Fake domains
- URL shorteners
- Insecure protocols (HTTP)
- Social engineering phrases
- Suspicious URL structures

After the analysis, the system calculates a risk score and classifies each scan as **Safe**, **Medium Risk**, or **High Risk**.

---

# ✨ Features

- 🔍 URL Analysis
- 💬 Message Analysis
- 🛡️ Rule-Based Phishing Detection
- 📊 Risk Score Calculation
- 🚨 Threat Classification
- 📈 Interactive Dashboard
- 📝 Recent Scan History
- 💾 SQLite Database
- ⚡ Fast Real-Time Analysis

---

# 🖼️ Screenshots

## Dashboard

![Dashboard](images/dashboard-home.png)

---

## Threat Analysis

![Threat Analysis](images/threat-analysis.png)

---

## Second Analysis

![Second Analysis](images/Second-analysis.png)

---

# 📂 Project Structure

```text
Threat-Pulse/
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
├── analyzer.py
├── README.md
├── requirements.txt
```

---

# ⚙️ Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- Regular Expressions (Regex)

---

# 🔍 Detection Logic

Threat Pulse uses a rule-based detection engine to identify phishing attempts by analyzing both URLs and messages.

### URL Indicators

- HTTP instead of HTTPS
- Suspicious keywords
- URL shorteners
- Fake domains
- Long URLs
- Multiple subdomains
- Special characters
- Suspicious symbols

### Message Indicators

- Urgent language
- Verification requests
- Password requests
- Banking keywords
- Prize and reward scams
- Social engineering phrases

Each detected indicator contributes to the final phishing score.

---

# 🚦 Risk Levels

| Score | Risk Level |
|-------:|------------|
| 0 – 29 | 🟢 Safe |
| 30 – 59 | 🟡 Medium Risk |
| 60+ | 🔴 High Risk |

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

Open your browser

```
http://127.0.0.1:5000
```

---

# 🎯 Future Improvements

- Machine Learning Detection
- VirusTotal API Integration
- Email Phishing Detection
- PDF Report Generation
- Threat Intelligence Integration
- User Authentication Improvements
- Dashboard Analytics

---

# 👩‍💻 Author

**Dima Raaed**

Cybersecurity Student

GitHub:

https://github.com/DimaSec04

---

# 📄 License

This project was developed for educational and learning purposes.
