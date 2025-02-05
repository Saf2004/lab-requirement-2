from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('Name')
        email = request.form.get('email')
        return render_template('greetings.html', name=name, email=email)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
