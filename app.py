from flask import Flask, request

app = Flask(__name__)


@app.route('/form', methods=['GET', 'POST'])
def form():  # put application's code here
    if request.method == 'POST':
        return 'Submitted'


if __name__ == '__main__':
    app.run()
