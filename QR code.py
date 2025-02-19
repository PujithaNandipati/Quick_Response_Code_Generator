import tkinter as T
from tkinter import messagebox
from PIL import Image, ImageTk
import pyqrcode

# Function to generate and display QR code
def generate_qr():
    # Get the URL entered by the user
    url = entered_url.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return
    
    try:
        # Generate the QR code
        qr = pyqrcode.create(url)
        qr.png("qr_code.png", scale=6)  # Save the QR code temporarily
        
        # Load the QR code image and display it in the label
        img = Image.open("qr_code.png")
        qr_image = ImageTk.PhotoImage(img)
        qr_label.config(image=qr_image)
        qr_label.image = qr_image  # Keep reference to prevent garbage collection
        messagebox.showinfo("Success", "QR Code generated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
window = T.Tk()
window.title("QR Code Generator")
window.geometry("400x500")

# Add a label and entry box for the URL
label = T.Label(window, text="Enter URL:", font=("Arial", 12))
label.pack(pady=10)

entered_url = T.Entry(window, width=40, font=("Arial", 10))
entered_url.pack(pady=10)

# Add a button to generate the QR code
generate_button = T.Button(window, text="Generate QR Code", font=("Arial", 10), bg="lightblue", command=generate_qr)
generate_button.pack(pady=20)

# Add a label to display the generated QR code
qr_label = T.Label(window, text="Your QR Code will appear here", font=("Arial", 10))
qr_label.pack(pady=20)

# Run the application
window.mainloop()
