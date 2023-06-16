# Machine Learning for Aksacarma

This is Machine Learning repository for Aksacarma App. Build for Capstone Project Bangkit 2023.

## Our Machine Learning Member

| Name                  | Bangkit ID  | Path             |
| --------------------- | ----------- | ---------------- |
| Fawwaz Muhammad Tsani | M309DSX0093 | Machine Learning |
| Fitria Nur Afah       | M151DSY1843 | Machine Learning |

## Description About Project

The goal of machine learning project is created a machine learning model to identify various kinds of skin diseases. The following are skin diseases that this model can identify.

- Acne And Rosacea
- Bullous Disease
- Eczema
- Melanoma Skin
- Cancer Nevi And Moles
- Scabies Lyme
- Disease And Other Infestations And Bites
- Tinea Ringworm
- Candidiasis And Other Fungal Infections
- Urticaria Hives
- Vascular Tumors
- Vasculitis
- Warts Molluscum And Other Viral Infections

This repository stores how to build models, save models, and run saved models. The data used to build the model is also available in this repository.

## Infrastructure for Built Model

### Libraries

Model Machine Learning for Aksacarma built with Jupyter Notebook on Google Colab. This Jupyter Notebook also can run in local. For development, the following are libraries which needs to be installed.

```
tensorflow==2.12.0
keras==2.12.0

opendatasets==0.1.22
matplotlib==3.7.1
numpy==1.22.4
```

### Dataset

The data used to build this model was obtained from Kagle, that is [Dermnet](https://www.kaggle.com/datasets/shubhamgoel27/dermnet). This data is merged and re-sorted according to the needs of the training model. The latest data used is available [here](https://github.com/AksaCerma/akscarma-ml/tree/main/dataset/merged-sorted-dermnet).

## How to Use This Project

For using this project you must clone this machine learning project with following command.

`git clone https://github.com/AksaCerma/akscarma-ml.git`

### How to Build Models

Complete steps on how to build the model are available on [ml_aksacarma_development.ipnyb](https://github.com/AksaCerma/akscarma-ml/blob/main/ml_aksacarma_development.ipynb). A summary of the steps is as follows.

1. Get [Dermet Data](https://www.kaggle.com/datasets/shubhamgoel27/dermnet) from Kagle
2. Merge and Sort Data, the result available [here](https://github.com/AksaCerma/akscarma-ml/tree/main/dataset/merged-sorted-dermnet)
3. Split data to train, validation, and test dataset
4. Train model with data
5. Save model

### How to Load Models

Complete steps on how to load the model are available on [ml_aksacarma_development.ipnyb](https://github.com/AksaCerma/akscarma-ml/blob/main/ml_aksacarma_development.ipynb) too. It is located at section `Load Saved Model`. In addition, the model can also be run using the following [code](https://github.com/AksaCerma/akscarma-ml/blob/main/deploy-model/aksacrama-predict-skin-desease.py). Both of these methods have the same code and differ only in the file format and how to run it. Saved models are available at the following [link](https://github.com/AksaCerma/akscarma-ml/tree/main/deploy-model/saved_model/ml-aksacarma).
