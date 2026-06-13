"""
3-Phase Electrical Grid: Synthetic Data Generator
==================================================
Generates normal and Line-to-Ground (LG) fault datasets.
"""
import numpy as np
import pandas as pd

FREQ = 50 
V_PEAK = 325.27 
I_PEAK = 14.14  
DURATION = 0.1  
SAMPLES = 1000  

PHASE_A = 0 
PHASE_B = -2 * np.pi / 3 
PHASE_C = +2 * np.pi / 3 

t = np.linspace(0, DURATION, SAMPLES)
omega = 2 * np.pi * FREQ 

def generate_normal_data(t, noise_level=0.005):
    Va = V_PEAK * np.sin(omega * t + PHASE_A)
    Vb = V_PEAK * np.sin(omega * t + PHASE_B)
    Vc = V_PEAK * np.sin(omega * t + PHASE_C)

    Ia = I_PEAK * np.sin(omega * t + PHASE_A)
    Ib = I_PEAK * np.sin(omega * t + PHASE_B)
    Ic = I_PEAK * np.sin(omega * t + PHASE_C)

    rng = np.random.default_rng(seed=42)
    noise = lambda amp: rng.normal(0, noise_level * amp, size=t.shape)
    
    Va += noise(V_PEAK); Vb += noise(V_PEAK); Vc += noise(V_PEAK)
    Ia += noise(I_PEAK); Ib += noise(I_PEAK); Ic += noise(I_PEAK)

    return pd.DataFrame({
        "time_s": t, "Va_V": Va, "Vb_V": Vb, "Vc_V": Vc,
        "Ia_A": Ia, "Ib_A": Ib, "Ic_A": Ic, "condition": "normal"
    })

def generate_fault_data(t, noise_level=0.005):
    FAULT_START = 0.04
    FAULT_SCALE = 0.05 
    FAULT_I_MULT = 7.0 
    
    rng = np.random.default_rng(seed=99)
    noise = lambda amp: rng.normal(0, noise_level * amp, size=t.shape)
    fault_mask = t >= FAULT_START

    Va = V_PEAK * np.sin(omega * t + PHASE_A)
    Vb = V_PEAK * np.sin(omega * t + PHASE_B)
    Vc = V_PEAK * np.sin(omega * t + PHASE_C)

    Va[fault_mask] *= FAULT_SCALE
    Vb[fault_mask] *= 1.15
    Vc[fault_mask] *= 1.15

    Ia = I_PEAK * np.sin(omega * t + PHASE_A)
    Ib = I_PEAK * np.sin(omega * t + PHASE_B)
    Ic = I_PEAK * np.sin(omega * t + PHASE_C)

    Ia[fault_mask] = (I_PEAK * FAULT_I_MULT) * np.sin(omega * t[fault_mask] + PHASE_A)

    Va += noise(V_PEAK); Vb += noise(V_PEAK); Vc += noise(V_PEAK)
    Ia += noise(I_PEAK); Ib += noise(I_PEAK); Ic += noise(I_PEAK)

    condition = np.where(fault_mask, "LG_fault", "pre_fault")
    
    return pd.DataFrame({
        "time_s": t, "Va_V": Va, "Vb_V": Vb, "Vc_V": Vc,
        "Ia_A": Ia, "Ib_A": Ib, "Ic_A": Ic, "condition": condition
    })

df_normal = generate_normal_data(t)
df_fault = generate_fault_data(t)

df_normal["fault_flag"] = 0
df_fault["fault_flag"] = df_fault["condition"].apply(lambda x: 1 if x == "LG_fault" else 0)

df_combined = pd.concat([df_normal, df_fault], ignore_index=True)
df_combined.to_csv("combined_dataset.csv", index=False)
print("✓ Created combined_dataset.csv")
