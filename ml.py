import pandas as pd
from sklearn.preprocessing import LabelEncoder , StandardScaler
from sklearn.linear_model import LinearRegression

def fiyat_tahmini(user_input):
    print("user_input", user_input)
    # CSV dosyasını oku
    df = pd.read_csv('products.csv')

    # Gerekli sütunları seç
    data_selected = df[['price', 'status']]

    # Bağımsız değişkenleri ve bağımlı değişkeni tanımla
    X = data_selected.drop('price', axis=1).values
    y = data_selected['price'].values

    # Kategorik verileri sayısal verilere dönüştür
    le = LabelEncoder()
    X[:, 0] = le.fit_transform(X[:, 0])


    # Verileri ölçeklendir
    sc = StandardScaler()
    y = y.reshape(-1, 1)
    y = sc.fit_transform(y)

    model = LinearRegression()
    model.fit(X, y)

    # Kullanıcı girişini DataFrame'e dönüştür
    user_input_df = pd.DataFrame(data=user_input, index=[0])

    # Kategorik verileri sayısal verilere dönüştür
    user_input_df['status'] = le.transform(user_input_df['status'])

    # Tahmin yap
    tahmin = model.predict(user_input_df)

    # Tahmini ölçeklendirmeyi geri al
    tahmin = sc.inverse_transform(tahmin)

    # Tahminin güven aralığını hesapla (örneğin standart sapma kullanarak)
    tahmin_std = model.predict(X).std()
    min_tahmin = tahmin - 1.96 * tahmin_std  # %95 güven aralığı için
    max_tahmin = tahmin + 1.96 * tahmin_std

    return [min_tahmin[0][0], max_tahmin[0][0]]

# # Örnek kullanıcı girişi
# kullanici_girisi = {
#     'status': 'used',
# }

# # Fonksiyonu çağırarak fiyat tahmini yap
# tahmin_edilen_fiyat = fiyat_tahmini(kullanici_girisi)

# print("Tahmini fiyat: ", tahmin_edilen_fiyat)
