from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def classify_triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        triangle_type = "These side lengths make a triangle."
        if a != b and a != c and b != c:
            triangle_type += "This is a scalene triangle."
        elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
            triangle_type += "This is an isosceles triangle."
        elif a == b == c:
            triangle_type += "This is an equilateral triangle."
    else:
        triangle_type = "Not a triangle. Try again."
    return triangle_type

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.json
    a = int(data["a"])
    b = int(data["b"])
    c = int(data["c"])
    result = classify_triangle(a, b, c)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)