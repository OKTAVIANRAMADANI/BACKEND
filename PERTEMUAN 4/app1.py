from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def hello():
    data = [{
        'nama': "Galih",
        'pekerjaan': 'Web Engineer',
        'pesan' : 'Hello Wolrd'
    }]
    return make_response(jsonify({'data': data}), 200)

app.run()
@app.route('/karyawan', methods=['GET','POST','PUT','DELETE'])
def karyawan():
    try:
        if request.method == 'GET':
            data = [{
                'nama' : 'Bjir',
                'pekerjaan': 'Web Engineer',
                'usia' : '24',
            }]
        elif request.method == 'POST':
            data = [{
                'nama' : 'Bjir',
                'pekerjaan': 'Web Engineer',
                'usia' : '24',
            }]
        elif request.method == 'PUT':
            data = [{
                'nama' : 'Bjir',
                'pekerjaan': 'Web Engineer',
                'usia' : '24',
            }]
        else:
            data = [{
                'nama' : 'Bjir',
                'pekerjaan': 'Web Engineer',
                'usia' : '24',
            }]
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)
    return make_response(jsonify({'data': data}), 200)

app.run()