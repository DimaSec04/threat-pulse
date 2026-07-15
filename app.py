from flask import Flask, render_template, request, redirect, jsonify
from database import get_recent_threats_detected
from analysis.analyser import analyze_full
from database import add_scan
from database import scans_completed, threats_blocked, active_users
from database import  get_recent_threats_activity
from database import get_high_alerts
from database import save_early_warning
from database import get_connection
from database import signup
from flask import session
from auth import login
from auth import reset_password
from auth import register
app = Flask(__name__)
app.secret_key = "secret123"
@app.route("/")
def home():
    recent_threats = get_recent_threats_detected()

    return render_template(
        "home.html",
        recent_threats=recent_threats
    )
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    result = None

    if request.method == "POST":

        message = request.form.get("message")

        if message:

            result = analyze_full(message)
    
    scan_count = scans_completed()
    threat_count = threats_blocked()
    user_count = active_users()
    high_alerts = get_high_alerts()

    return render_template(
        "dashboard.html",
        result=result,
        scan_count=scan_count,
        threat_count=threat_count,
        user_count=user_count,
        recent_activity=get_recent_threats_activity(),
        high_alerts=high_alerts
    )
@app.route("/api/dashboard-stats")
def dashboard_stats():

    return jsonify({
        "scans_completed": scans_completed(),
        "threats_blocked": threats_blocked(),
        "active_users": active_users()
    })


@app.route("/api/recent-activity")
def recent_activity():

    return jsonify(get_recent_threats_activity())


@app.route("/api/early-warnings")
def early_warnings():

    return jsonify(get_high_alerts())
@app.route("/login", methods=["GET", "POST"])
def login_page():

    if "username" in session:
     return render_template("login.html")

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        result = login(username, password)

        if result == "Login successful":

            session["username"] = username

            return redirect("/dashboard")

        return render_template("login.html", error=result)

    return render_template("login.html")

@app.route("/reset-password", methods=["GET", "POST"])
def reset_password_page():

    if request.method == "POST":

        code = request.form["code"]
        password = request.form["password"]

        result = reset_password(code, password)

        return result

    return render_template("reset_password.html")    
@app.route("/api/recent-threats")
def recent_threats_api():

    limit = request.args.get("limit", 3)

    threats = get_recent_threats_detected()

    return jsonify(threats[:int(limit)])

@app.route("/api/scan", methods=["POST"])
def api_scan():

    data = request.get_json()

    content = data.get("content")

    result = analyze_full(content)

    if result["score"] >= 70:
        risk_level = "High"

    elif result["score"] >= 40:
        risk_level = "Medium"

    else:
        risk_level = "Low"
    username = session.get("username")
    add_scan(
    None,
    username,
    result["score"],
    "high" if result["score"] >= 70 else "medium" if result["score"] >= 30 else "low",
    "",
    content,
   data.get("type")
)
    if risk_level.lower() == "high":
     save_early_warning(
     data.get("type"),
    content,
    risk_level
    )

    return jsonify({
    "score": result["score"],
    "message": result["message"],
    "scan_count": result["scan_count"],
    "reasons": result.get("reasons", []),
   "alert_triggered": (
        risk_level.lower() == "high"
        and result["scan_count"] >= 2)
    })
@app.route("/api/login", methods=["POST"])
def api_login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    result = login(email, password)

    if isinstance(result, dict):

        session["username"] = result["username"]

        return jsonify({
            "success": True,
            "redirect": "/dashboard"
        })

    return jsonify({
        "success": False,
        "message": result
    })
@app.route("/api/signup", methods=["POST"])
def api_signup_fixed():
    try:
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        
        # استدعاء دالة قاعدة البيانات
        result = signup(username, email, password)
        
        if result == "User created successfully":
            return jsonify({"success": True})
            
        return jsonify({"success": False, "message": result})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

    return jsonify({
        "success": False,
        "message": result
    })
@app.route("/api/forgot-password/send-code", methods=["POST"])
def send_reset_code():

    data = request.get_json()

    email = data.get("email")

    return jsonify({
        "success": True,
        "message": "Verification code sent"
    })
@app.route("/api/forgot-password/verify-code", methods=["POST"])
def verify_reset_code():

    data = request.get_json()

    code = data.get("code")

    saved_code = session.get("reset_code")

    if code == saved_code:
        return jsonify({
            "success": True
        })

    return jsonify({
        "success": False,
        "message": "Invalid verification code"
    })
if __name__ == "__main__":
    app.run(debug=True)
      