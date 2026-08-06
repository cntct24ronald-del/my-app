from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>PandaStack Cloud Console App</title>
    </head>
    <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 100px; background-color: #f8f9fa;">
        <div style="display: inline-block; padding: 40px; background: white; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h1 style="color: #2b2d42;">🐼 Status: Application Live!</h1>
            <p style="color: #8d99ae; font-size: 18px;">Your custom Python Web App is running flawlessly on PandaStack PaaS.</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
