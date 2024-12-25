import cv2
import os

def preprocess_image(image_path):
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return None  # Skip processing if the file doesn't exist

    try:
        img = cv2.imread(image_path)
        if img is None:
            print(f"Failed to load image: {image_path}")
            return None
        
        img_resized = cv2.resize(img, (1024, 768))
        img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
        return img_gray
    except Exception as e:
        print(f"Error in preprocessing image {image_path}: {e}")
        return None

BASELINE_DIR = r"C:\Users\saisu\Computer vision project\screenshots\baseline"
CURRENT_DIR = r"C:\Users\saisu\Computer vision project\screenshots\current"
PROCESSED_DIR = r"C:\Users\saisu\Computer vision project\screenshots\processed"

os.makedirs(PROCESSED_DIR, exist_ok=True)

# Preprocess images (grayscale and resize)
for filename in os.listdir(CURRENT_DIR):
    if filename.endswith(".png"):
        # Modify the filename to match the baseline image (replace '_current' with '_baseline')
        baseline_filename = filename.replace("_current", "_baseline")
        
        baseline_path = os.path.join(BASELINE_DIR, baseline_filename)
        current_path = os.path.join(CURRENT_DIR, filename)
        
        # Debugging: print the paths being processed
        print(f"Processing {filename}...")
        print(f"Baseline image path: {baseline_path}")
        print(f"Current image path: {current_path}")
        
        # Check if both baseline and current images exist
        if not os.path.exists(baseline_path):
            print(f"Baseline image not found: {baseline_path}")
            continue
        if not os.path.exists(current_path):
            print(f"Current image not found: {current_path}")
            continue
        
        baseline_img = preprocess_image(baseline_path)
        current_img = preprocess_image(current_path)
        
        if baseline_img is not None and current_img is not None:
            cv2.imwrite(os.path.join(PROCESSED_DIR, f"processed_{filename}"), baseline_img)
            cv2.imwrite(os.path.join(PROCESSED_DIR, f"processed_{filename.replace('baseline', 'current')}"), current_img)
            print(f"Preprocessed images saved for {filename}")
        else:
            print(f"Preprocessing failed for {filename}")

print("Image preprocessing completed.")
