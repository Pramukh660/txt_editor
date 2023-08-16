from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    data = request.json
    text = data.get('text', '')

    with open('saved_text.txt', 'w') as f:
        f.write(text)

    return jsonify({'message': 'Text saved successfully.'})

if __name__ == '__main__':
    app.run(debug=True)