
import joblib
from pathlib import Path
import pickle
import os

# Try to load with different methods
preprocessor_path = Path("artifacts/data_transformation/preprocessor.pkl")

print(f"File exists: {os.path.exists(preprocessor_path)}")
print(f"File size: {os.path.getsize(preprocessor_path) if os.path.exists(preprocessor_path) else 'N/A'} bytes")

try:
    # Method 1: joblib
    print("\nTrying joblib.load...")
    preprocessor = joblib.load(preprocessor_path)
    print(f"Success! Type: {type(preprocessor)}")
    print(f"Has transformers attribute: {'transformers' in dir(preprocessor)}")
    
    # Check if fitted
    try:
        from sklearn.utils.validation import check_is_fitted
        check_is_fitted(preprocessor)
        print("Preprocessor is fitted!")
    except Exception as e:
        print(f"Not fitted: {e}")
except Exception as e:
    print(f"Failed: {e}")

try:
    # Method 2: pickle
    print("\nTrying pickle.load...")
    with open(preprocessor_path, 'rb') as f:
        preprocessor = pickle.load(f)
    print(f"Success! Type: {type(preprocessor)}")
    print(f"Has transformers attribute: {'transformers' in dir(preprocessor)}")
    
    # Check if fitted
    try:
        from sklearn.utils.validation import check_is_fitted
        check_is_fitted(preprocessor)
        print("Preprocessor is fitted!")
    except Exception as e:
        print(f"Not fitted: {e}")
except Exception as e:
    print(f"Failed: {e}")
