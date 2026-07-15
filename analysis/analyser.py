import re

urgency_words = [
    "urgent", "immediately", "now", "asap", "deadline", "limited",
    "final", "last chance", "act now", "limited time",
    "action required", "final notice",
    "فورا", "الان", "اخر فرصة", "عاجل", "اضغط", "هنا"
]

lure_words = [
    "free", "win", "winner", "prize", "gift", "bonus",
    "deal", "discount", "reward", "cash", "offer",
    "exclusive", "claim", "award", "congratulations",
    "limited offer", "guarantee", "entry", "competition",
    "chance", "won", "sale", "promotion", "special",
    "selected", "risk",
    "مبروك", "ربحت", "هدية", "عرض مجاني",
    "عرض خاص", "اربح الان"
]

financial_words = [
    "bank", "account", "credit", "card", "payment",
    "transaction", "balance", "invoice", "billing",
    "apply", "refund", "transfer", "loan",
    "deposit", "buy", "order",
    "بنك", "حسابك البنكي", "رصيد",
    "معاملة مالية", "بطاقة"
]

security_words = [
    "login", "verify", "confirm", "password",
    "reset", "credentials", "update", "security",
    "authenticate", "validation",
    "تحقق من حسابك", "تحديث البيانات",
    "الهوية", "تسجيل الدخول", "كلمة المرور"
]

threat_words = [
    "suspended", "blocked", "locked", "terminated",
    "disabled", "restricted", "warning",
    "security alert", "account locked",
    "access denied",
    "سيتم ايقاف حسابك", "تم حظر حسابك",
    "تحذير", "اجراء قانوني",
    "سيتم اغلاق حسابك", "سيتم تعطيل حسابك"
]

action_words = [
    "click", "link", "open", "visit", "download",
    "install", "submit", "enter", "fill",
    "sign in", "subscribe"
]

currency_symbols = ["$", "€", "£", "¥", "₹"]

shorteners = [
    "bit.ly", "tinyurl.com", "t.co", "goo.gl",
    "ow.ly", "cutt.ly", "is.gd", "tiny.cc",
    "lnkd.in", "rebrand.ly", "shorte.st",
    "adf.ly", "bc.vc", "soo.gd",
    "s2r.co", "clicky.me", "shorturl.at"
]

fake_domains = [
    "paypa1", "g00gle", "faceb00k",
    "amaz0n", "micros0ft"
]

suspicious_domains = [
    ".xyz", ".tk", ".ml", ".ga", ".cf"
]

phishing_keywords = [
    "login", "verify", "account",
    "secure", "update", "bank",
    "confirm", "password"
]

url_pattern = r'(https?://[^\s]+|www\.[^\s]+)'


def flexible_pattern(word):
    word = re.escape(word)
    word = re.sub(r'[هة]', '[هة]', word)
    word = re.sub(r'[اأإآ]', '[اأإآ]', word)
    word = re.sub(r'[يى]', '[يى]', word)
    return word


def contains(text, word):
    pattern = flexible_pattern(word)
    return bool(re.search(pattern, text))


def analyze_message(message):

    score = 0
    reasons = []

    for word in urgency_words:
        pattern = flexible_pattern(word)

        if re.search(pattern, message, re.IGNORECASE):
            score += 10
            reasons.append(f"Urgency word detected: {word}")

    for word in lure_words:
        pattern = flexible_pattern(word)

        if re.search(pattern, message, re.IGNORECASE):
            score += 10
            reasons.append(f"Lure word detected: {word}")

    for word in financial_words:
        pattern = flexible_pattern(word)

        if re.search(pattern, message, re.IGNORECASE):
            score += 15
            reasons.append(f"Financial word detected: {word}")

    for word in security_words:
        pattern = flexible_pattern(word)

        if re.search(pattern, message, re.IGNORECASE):
            score += 20
            reasons.append(f"Security word detected: {word}")

    for word in threat_words:
        pattern = flexible_pattern(word)

        if re.search(pattern, message, re.IGNORECASE):
            score += 20
            reasons.append(f"Threat word detected: {word}")

    for word in action_words:
        pattern = flexible_pattern(word)

        if re.search(pattern, message, re.IGNORECASE):
            score += 5
            reasons.append(f"Action word detected: {word}")

    for c in currency_symbols:

        if c in message:
            score += 10
            reasons.append(f"Currency ({c}) detected in message")

    return {
        "score": score,
        "reasons": reasons
    }


def analyze_urls(message):

    score = 0
    reasons = []

    urls = re.findall(url_pattern, message)

    for url in urls:

        for s in shorteners:

            if s in url:
                score += 15
                reasons.append(f"Shortener ({s}) detected in URL: {url}")

        for f in fake_domains:

            if f in url:
                score += 30
                reasons.append(f"Fake domain ({f}) detected in URL: {url}")

        for d in suspicious_domains:

            if d in url:
                score += 10
                reasons.append(f"Suspicious TLD ({d}) detected in URL: {url}")

        for k in phishing_keywords:

            if k in url:
                score += 15
                reasons.append(f"Phishing keyword ({k}) detected in URL: {url}")

        if "@" in url:
            score += 30
            reasons.append(f"Suspicious '@' symbol detected in URL: {url}")

        if len(url) > 60:
            score += 15
            reasons.append(f"Long URL detected (length {len(url)}): {url}")

        if url.startswith("http://"):
            score += 20
            reasons.append(f"Not secure (HTTP) detected in URL: {url}")

        if url.count('.') > 3:
            score += 15
            reasons.append(
                f"Too many subdomains ({url.count('.')}) in URL: {url}"
            )

    return {
        "url_score": score,
        "url_reasons": reasons
    }


def analyze_full(message):

    msg_result = analyze_message(message)
    url_result = analyze_urls(message)

    final_score = msg_result["score"] + url_result["url_score"]

    if final_score > 100:
        final_score = 100

    all_reasons = []

    msg_reasons = msg_result["reasons"]
    url_reasons = url_result["url_reasons"]

    max_len = max(len(msg_reasons), len(url_reasons))

    for i in range(max_len):

        if i < len(msg_reasons):
            all_reasons.append(msg_reasons[i])

        if i < len(url_reasons):
            all_reasons.append(url_reasons[i])

    all_reasons = list(dict.fromkeys(all_reasons))

    if final_score >= 70:
        risk_message = "High risk phishing content detected."

    elif final_score >= 30:
        risk_message = "Medium risk suspicious content detected."

    else:
        risk_message = "Low risk content."

    return {
        "score": final_score,
        "message": risk_message,
        "reasons": all_reasons,
        "scan_count": 0
    }