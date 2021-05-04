from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>hello</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    # return redirect(url_for('home'))
    # Or this:
    # return redirect('/')
    # With parameters:
    return redirect(url_for('user', name='fsw'))

@app.route('/test/')  # both '/test/' and '/test' will lead to this page
def test():
    return "This is a test page."

if __name__ == '__main__':
    app.run()