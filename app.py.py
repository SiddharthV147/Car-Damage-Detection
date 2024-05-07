import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image
import h5py

model = load_model('Models/vgg_best_model.h5')
# model1 = load_model('/content/drive/MyDrive/Car_Damage_Detection/Models/mobil_best_model.h5')


def preprocess_image(img):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def print_weigths(model, img):
  def list_datasets_in_group(file_path, group_name):
      with h5py.File(file_path, 'r') as f:
          group = f[group_name]
          datasets = list(group.keys())
      return datasets

  # Usage
  file_path = 'Models/mobil_best_model.h5'  # replace with your .h5 file path
  output=[]
  # List datasets in 'model_weights' group
  model_datasets = list_datasets_in_group(file_path, 'model_weights')

  output.append(model_datasets)

  # List datasets in 'optimizer_weights' group
  optimizer_datasets = list_datasets_in_group(file_path, 'optimizer_weights')

  output.append(optimizer_datasets)
  return output



def predict_damage_classification(model, img):
    img = preprocess_image(img)
    prediction = model.predict(img)[0][0]
    
    if prediction > 0.5:
        label = "Damaged"
    else:
        label = "Not Damaged"
    return label


st.markdown("<h1 style='text-align: center; color: White;'>Car Damage Assessment</h1><br><br> ", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
  st.markdown("<br>", unsafe_allow_html=True)
  img = Image.open(uploaded_file)
  st.image(img, caption='Uploaded Image.', use_column_width=True)
  
  predict_damage=st.button("Predict")
  
  if predict_damage:
    st.write("")
    # st.markdown("<br><p style='text-align: center; color: White;'>Classifying...</p> <br>", unsafe_allow_html=True)

    label1 = predict_damage_classification(model, img)
    if label1 == "Damaged":
            st.markdown("<p style='text-align: center; color: White;'>The Car is Damaged</p> ", unsafe_allow_html=True)

    else:
            st.markdown("<p style='text-align: center; color: White;'>The car is not Damaged</p> ", unsafe_allow_html=True)
  
  give_lables=st.button("Give Lables")
  if give_lables:
    lables2=print_weigths(model,img)
    st.write(lables2)
      

else:

  st.markdown("<br><p style='text-align: center; color: White;'>No image has been uploaded yet.... upload your image</p> <br><br>", unsafe_allow_html=True)

