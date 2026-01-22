# 🩺 Diabetes Prediction

## 📌 Project Overview
This repository contains a machine learning project that predicts the likelihood of diabetes based on patient health data.  
The dataset **`diabetes.csv`** is included in the **`data/`** folder, so no external download is required.

---



### Used Technologies / Libraries / Tools : 
                                                              - Flask (For GUI)
                                                              - Random Forest Classifier (For Machine Learning Model)
                                                              - Pandas (For Data cleaning , Data visulization)
                                                              - Numpy 
                                                              - HTML / CSS (For Stylish Interface) 
   

                                                              
                          

---


## ⚙️ How to Use

### Option 1: Run the Web App (Recommended)
You can directly use the pre‑trained model by running the Flask app:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```


### Option 2:  Train the model by yourself using **`notebook.ipynb`** (if you                    wish to learn.) :
 
1. **Open** **`notebook.ipynb`** file.
2. **Data Loading** – Reads `data/diabetes.csv`.
3. **Run each cell** one by one. 
4. **Evaluation** – Reports accuracy, precision, recall, F1-score, and ROC curve.  
5. **Prediction** – Generates predictions for new patient data.

---


---

## 📂 Repository Structure :
```
📂 Diabetes Prediction/
 ┣ 📁 data/
 ┃ ┗ 📄 diabetes.csv
 ┣ 📁 templates/
 ┃ ┗ 📄 index.html
 ┣ 📓 app.py
 ┣ 🧠 model.pkl   
 ┣ 📓 notebook.ipynb
 ┣ 📄 requirements.txt
 ┗ 📄 README.md
```


