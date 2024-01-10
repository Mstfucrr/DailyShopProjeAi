# flask api ile bilgi alacak

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

from DataPull import get_products_by_category_id_data
from ml import fiyat_tahmini

app = Flask(__name__)
CORS(app, resources={r"/get_quote": {"origins": "http://localhost:5173"}}, supports_credentials=True)

@app.route('/get_quote', methods=['POST'])
def get_quote():
    req = request.get_json()
    try :
        category = req["data"]["category"]
        is_deleted_datas = "true"
        get_products_by_category_id_data(category, is_deleted_datas)
        user_input = {
            'status': req["data"]["status"],
        }
        res = {
            "message": "Ürünler fiyat önerisi başarılı bir şekilde getirildi.",
            "status": 200,
            "data":{ "min" : fiyat_tahmini(user_input)[0].round(2)
                    , "max" : fiyat_tahmini(user_input)[1].round(2)
            }
        }
        
    except Exception:
        res = {
            "message": "Ürünler fiyat önerisi getirilirken bir hata oluştu.",
            "status": 400,
        }
        return jsonify(res)  # Hata durumu için 400 HTTP durumu

    response = jsonify(res)
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response


@app.route('/test', methods=['GET'])
def test():
    return "test"

if __name__ == '__main__':
    app.run(debug=True)

    