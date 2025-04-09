import tkinter as tk
from tkinter import filedialog, messagebox

def process_video(): #processing video
    # Open file picker to choose video
    video_path = filedialog.askopenfilename(title="Select CCTV Video",
                                            filetypes=[("MP4 files", "*.mp4"), ("All Files", "*.*")])
    if video_path:
        # Just simulate processing for now
        messagebox.showinfo("Processing", f"Processing started for:\n{video_path}")
        
        # 🚧 Add your YOLO & OCR code here later
        print("Processing video:", video_path)

        # Simulated result
        messagebox.showinfo("Done", "Violation report generated successfully!")

# Create main window
root = tk.Tk()
root.title("DeepTraffix - Violation Detector")
root.geometry("400x250")
root.configure(bg="#f0f0f0")

# UI Elements
title_label = tk.Label(root, text="🚦 DeepTraffix", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

desc_label = tk.Label(root, text="Upload a CCTV video to detect traffic violations.", bg="#f0f0f0")
desc_label.pack(pady=5)

upload_btn = tk.Button(root, text="📁 Upload Video", font=("Arial", 12), command=process_video, bg="#4CAF50", fg="white", padx=10, pady=5)
upload_btn.pack(pady=20)

# Run the app
root.mainloop()
