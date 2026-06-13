"""
Phase 4: Data Visualization
===========================
Generates Matplotlib plots comparing normal operations with faults.
"""
import pandas as pd
import matplotlib.pyplot as plt

print("Loading data for visualization...")
df = pd.read_csv("combined_dataset.csv")

df_normal = df[df['condition'] == 'normal']
df_fault = df[df['condition'] != 'normal']

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Normal conditions
ax1.plot(df_normal['time_s'], df_normal['Va_V'], label='Phase A', color='red')
ax1.plot(df_normal['time_s'], df_normal['Vb_V'], label='Phase B', color='blue')
ax1.plot(df_normal['time_s'], df_normal['Vc_V'], label='Phase C', color='green')
ax1.set_title("Normal 3-Phase Voltage")
ax1.set_ylabel("Voltage (V)")
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend(loc="upper right")

# Fault conditions
ax2.plot(df_fault['time_s'], df_fault['Va_V'], label='Phase A (Faulted)', color='red', linewidth=2.5)
ax2.plot(df_fault['time_s'], df_fault['Vb_V'], label='Phase B', color='blue', alpha=0.5)
ax2.plot(df_fault['time_s'], df_fault['Vc_V'], label='Phase C', color='green', alpha=0.5)
ax2.set_title("Line-to-Ground Fault on Phase A (t=0.04s)")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Voltage (V)")
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend(loc="upper right")

plt.tight_layout()
plt.savefig("waveform_comparison.png", dpi=300)
print("✓ Plot saved successfully as waveform_comparison.png")
plt.show()
