from flask import Flask, render_template, request, jsonify
import os
import torch
from torchvision import models, transforms
from torch import nn
from PIL import Image, UnidentifiedImageError

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define the model architecture
class_names = ['No fibrosis', 'Portal', 'Periportal', 'Septal', 'Cirrhosis']
num_classes = len(class_names)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model and weights
try:
    model = models.resnet18(pretrained=False)
    model.fc = nn.Linear(model.fc.in_features, num_classes)  # Update for your dataset
    model.load_state_dict(torch.load('hkth_model.pth', map_location=device))  # Load state_dict
    model = model.to(device)
    model.eval()  # Set to evaluation mode
except Exception as e:
    raise RuntimeError(f"Error loading the model: {e}")

# Image Transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Predict function
def predict(image_path):
    try:
        # Open and preprocess the image
        image = Image.open(image_path).convert('RGB')
        input_tensor = transform(image).unsqueeze(0).to(device)
        # Perform prediction
        with torch.no_grad():
            output = model(input_tensor)
            _, predicted_class = torch.max(output, 1)
        return class_names[predicted_class.item()]
    except UnidentifiedImageError:
        raise ValueError("Uploaded file is not a valid image.")
    except Exception as e:
        raise RuntimeError(f"Error during prediction: {e}")

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        if file:
            # Save the uploaded file
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            # Predict
            prediction = predict(file_path)
            return jsonify({"filename": file.filename, "prediction": prediction}), 200
        else:
            return jsonify({"error": "Invalid file"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500

if __name__ == '__main__':
    # Ensuring the app runs on the correct host and port provided by Render
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
