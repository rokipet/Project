"""
Test script to verify all packages are installed correctly
"""

print("Testing package imports...")
print("-" * 50)

try:
    import numpy as np
    print(f"[OK] NumPy {np.__version__}")
except ImportError as e:
    print(f"[FAILED] NumPy: {e}")

try:
    import pandas as pd
    print(f"[OK] Pandas {pd.__version__}")
except ImportError as e:
    print(f"[FAILED] Pandas: {e}")

try:
    import matplotlib
    print(f"[OK] Matplotlib {matplotlib.__version__}")
except ImportError as e:
    print(f"[FAILED] Matplotlib: {e}")

try:
    import seaborn
    print(f"[OK] Seaborn {seaborn.__version__}")
except ImportError as e:
    print(f"[FAILED] Seaborn: {e}")

try:
    import sklearn
    print(f"[OK] Scikit-learn {sklearn.__version__}")
except ImportError as e:
    print(f"[FAILED] Scikit-learn: {e}")

try:
    import scipy
    print(f"[OK] SciPy {scipy.__version__}")
except ImportError as e:
    print(f"[FAILED] SciPy: {e}")

print("-" * 50)
print("All packages imported successfully!")
print("\nYour Python environment is ready for the project.")
