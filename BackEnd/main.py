from flask import Flask, render_template

app = Flask(
    __name__, 
    static_folder='../FrontEnd/build/static',
    template_folder='../FrontEnd/build',
)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()