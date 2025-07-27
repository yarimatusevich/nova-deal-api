from nova_act_service import request_nova
from flask import Flask, jsonify
from flask_cors import CORS
from urllib.parse import unquote

app = Flask(__name__)
CORS(app)
@app.route("/product/<product_name>", methods = ["Get"])
def search_deals(product_name: str):
    unquote(product_name) # decoding percent-encoded characters in url string
    deal_list = request_nova(product_name)

    return jsonify(deals = deal_list.model_dump())

if __name__ == "__main__":
    app.run(port = 8080)