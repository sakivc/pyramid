from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "HOME PAGE."

@app.route("/left",methods=["POST", "GET"])
def app1():
    if request.method == "GET":
        return render_template("/app1/index.html")
    else:
        n = int(request.form["num"])
        pattern = left_pyramid(n)
        return render_template("/app1/result.html",paragraph=pattern)

@app.route("/right")
def app2():
    if request.method == "GET":
        return render_template("/app2/index.html")
    else:
        n = int(request.form["num"])
        pattern = right_pyramid(n)
        return render_template("/app2/result.html",paragraph=pattern)

def left_pyramid(_n):
    pattern = []
    for i in range(_n):
        temp = 'o '
        pattern.append(temp)
    return pattern

def right_pyramid(_n):
    pattern = []
    for i in range(_n):
        temp = '  ' * (_n-1-i)
        temp += 'o ' * (i)
        pattern.append(temp)
    return pattern

if __name__ == "__main__" :
    app.run(debug=True)
