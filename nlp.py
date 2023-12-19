import tkinter as tk
from tkinter import scrolledtext
from summarizer import Summarizer

def generate_summary():
    input_text = text_input.get("1.0", "end-1c")
    if input_text:
        model = Summarizer()
        summary = model(input_text)
        text_output.config(state="normal")
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, summary)
        text_output.config(state="disabled")

# Create the main application window
root = tk.Tk()
root.title("Text Summarization App")

# Create and configure the input text area
text_input_label = tk.Label(root, text="Input Text:")
text_input_label.pack()

text_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
text_input.pack()

# Create and configure the generate button
generate_button = tk.Button(root, text="Generate Summary", command=generate_summary)
generate_button.pack(pady=10)

# Create and configure the output text area
text_output_label = tk.Label(root, text="Summary:")
text_output_label.pack()

text_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10, state="disabled")
text_output.pack()

# Run the application
root.mainloop()
