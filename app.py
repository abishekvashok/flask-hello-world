from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/redirect')
def redirect():
    url = request.args.get('url')
    return redirect(url)

@app.route('/check')
def check():
    return render_template('index.html')

@app.route('/redirect-via-img')
def redirect_via_img():
    url = request.args.get('url')
    return render_template('redirect.html', url=url)

if __name__ == "__main__":
    app.run(debug=True)
