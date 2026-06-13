"""
Phase 2: Mathematical Feature Extraction
==================================================
Calculates Rolling RMS and Impedance (Z) using vectorized Pandas logic.
"""
import pandas as pd
import numpy as np

print("Loading combined dataset...")
df = pd.read_csv("combined_dataset.csv")

CYCLE_SAMPLES = 200

def calculate_rolling_rms(series, window_size):
    return np.sqrt(series.pow(2).rolling(window=window_size, min_periods=1).mean())

print("Calculating core features...")
df['Va_RMS'] = calculate_rolling_rms(df['Va_V'], CYCLE_SAMPLES)
df['Ia_RMS'] = calculate_rolling_rms(df['Ia_A'], CYCLE_SAMPLES)

epsilon = 1e-6
df['Za_Ohm'] = df['Va_RMS'] / (df['Ia_RMS'] + epsilon)
df['Sa_VA'] = np.abs(df['Va_V'] * df['Ia_A'])

df.to_csv("features_dataset.csv", index=False)
print("✓ Saved extracted features to features_dataset.csv")
