
# 🏱 1GB Free Internet - Device Info Logger

This is a Flask-based project designed to demonstrate how to collect detailed device and browser information when a user visits a web page. The project includes a styled landing page and an admin panel to view collected data.

> ⚠️ This project is for **educational and awareness** purposes only. Do not deploy or use this for unethical purposes. Ensure **user consent and privacy compliance** if used in any real-world scenario.

---

## 🚀 Features

* ✅ Responsive web page styled in a terminal-like green-on-black theme.
* 📋 Automatically collects:

  * IP, location, and network info
  * Screen and window size
  * OS, browser (User Agent)
  * Battery level and charging status
  * Network type and latency
  * Clipboard write permission
  * Installed plugins
  * Media devices (camera/mic labels)
  * Canvas fingerprint (base64)
  * Page load time
* 🛡 Admin panel at `/admin` to view logs in a tabular format.

---

## 📂 Project Structure

```bash
project/
│
├── app.py                # Flask backend
├── templates             # HTML embedded as string (no external templates)
└── README.md             # You're here!
```

---


## 📦 Requirements

* Python 3.x
* Flask

Install with:

```bash
pip install flask
```

---

## 🔧 How to Run

```bash
python app.py
```

Visit:

* User view: `http://localhost:5000/`
* Admin panel: `http://localhost:5000/admin`

---

## 📜 Example Output in Console

```bash
🧠 New Device Data:
             ip: 103.XXX.XXX.XX
           city: Mumbai
         region: Maharashtra
        country: India
            org: Jio
       platform: Win32
      userAgent: Mozilla/5.0 (...)
         screen: 1920x1080
        battery: 95%
...
```

---

## ⚠️ Legal & Ethical Use

This tool is for:

* Cybersecurity awareness
* Ethical hacking education
* Demonstration of browser fingerprinting

**Do NOT**:

* Deploy in phishing campaigns
* Collect user data without explicit consent

---

## 🛡 Disclaimer

This software is provided for **educational** purposes only. The author is **not responsible** for any misuse of the code. Always respect privacy and follow the law.

---

## ⭐ Credits

Created by **\[alan]**
Feel free to fork, improve, and share ethically!

---

Let me know if you'd like a version with images/icons, deployment guide, or GitHub Pages integration.
