# Mushroom Image Classification AI

This repository contains the code and resources for a deep learning-based Mushroom Image Classification AI. The model is designed to distinguish between edible and poisonous mushrooms using image inputs, providing users with an easy way to assess mushroom safety.

## Features
- Image classification for edible and poisonous mushrooms
- Deep learning-based model trained on a labeled dataset
- User-friendly interface for uploading mushroom images
- Real-time predictions with confidence scores

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/michlleee/mushroom-image-classification-ai.git
   ```
2. Navigate to the project directory:
   ```bash
   cd mushroom-image-classification-ai
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download the dataset (if applicable) and place it in the appropriate directory.

## Usage
To run the model and classify images:

```bash
python main.py --image_path path/to/your/image.jpg
```

Alternatively, if the project includes a web interface:

```bash
python app.py
```
Then, open your browser and navigate to `http://localhost:5000` to use the interface.

## Dataset
The model is trained on a dataset containing images of edible and poisonous mushrooms from https://www.kaggle.com/datasets/derekkunowilliams/mushrooms. The dataset is preprocessed and augmented to improve accuracy.

## Model
- Custom Convolutional Neural Network (CNN) architecture
- Trained using TensorFlow
- Accuracy above 70%

## Contributions
Contributions are welcome! Feel free to submit pull requests or open issues for bug fixes and improvements.


