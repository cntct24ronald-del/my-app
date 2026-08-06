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
<title>Nova Cloud Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
<style>
*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Poppins,sans-serif;
}
body{
background:
linear-gradient(135deg,#050816,#0d1326,#081629);
height:100vh;
overflow:hidden;
color:white;

}

/* Sidebar */

.sidebar{

position:fixed;
left:0;
top:0;
width:250px;
height:100%;
background:rgba(255,255,255,.05);
backdrop-filter:blur(20px);
border-right:1px solid rgba(255,255,255,.1);

padding:30px;

}

.logo{

font-size:26px;
font-weight:bold;
margin-bottom:50px;
color:#59d6ff;

}

.menu a{

display:block;
text-decoration:none;
color:white;
padding:15px;
margin-bottom:10px;
border-radius:12px;
transition:.3s;

}

.menu a:hover{

background:linear-gradient(90deg,#00d2ff,#3a7bd5);

transform:translateX(8px);

}

/* Top */

.top{

margin-left:250px;
height:80px;
display:flex;
justify-content:space-between;
align-items:center;
padding:20px 40px;

}

.search{

width:350px;
padding:12px 20px;
border:none;
outline:none;
border-radius:40px;
background:rgba(255,255,255,.1);
color:white;

}

.profile{

width:50px;
height:50px;
border-radius:50%;
background:linear-gradient(45deg,#00d2ff,#3a7bd5);

}

/* Main */

.container{

margin-left:250px;
padding:30px 40px;

}

.title{

font-size:35px;
font-weight:700;
margin-bottom:30px;

}

.grid{

display:grid;
grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
gap:25px;

}

.card{

background:rgba(255,255,255,.08);

border-radius:20px;

padding:25px;

backdrop-filter:blur(20px);

transition:.4s;

position:relative;

overflow:hidden;

}

.card:hover{

transform:translateY(-10px);

box-shadow:0 20px 40px rgba(0,0,0,.4);

}

.card::before{

content:'';

position:absolute;

top:-50%;

left:-50%;

width:200%;

height:200%;

background:linear-gradient(
45deg,
transparent,
rgba(255,255,255,.15),
transparent);

transform:rotate(25deg);

animation:shine 8s infinite;

}

@keyframes shine{

100%{

transform:translateX(250%) rotate(25deg);

}

}

.card h2{

margin-bottom:20px;

}

.value{

font-size:40px;

font-weight:bold;

color:#59d6ff;

margin-bottom:10px;

}

.progress{

height:10px;

background:#222;

border-radius:20px;

overflow:hidden;

margin-top:15px;

}

.bar{

height:100%;

background:linear-gradient(90deg,#00d2ff,#3a7bd5);

animation:grow 2s;

}

@keyframes grow{

from{

width:0;

}

}

/* Table */

.table{

margin-top:40px;

background:rgba(255,255,255,.06);

padding:25px;

border-radius:20px;

}

table{

width:100%;

border-collapse:collapse;

}

th,td{

padding:15px;

text-align:left;

}

tr:nth-child(even){

background:rgba(255,255,255,.05);

}

/* Footer */

.footer{

margin-top:40px;

text-align:center;

opacity:.7;

}

</style>
</head>
<body>

<div class="sidebar">

<div class="logo">
☁ Nova Cloud
</div>

<div class="menu">

<a href="#">🏠 Dashboard</a>
<a href="#">⚡ Compute</a>
<a href="#">💾 Storage</a>
<a href="#">🌐 Network</a>
<a href="#">📈 Analytics</a>
<a href="#">🤖 AI Studio</a>
<a href="#">🔒 Security</a>
<a href="#">⚙ Settings</a>

</div>

</div>

<div class="top">

<input class="search" placeholder="Search anything...">

<div class="profile"></div>

</div>

<div class="container">

<div class="title">

Welcome Back 👋

</div>

<div class="grid">

<div class="card">

<h2>CPU Usage</h2>

<div class="value">43%</div>

<div class="progress">

<div class="bar" style="width:43%"></div>

</div>

</div>

<div class="card">

<h2>Memory</h2>

<div class="value">11.2 GB</div>

<div class="progress">

<div class="bar" style="width:70%"></div>

</div>

</div>

<div class="card">

<h2>Storage</h2>

<div class="value">820 GB</div>

<div class="progress">

<div class="bar" style="width:82%"></div>

</div>

</div>

<div class="card">

<h2>Visitors</h2>

<div class="value">25,341</div>

<div class="progress">

<div class="bar" style="width:91%"></div>

</div>

</div>

</div>

<div class="table">

<h2 style="margin-bottom:20px;">Recent Deployments</h2>

<table>

<tr>

<th>Application</th>

<th>Status</th>

<th>Region</th>

<th>Time</th>

</tr>

<tr>

<td>Nova API</td>

<td>🟢 Running</td>

<td>US-East</td>

<td>2 mins ago</td>

</tr>

<tr>

<td>Image AI</td>

<td>🟢 Running</td>

<td>Europe</td>

<td>10 mins ago</td>

</tr>

<tr>

<td>Analytics</td>

<td>🟡 Updating</td>

<td>Asia</td>

<td>30 mins ago</td>

</tr>

<tr>

<td>Database</td>

<td>🔴 Offline</td>

<td>US-West</td>

<td>1 hour ago</td>

</tr>

</table>

</div>

<div class="footer">

© 2026 Nova Cloud Platform

</div>

</div>

</body>
</html>
"""
"""

@app.route('/')
def home():
    return render_template_string(DASHBOARD_HTML)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
