from flask import Flask, request, jsonify, render_template

from db import session, Topic

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    offset = request.args.get('offset', 0, type=int)
    limit = request.args.get('limit', 10, type=int)

    entities = session.query(Topic).offset(offset).limit(limit).all()
    data = [e.to_dict() for e in entities]

    # return jsonify(success=True, msg='', data=data)
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)

