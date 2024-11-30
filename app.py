
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video Downloader</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; }
        .container { max-width: 600px; margin: 50px auto; padding: 20px; background: white; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h1 { text-align: center; color: #333; }
        textarea, input[type="text"], button { width: 100%; margin-bottom: 15px; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }
        button { background-color: #5cb85c; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #4cae4c; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Video Downloader</h1>
        <form method="POST" action="/download">
            <label for="urls">Video URLs (one per line):</label>
            <textarea name="urls" id="urls" rows="6" placeholder="Enter video URLs here..."></textarea>
            <label for="quality">Select Quality:</label>
            <input type="text" name="quality" id="quality" placeholder="e.g., bestvideo+bestaudio/best">
            <button type="submit">Download</button>
        </form>
        <p>{{ message }}</p>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        urls = request.form.get('urls', '').strip().splitlines()
        quality = request.form.get('quality', 'bestvideo+bestaudio/best')
        return render_template_string(html_template, message="Processing your request...")
    return render_template_string(html_template, message="")

@app.route('/download', methods=['POST'])
def download():
    urls = request.form.get('urls', '').strip().splitlines()
    quality = request.form.get('quality', 'bestvideo+bestaudio/best')
    return jsonify({"status": "success", "message": f"{len(urls)} videos processed with quality {quality}."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
