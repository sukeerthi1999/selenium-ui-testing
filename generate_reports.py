import cv2
import os

def generate_heatmap(diff_img):
    try:
        heatmap = cv2.applyColorMap(diff_img, cv2.COLORMAP_JET)
        return heatmap
    except Exception as e:
        print(f"Error generating heatmap: {e}")
        return None

# Explicitly set the report directory path
REPORT_DIR = r"C:\Users\saisu\Computer vision project\screenshots\reports"
ANOMALY_DIR = r"C:\Users\saisu\Computer vision project\screenshots\anomalies"

# Create the report directory if it doesn't exist
os.makedirs(REPORT_DIR, exist_ok=True)

# Process each anomaly image
for filename in os.listdir(ANOMALY_DIR):
    if filename.endswith(".png"):
        anomaly_path = os.path.join(ANOMALY_DIR, filename)
        diff_img = cv2.imread(anomaly_path)
        
        if diff_img is not None:
            heatmap = generate_heatmap(diff_img)
            if heatmap is not None:
                # Save the heatmap in the reports directory
                report_path = os.path.join(REPORT_DIR, f"heatmap_{filename}")
                cv2.imwrite(report_path, heatmap)
                print(f"Heatmap saved for {filename} as {report_path}")
            else:
                print(f"Failed to generate heatmap for {filename}")
        else:
            print(f"Anomaly image not found for {filename}")

print("Result reporting completed.")
