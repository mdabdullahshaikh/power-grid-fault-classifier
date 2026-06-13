# Power Grid Fault Classifier ⚡

An automated, data-driven Python application designed to simulate and classify Line-to-Ground (LG) electrical faults on a 3-phase power grid. 

This project serves as a practical execution of applying programmatic logic to core EEE concepts like instantaneous power, root mean square algorithms, and impedance calculations. Building this system from scratch is a core module in a focused progression toward achieving professional-level software architecture proficiency.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Engineering:** NumPy, Pandas
* **Machine Learning:** Scikit-Learn (Decision Trees)
* **Visualization:** Matplotlib

## 📂 Repository Structure
* `generate_grid_data.py`: Generates synthetic time-series AC wave data.
* `feature_extraction.py`: Computes rolling RMS and system impedance dynamically.
* `fault_classifier.py`: Evaluates grid health using hardcoded thresholds and ML classifiers.
* `visualize_waveforms.py`: Renders comparative analytical plots.

## 🚀 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Generate the electrical datasets: `python generate_grid_data.py`
3. Extract core features (Z and RMS): `python feature_extraction.py`
4. Train and test the classifier: `python fault_classifier.py`
5. Generate performance visuals: `python visualize_waveforms.py`
