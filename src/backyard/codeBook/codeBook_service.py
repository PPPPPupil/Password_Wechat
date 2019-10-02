from flask import render_template, jsonify, request, session
from src import app
import json
from flask_wtf import CSRFProtect
csrf = CSRFProtect()

@app.route("/weichat_post", methods=["POST"])
def weichat_post():
    print("posting")
    data = request.form["wei_data"]
    # data = request.form.get('wei_data')
    # data = request.values.get('wei_data')
    print(json.loads(data))

    return jsonify({
        "success": True,
        "return_data": "posted"
    })


@app.route("/weichat_get", methods=["GET"])
def weichat_get():
    print("getting")

    return jsonify({
        "success": True,
        "return_data": "geted"
    })