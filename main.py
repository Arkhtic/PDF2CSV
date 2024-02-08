import os
import csv
from tkinter import Tk, Button, Label, filedialog
from PyPDF2 import PdfReader

def pdf_to_csv(input_folder, output_folder):
    # Loop through PDF files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            # Extract text from PDF
            text = extract_text(os.path.join(input_folder, filename))

            # Write text to CSV
            csv_filename = os.path.splitext(filename)[0] + '.csv'
            with open(os.path.join(output_folder, csv_filename), 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                for line in text.split('\n'):
                    writer.writerow([line])

            print(f'{filename} converted to CSV successfully.')

def extract_text(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def select_input_folder():
    input_folder = filedialog.askdirectory()
    input_folder_label.config(text=input_folder)

def select_output_folder():
    output_folder = filedialog.askdirectory()
    output_folder_label.config(text=output_folder)

def convert_to_csv():
    input_folder = input_folder_label.cget("text")
    output_folder = output_folder_label.cget("text")
    pdf_to_csv(input_folder, output_folder)
    status_label.config(text="Conversion complete.")

# Create GUI window
root = Tk()
root.title("PDF to CSV Converter")

# Labels
input_folder_label = Label(root, text="Select input folder")
input_folder_label.grid(row=0, column=0)

output_folder_label = Label(root, text="Select output folder")
output_folder_label.grid(row=1, column=0)

status_label = Label(root, text="")
status_label.grid(row=3, column=0)

# Buttons
input_folder_button = Button(root, text="Browse", command=select_input_folder)
input_folder_button.grid(row=0, column=1)

output_folder_button = Button(root, text="Browse", command=select_output_folder)
output_folder_button.grid(row=1, column=1)

convert_button = Button(root, text="Convert", command=convert_to_csv)
convert_button.grid(row=2, column=0, columnspan=2)

# Run the GUI
root.mainloop()
