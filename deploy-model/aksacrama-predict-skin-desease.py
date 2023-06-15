import os
import tensorflow as tf
from keras.preprocessing import image
import keras.utils as image
import numpy as np

# --- Function ---
# Determine class
def what_class(arr_prob_class, type_skin_diseases):
  # Get class with highest probabilty
  index_highest_probability_class  = np.argmax(arr_prob_class)
  if arr_prob_class[index_highest_probability_class] < 0.5:
    return None

  for i in range(len(skin_type_desease)):
    if index_highest_probability_class == i:
      return skin_type_desease[i]
  
# Predict skin desease
def predict_skin_desease(img_path, new_model, skin_type_desease):
    # Convert image for input tensorflow
    img = image.load_img(img_path, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0  # Normalize image

    # Predict image
    predictions = new_model.predict(x)
    return what_class(predictions[0], skin_type_desease)

# --- Run Model ---
# Load Saved_Model
model_path = "./saved_model/ml-aksacarma"
new_model = tf.keras.models.load_model(model_path)

# skin_type_desease
skin_type_desease = [
    'acne and rosacea',
    'bullous disease',
    'eczema',
    'melanoma skin cancer nevi and moles',
    'scabies lyme disease and other infestations and bites',
    'tinea ringworm candidiasis and other fungal infections',
    'urticaria hives',
    'vascular tumors',
    'vasculitis',
    'warts molluscum and other viral infections',
    ]

# Get image that want to predict
path = "/content/drive/MyDrive/Colab Notebooks/dermnet-image-for-train/test/warts-molluscum-and-other-viral-infections/corns-36.jpg"
print(predict_skin_desease(path, new_model, skin_type_desease))