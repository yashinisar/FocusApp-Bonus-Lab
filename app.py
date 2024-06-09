from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    # Run the focus1.py script
    result = subprocess.run(['python', 'focus1.py'], capture_output=True, text=True)
    output = result.stdout
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
