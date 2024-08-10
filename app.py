from flask import Flask, render_template

app = Flask(__name__)

datal = ["I", "G", "S"]

@app.route('/')
def home():
    biodata = {
        'nama': 'Matthew Naibaho',
        'kelas': '11 IPA 5',
        'hobi': 'nonton anime dan main game'
    }
    return render_template('home.html', biodata=biodata)

@app.route('/igs')
def igs():
    return render_template('igs.html', datal=datal)

if __name__ == '__main__':
    app.run(debug=True)
