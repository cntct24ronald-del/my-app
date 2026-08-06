from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Google Cloud Console Styled HTML Template
DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Cloud Console Clone</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Roboto', Arial, sans-serif; }
        body { display: flex; height: 100vh; background-color: #f1f3f4; color: #3c4043; }
        
        /* Top Navigation Bar */
        .navbar { position: fixed; top: 0; left: 0; right: 0; height: 48px; background-color: #1a73e8; color: white; display: flex; align-items: center; padding: 0 16px; z-index: 100; box-shadow: 0 1px 2px rgba(0,0,0,0.1); }
        .nav-brand { font-size: 18px; font-weight: 500; margin-right: 30px; display: flex; align-items: center; gap: 8px; }
        .nav-search { background: rgba(255,255,255,0.15); border: none; padding: 6px 12px; border-radius: 4px; width: 400px; color: white; }
        .nav-search::placeholder { color: rgba(255,255,255,0.7); }

        /* Left Sidebar Nav */
        .sidebar { width: 256px; background-color: white; border-right: 1px solid #dadce0; padding-top: 64px; display: flex; flex-direction: column; }
        .sidebar-item { padding: 12px 24px; font-size: 14px; font-weight: 500; color: #5f6368; text-decoration: none; display: flex; align-items: center; gap: 12px; }
        .sidebar-item:hover, .sidebar-item.active { background-color: #e8f0fe; color: #1a73e8; }

        /* Main Console Panel Content */
        .main-content { flex: 1; padding: 72px 32px 32px 32px; overflow-y: auto; }
        .header-banner { background-color: white; border: 1px solid #dadce0; border-radius: 8px; padding: 24px; margin-bottom: 24px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
        .header-banner h1 { font-size: 28px; color: #202124; margin-bottom: 8px; font-weight: 400; }
        .header-banner p { font-size: 14px; color: #5f6368; }

        /* Dashboard Resource Cards Layout Grid */
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; }
        .card { background: white; border: 1px solid #dadce0; border-radius: 8px; padding: 20px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
        .card-title { font-size: 16px; font-weight: 500; color: #202124; margin-bottom: 16px; border-bottom: 1px solid #f1f3f4; padding-bottom: 8px; }
        
        /* Interactive Component Elements */
        .status-badge { display: inline-block; padding: 4px 8px; border-radius: 12px; font-size: 12px; font-weight: 500; background-color: #e6f4ea; color: #137333; }
        .metric-row { display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 14px; }
        .metric-label { color: #5f6368; }
        .metric-value { font-weight: 500; color: #202124; }
    </style>
</head>
<body>

    <!-- Top Menu Header Navbar -->
    <div class="navbar">
        <div class="nav-brand">☁️ Google Cloud Console</div>
        <input type="text" class="nav-search" placeholder="Search resources, services, and products...">
    </div>

    <!-- Sidebar Menu Options Navigation Component -->
    <div class="sidebar">
        <a href="#" class="sidebar-item active">🏠 Dashboard</a>
        <a href="#" class="sidebar-item">🚀 App Engine</a>
        <a href="#" class="sidebar-item">📦 Cloud Storage</a>
        <a href="#" class="sidebar-item">🛡️ IAM & Admin</a>
        <a href="#" class="sidebar-item">📊 Billing</a>
    </div>

    <!-- Central Project Dashboard Area View -->
    <div class="main-content">
        <div class="header-banner">
            <h1>Hello Google App Engine</h1>
            <p>Welcome to your customized full-stack administration console dashboard tracking project infrastructure health status metrics live.</p>
        </div>

        <div class="grid">
            <!-- Project Information System Card Widget -->
            <div class="card">
                <div class="card-title">Project Info</div>
                <div class="metric-row">
                    <span class="metric-label">Project Name:</span>
                    <span class="metric-value">my-paas-application</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Project ID:</span>
                    <span class="metric-value">paas-cloud-app-2026</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Project Number:</span>
                    <span class="metric-value">492019385023</span>
                </div>
            </div>

            <!-- Platform-As-A-Service Engine Status Summary Monitor -->
            <div class="card">
                <div class="card-title">App Engine Status</div>
                <div class="metric-row">
                    <span class="metric-label">Status:</span>
                    <span class="status-badge">Active / Serving</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Runtime Environment:</span>
                    <span class="metric-value">Python 3.9 (Standard)</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Instance Allocation Class:</span>
                    <span class="metric-value">F1 (Free Tier Tiering)</span>
                </div>
            </div>

            <!-- Network Billing and Requests Monitoring Widget Card -->
            <div class="card">
                <div class="card-title">Resources & Billing Usage</div>
                <div class="metric-row">
                    <span class="metric-label">Daily Instance Allocation:</span>
                    <span class="metric-value">0.12 / 28.0 Hours</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Network Outbound Traffic:</span>
                    <span class="metric-value">0.01 GB / 1.00 GB</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Estimated Charges:</span>
                    <span class="metric-value" style="color: #137333; font-weight: bold;">$0.00 (100% Free)</span>
                </div>
            </div>
        </div>
    </div>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(DASHBOARD_HTML)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
