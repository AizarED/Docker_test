from flask import Flask 
app= Flask(__name__)
@app.route("/")
def root():
    print("Close the pod door Hal")
    return "I am afraid I can't let you in"

@app.route("/other")
def root2():
    print("Second one activated")
    return "No backdoors for you"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)