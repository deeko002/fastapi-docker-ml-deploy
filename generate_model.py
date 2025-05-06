import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_model():
    # Read the training data from the CSV file
    data = pd.read_csv('train.csv')

    # Check if the required columns are in the dataset
    if 'feature1' not in data.columns or 'feature2' not in data.columns or 'label' not in data.columns:
        print("Error: The dataset must contain 'feature1', 'feature2', and 'label' columns.")
        exit(1)

    # Separate features and labels
    X = data[['feature1', 'feature2']]  # Features
    y = data['label']  # Label

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model's performance
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model Accuracy: {accuracy * 100:.2f}%')

    # Save the model to a file using joblib
    joblib.dump(model, 'model.pkl')
    print("Model saved as 'model.pkl'")

if __name__ == "__main__":
    train_model()