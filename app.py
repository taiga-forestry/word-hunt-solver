from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import solver

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/solutions")
def solutions():
    letters = request.args.get("letters")
    wh_solver = solver.Solver("ENGLISH_DICT_2.txt")
    wh_solver.fill_board(letters)
    wh_solver.solve_board()
    
    return jsonify(wh_solver.solutions)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)