# Threat Pulse

Threat Pulse is a community-driven cybersecurity platform developed using **Python**, **Flask**, **HTML**, **CSS**, and **SQLite**. The system helps users detect phishing attempts, suspicious URLs, and scam messages using a rule-based analysis engine.

It simulates the workflow of a lightweight Security Operations Center (SOC) by analyzing submitted content, assigning a risk level, and displaying security statistics through an interactive dashboard.

---

## Features

- Analyze suspicious URLs
- Analyze suspicious text messages
- Rule-based phishing detection
- Risk classification (Safe / Medium / High)
- Suspicious keyword detection
- URL pattern analysis
- Dashboard with security statistics
- Scan history
- Modern responsive user interface

---

## Technologies

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- Regular Expressions (Regex)

---

## Project Structure

```
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
│   └── register.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── images/
    ├── dashboard-home1.png
    ├── threat-analysis.png
    └── Second analysis.png
```

---

## Screenshots

### Dashboard Home

![Dashboard Home](images/dashboard-home1.png)

---

### Threat Analysis

![Threat Analysis](images/threat-analysis.png)

---

### Second Analysis

![Second Analysis](images/Second%20analysis.png)

---

## Detection Process

1. User submits a URL or message.
2. Threat Pulse analyzes the input using rule-based detection.
3. Suspicious keywords and URL patterns are identified.
4. A risk score is calculated.
5. The system classifies the result as:
   - Safe
   - Medium Risk
   - High Risk
6. The dashboard displays the analysis results and security statistics.

---

## Future Improvements

- Machine Learning-based phishing detection
- Email attachment analysis
- VirusTotal API integration
- User reporting system
- Real-time threat intelligence feeds
- PDF report generation
- User authentication improvements

---

## Run the Project

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

## Author

**Dima Raaed**

Cybersecurity Student

---

## License

This project was developed for educational purposes.
