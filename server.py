from flask import jsonify,Flask
import request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    #respond with code 200 and concent:'hello world'
    data={
        'Code':200,
        'Content':'Hello world'
    }
    return jsonify(data) 


@app.route("/calculator/add", methods=['POST'])
def add():
    incoming=request.json()

    data={
        'Status code':200,
        'Content':incoming['first']+incoming['second']
    }
    return jsonify(data)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    incoming=request.json()

    data={
        'Status code':200,
        'Content':incoming['first']-incoming['second']
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
