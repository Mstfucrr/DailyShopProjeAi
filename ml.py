import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder , LabelEncoder
from sklearn.linear_model import LinearRegression

def fiyat_tahmini(user_input):
    # CSV dosyasını oku
    df = pd.read_csv('data.csv')

    # Gerekli sütunları seç
    data_selected = df[['price', 'status']]

    # Bağımsız değişkenleri ve bağımlı değişkeni tanımla
    X = data_selected.drop('price', axis=1)
    y = data_selected['price']

    # Kategorik verileri sayısal verilere dönüştür
    le = LabelEncoder()
    X['status'] = le.fit_transform(X['status'])
    # Kategorik verileri one-hot encoding ile sayısal verilere dönüştür
    ohe = ColumnTransformer([('ohe', OneHotEncoder(dtype=float), [0])], remainder='passthrough')
    X = ohe.fit_transform(X)

    # Modeli eğit
    model = LinearRegression()
    model.fit(X, y)
    
    # Kullanıcı girişini DataFrame'e çevir
    user_input_df = pd.DataFrame(user_input, index=[0])

    # Kullanıcı girişindeki kategorik verileri sayısal verilere dönüştür
    user_input_df['status'] = le.transform(user_input_df['status'])

    # Kullanıcı girişindeki kategorik verileri one-hot encoding ile sayısal verilere dönüştür
    user_input_df = ohe.transform(user_input_df)


    # Tahmin yap
    tahmin = model.predict(user_input_df)

    return tahmin[0]


# # Örnek kullanıcı girişi
# kullanici_girisi = {
#     'status': 'used',
#     'name': 'Nike Air Max',
# }

# # Fonksiyonu çağırarak fiyat tahmini yap
# tahmin_edilen_fiyat = fiyat_tahmini(kullanici_girisi)

# print("Tahmini fiyat: ", tahmin_edilen_fiyat)
