from flask import Flask, render_template

app = Flask("edulog.space")

@app.route('/journal/<name>')
def teach_journal(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(debug=True)