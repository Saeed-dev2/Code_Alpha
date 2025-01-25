
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler

# Example data: user song history and target variable (1: repeated play within 30 days, 0: otherwise)
data = pd.DataFrame({
    'user_id': [1, 1, 2, 2, 3, 3],
    'song_id': [101, 102, 101, 103, 104, 105],
    'hour_played': [15, 18, 12, 16, 20, 9],
    'day_of_week': [5, 5, 4, 6, 3, 1],
    'play_count': [5, 3, 8, 10, 2, 4],  # Number of times song was played by user
    'target': [1, 0, 1, 0, 1, 0]  # 1 if played again within 30 days, else 0
})

# Feature and target
X = data[['hour_played', 'day_of_week', 'play_count']]  # Features
y = data['target']  # Target variable

# Scaling features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, zero_division=1))

# Example of making recommendations (predicting for a new user-song pair)
new_data = np.array([[17, 4, 6]])  # New user's features: hour_played, day_of_week, play_count
new_data_scaled = scaler.transform(new_data)
prediction = model.predict(new_data_scaled)

if prediction == 1:
    print("Recommend song (likely to listen again within a month).")
else:
    print("Do not recommend song.")
