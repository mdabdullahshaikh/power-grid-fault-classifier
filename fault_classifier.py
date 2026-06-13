"""
Phase 3: Fault Classification Engine
====================================
Implements rule-based logic and a Decision Tree Machine Learning model.
"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

print("Loading features dataset...")
df = pd.read_csv("features_dataset.csv")

# --- 1. EEE Rule-Based Classification ---
Z_THRESHOLD = 15.0 # Ohms
I_THRESHOLD = 20.0 # Amps

def logic_classifier(row):
    if row['Za_Ohm'] < Z_THRESHOLD and row['Ia_RMS'] > I_THRESHOLD:
        return 1 
    return 0 

df['logic_prediction'] = df.apply(logic_classifier, axis=1)

# --- 2. Machine Learning Classification ---
print("\nTraining Decision Tree Model...")
X = df[['Za_Ohm', 'Ia_RMS']]
y = df['fault_flag']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\n--- ML Model Accuracy ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%\n")
print(classification_report(y_test, y_pred, target_names=["Normal", "LG Fault"]))
