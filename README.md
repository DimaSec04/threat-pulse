# Threat Pulse

## Community-Driven Digital Scam Early Warning System

Threat Pulse is a web-based phishing detection and early warning system designed to help users identify phishing attempts and suspicious messages before they become victims of online scams.

The system analyzes URLs and text messages using a rule-based detection engine with regular expressions (Regex) and assigns a risk level based on predefined security indicators.

## Features

- Analyze suspicious URLs
- Analyze suspicious text messages
- Rule-based phishing detection
- Risk classification (Safe, Medium, High)
- Early warning alerts
- User registration and login
- Dashboard with threat statistics
- Community reporting of suspicious content

## Technologies Used

- Python
- Flask
- SQLite
- HTML5
- CSS3
- JavaScript
- Regular Expressions (Regex)

## Project Structure

```
threat-pulse/
│
├── analysis/
├── static/
├── templates/
├── app.py
├── auth.py
├── database.py
└── .gitignore
```

## How to Run

1. Clone the repository

```bash
git clone https://github.com/DimaSec04/threat-pulse.git
```

2. Install dependencies

```bash
pip install Flask
```

3. Run the application

```bash
python app.py
```

4. Open your browser

```
http://127.0.0.1:5000
```

## Project Highlights

- Detects phishing URLs using rule-based analysis.
- Detects suspicious keywords commonly used in phishing attacks.
- Classifies threats into Safe, Medium, and High risk.
- Provides an easy-to-use dashboard for monitoring scans and threats.
  
## Dashboard Preview

<p align="center">
  <img src="Screenshot.png" alt="Threat Pulse Dashboard" width="900">
</p>## Author

**Dima**
