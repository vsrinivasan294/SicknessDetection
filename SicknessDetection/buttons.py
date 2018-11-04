from flask import Flask, render_template, request
button = Flask(__name__)

@button.route('/send', methods = ['MAKE', 'DISPLAY'])
def send():
    if request.method == 'DISPLAY':
        disease = request.form['disease']

        return render_template('disease.html', disease = disease)
    return render_template('index.html')

if __name__ == "__main__":
    button.run()