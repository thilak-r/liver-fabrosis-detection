# 🌟 Liver Fibrosis Detection using Deep Learning

## 🩺 **Why is Liver Fibrosis Detection Important?**
Liver fibrosis is a serious medical condition caused by the excessive buildup of connective tissue in the liver due to chronic damage. Left untreated, it can progress to cirrhosis and even liver failure, significantly impacting patients' lives. Early and accurate detection of liver fibrosis is critical for timely intervention and effective treatment, reducing the burden on patients and healthcare systems.
--
⭐ If you like this project, don't forget to give it a star on GitHub!  

---
<a href="https://github.com/thilak-r/liver-fabrosis-detection/blob/main/Original-ResNet-18-Architecture.png">
  <img src="https://raw.githubusercontent.com/thilak-r/liver-fabrosis-detection/main/Original-ResNet-18-Architecture.png" 
       alt="Original ResNet-18 Architecture" 
       style="max-width: 100%; height: auto; display: block; margin: auto;">
</a>

---
## 🚀 **Project Overview**
This project is an advanced AI-based system to detect and classify liver fibrosis stages (F0 to F4) from medical images. Using a pretrained **ResNet-18** model and optimized training methods, our model achieves high accuracy and reliability in distinguishing between subtle stages of fibrosis.

---

##  **Key Features**
- **Non-Invasive Analysis**: Provides predictions directly from liver images, reducing reliance on biopsies.
- **ResNet-18 Backbone**: Fine-tuned for classifying five fibrosis stages with high precision.
- **Performance Monitoring**: Integrated **confusion matrix** and **training vs. validation accuracy plots**.
- **Data Augmentation**: Enhanced feature extraction to address class imbalances and improve performance.

---

## 📊 **Dataset Summary**
- **Total Images**: 6,323
- **Classes**:
  - `F0`: Normal liver tissue (2,114 images)
  - `F1`: Portal fibrosis without septum (861 images)
  - `F2`: Portal fibrosis with fewer septa (793 images)
  - `F3`: Many septa but no cirrhosis (857 images)
  - `F4`: Liver cirrhosis (1,698 images)
    
- **Data Split**:
  - **Training Set**: 70%
  - **Validation Set**: 15%
  - **Test Set**: 15%
    
---

### Confusion Matrix
<p align="center">
  <img src="https://github.com/user-attachments/assets/55bec119-9aac-492b-91da-6844072cadee" alt="Confusion Matrix" width="600">
</p>

--- 

### Training vs Validation Accuracy
<p align="center">
  <img src="https://github.com/user-attachments/assets/95490d0d-dba1-4dbc-a482-e087bc787132" alt="Training vs Validation Accuracy" width="600">
</p>

---


## ⚙️ **Technologies Used**

| **Technology**       | **Logo**                                                                                  |
|-----------------------|-------------------------------------------------------------------------------------------|
| **Python**           | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **PyTorch**          | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) |
| **Flask**            | ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) |
| **HTML**             | ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) |
| **CSS**              | ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) |
| **JavaScript**       | ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) |
| **Matplotlib**       | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white) |

---

## 📂 **Folder Structure**

.
├── app.py                # Flask app for the project
├── model.pth             # Trained PyTorch model
├── dataset/              # Folder containing the liver fibrosis dataset
├── templates/            # Contains HTML frontend files
├── static/               # CSS, JavaScript, and images for the frontend
├── images/               # Screenshots, confusion matrix, and accuracy plots
└── README.md             # Project documentation


---

## 🚀 **How to Run This Project**
1. Clone the repository:
   ```bash
   git clone https://github.com/thilak-r/liver-fibrosis-detection.git
   cd liver-fibrosis-detection

2. Install Dependencies: 
Run the following command to install all required dependencies:
   ```bash 
   pip install -r requirements.txt

3. Run the Flask App
Start the Flask application by running:
   ```bash
   python app.py

4. Open Your Browser
Navigate to the following address in your web browser to access the application:
   ```bash
   http://127.0.0.1:5000

   
---


### 🔑 **Results**

Our model demonstrated exceptional accuracy and robust performance across all fibrosis stages, from F0 (healthy tissue) to F4 (severe cirrhosis). By effectively handling the challenges of differentiating between early fibrosis stages such as F1, F2, and F3—which often exhibit subtle and overlapping characteristics—the model proves its reliability for clinical-grade liver fibrosis detection.

Leveraging the power of the pretrained ResNet-18 architecture, combined with advanced data augmentation techniques and extensive training, the model excels in identifying key patterns within medical imaging data. The integration of a balanced dataset and careful preprocessing ensures its robustness and adaptability across various scenarios. Moreover, the use of metrics like the confusion matrix and ROC curves validates its high precision and recall across all classes, ensuring minimal misclassifications.

This achievement highlights the model's potential for real-world applications, such as:

Non-invasive diagnosis of liver fibrosis, reducing the need for painful and invasive biopsies.
Early-stage detection that empowers healthcare professionals to intervene promptly, potentially halting or reversing disease progression.
Monitoring disease progression and treatment efficacy in patients with chronic liver conditions.

---
under guidance of [Dr Agughasi Victor Ikechukwu](https://github.com/Victor-Ikechukwu)
---



## ❤️ Thank You!
Thank you for checking out our project! We hope this inspires you to explore the intersection of AI and healthcare. Feel free to reach out for questions, suggestions, or collaborations.

---
