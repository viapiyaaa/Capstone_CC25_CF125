import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load model hanya sekali
model = load_model("best_model.keras")

# Label pelatihan dan pemetaan
class_labels = ['battery', 'biological', 'cardboard', 'clothes', 'glass',
                'metal', 'paper', 'plastic', 'shoes', 'trash']

remap_dict = {
    'battery': 'residu',
    'biological': 'organik',
    'cardboard': 'anorganik',
    'clothes': 'residu',
    'glass': 'anorganik',
    'metal': 'anorganik',
    'paper': 'anorganik',
    'plastic': 'anorganik',
    'shoes': 'residu',
    'trash': 'residu'
}

spesifik_info = {
    'battery': 'Baterai bekas harap dibuang ke e-waste center agar tidak mencemari lingkungan.',
    'biological': 'Sisa makanan bisa dikomposkan menjadi pupuk alami.',
    'cardboard': 'Kardus bekas dapat dilipat dan dijual atau didaur ulang.',
    'clothes': 'Pakaian bekas bisa disumbangkan atau dibuang di tempat residu.',
    'glass': 'Botol dan kaca dikumpulkan untuk didaur ulang, hati-hati pecahan.',
    'metal': 'Kaleng dan logam dibersihkan dan dijual ke pengepul.',
    'paper': 'Kertas bersih bisa dikumpulkan dan dijual ke bank sampah.',
    'plastic': 'Plastik dibersihkan, dipisahkan dan didaur ulang.',
    'shoes': 'Sepatu masih layak pakai bisa disumbangkan, sisanya ke sampah residu.',
    'trash': 'Sampah ini tidak dapat didaur ulang, buang sesuai prosedur.'
}

def predict_image(img_pil):
    img = img_pil.resize((150, 150))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0]
    predicted_index = np.argmax(prediction)
    confidence = prediction[predicted_index]

    label = class_labels[predicted_index]
    jenis = remap_dict[label]
    info = spesifik_info.get(label, "Informasi belum tersedia.")

    return label, jenis, confidence, info
