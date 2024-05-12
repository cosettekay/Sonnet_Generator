import tkinter as tk
import gpt_2_simple as gpt2

# Define the checkpoint directory and run name
checkpoint_dir = "C:\\Users\\lopez\\Documents\\ML Project\\checkpoint"
run_name = 'run1'

# Start TensorFlow session
sess = gpt2.start_tf_sess()

# Load the fine-tuned model
gpt2.load_gpt2(sess, run_name=run_name, checkpoint_dir=checkpoint_dir)

# Function to generate poem based on user input
def generate_poem(prompt):
    # Generate poem using user input as prefix
    poem = gpt2.generate(sess,
                         length=250,
                         temperature=0.9,
                         top_k=40,
                         top_p=0.9,
                         prefix=prompt,
                         truncate='<|endoftext|',
                         nsamples=1,
                         batch_size=1,
                         return_as_list=True)[0]
    return poem

def generate_poem_from_input():
    prompt = entry.get()
    poem = generate_poem(prompt)
    output_text.config(state='normal')
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, poem)
    output_text.config(state='disabled')

# Create the main window
root = tk.Tk()
root.title("Poem Generator")

# Set window size and position
window_width = 500
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Add custom styling
root.configure(bg='#f0f0f0')  # Set background color
root.option_add('*Font', 'Arial 10')  # Set default font for all widgets

# Create input field
entry = tk.Entry(root, width=50, bg='#ffffff', fg='#333333', font=('Arial', 12), borderwidth=2, relief=tk.FLAT)
entry.pack(pady=20)

# Create generate button
generate_button = tk.Button(root, text="Generate Poem", command=generate_poem_from_input, bg='#4caf50', fg='#ffffff', font=('Arial', 12, 'bold'), relief=tk.RAISED)
generate_button.pack(pady=10)

# Create output text area
output_text = tk.Text(root, height=10, width=50, wrap=tk.WORD, state='disabled', bg='#ffffff', fg='#333333', font=('Arial', 12), borderwidth=2, relief=tk.FLAT)
output_text.pack(pady=20)

# Run the application
root.mainloop()
