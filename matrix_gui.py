import tkinter as tk
from tkinter import messagebox, Text, Frame, Label, Button
import numpy as np
import sys

class MatrixApp:
    def __init__(self, root):
        """Initializes the GUI application."""
        self.root = root
        self.root.title("Matrix Operations Tool")
        self.root.geometry("650x550")

        # --- Create Frames ---
        # Frame for Matrix Inputs
        frame_input = Frame(root, pady=10)
        frame_input.pack(fill="x")

        # Frame for Operation Buttons
        frame_ops = Frame(root, pady=5)
        frame_ops.pack(fill="x")

        # Frame for the Result
        frame_result = Frame(root, pady=10)
        frame_result.pack(fill="both", expand=True)

        # --- Input Frame Widgets ---
        # Matrix A
        Label(frame_input, text="Matrix A", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10)
        self.txt_matrix_a = Text(frame_input, height=8, width=35, font=("Courier New", 10))
        self.txt_matrix_a.grid(row=1, column=0, padx=10, pady=5)
        self.txt_matrix_a.insert("1.0", "1 2 3\n4 5 6") # Example data

        # Matrix B
        Label(frame_input, text="Matrix B", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10)
        self.txt_matrix_b = Text(frame_input, height=8, width=35, font=("Courier New", 10))
        self.txt_matrix_b.grid(row=1, column=1, padx=10, pady=5)
        self.txt_matrix_b.insert("1.0", "7 8\n9 1\n2 3") # Example data

        # --- Operations Frame Widgets ---
        # Group buttons in a sub-frame for better centering
        button_container = Frame(frame_ops)
        button_container.pack()

        Button(button_container, text="A + B", width=12, command=self.add).pack(side="left", padx=5)
        Button(button_container, text="A - B", width=12, command=self.subtract).pack(side="left", padx=5)
        Button(button_container, text="A × B (Multiply)", width=12, command=self.multiply).pack(side="left", padx=5)
        Button(button_container, text="Transpose (A)", width=12, command=self.transpose).pack(side="left", padx=5)
        Button(button_container, text="Determinant (A)", width=12, command=self.determinant).pack(side="left", padx=5)

        # --- Result Frame Widgets ---
        Label(frame_result, text="Result", font=("Arial", 12, "bold")).pack()
        self.txt_result = Text(frame_result, height=10, width=70, font=("Courier New", 12), state="disabled")
        self.txt_result.pack(padx=10, pady=5, fill="both", expand=True)

    def parse_matrix_from_text(self, text_widget):
        """
        Reads text from a Text widget and converts it to a NumPy array.
        Raises ValueError if parsing fails.
        """
        text = text_widget.get("1.0", "end-1c").strip()
        if not text:
            raise ValueError("Matrix input is empty.")
            
        matrix = []
        rows = text.split('\n')
        
        # Check for consistent column lengths
        expected_cols = -1
        
        for r_idx, row_str in enumerate(rows):
            if not row_str.strip(): # Skip empty lines
                continue
            
            try:
                # Split by space, comma, or tab
                elements = [float(x) for x in row_str.replace(',', ' ').replace('\t', ' ').split()]
            except ValueError as e:
                raise ValueError(f"Non-numeric data found in row {r_idx + 1}: '{row_str}'")

            if not elements:
                continue
                
            if expected_cols == -1:
                expected_cols = len(elements)
            elif len(elements) != expected_cols:
                raise ValueError(f"Inconsistent row lengths. Row {r_idx + 1} has {len(elements)} columns, expected {expected_cols}.")
                
            matrix.append(elements)
            
        if not matrix:
            raise ValueError("No valid matrix data entered.")
            
        return np.array(matrix)

    def set_result_text(self, result):
        """Displays the result (or text) in the result text box."""
        self.txt_result.config(state="normal")
        self.txt_result.delete("1.0", "end")
        
        if isinstance(result, np.ndarray):
            # Format NumPy array for clean output
            np.set_printoptions(precision=4, suppress=True)
            self.txt_result.insert("1.0", str(result))
        else:
            # For scalar results like determinant
            self.txt_result.insert("1.0", f"{result:.6f}")
            
        self.txt_result.config(state="disabled")

    # --- Operation Handlers ---

    def perform_operation(self, operation):
        """A generic handler to parse, execute, and handle errors."""
        try:
            # Get matrices based on the operation
            A = self.parse_matrix_from_text(self.txt_matrix_a)
            
            if operation in ['add', 'subtract', 'multiply']:
                B = self.parse_matrix_from_text(self.txt_matrix_b)
                if operation == 'add':
                    result = A + B
                elif operation == 'subtract':
                    result = A - B
                else: # multiply
                    result = A @ B
            elif operation == 'transpose':
                result = A.T
            elif operation == 'determinant':
                result = np.linalg.det(A)
                
            self.set_result_text(result)

        except (ValueError, np.linalg.LinAlgError) as e:
            messagebox.showerror("Operation Error", f"Error: {e}\n\nPlease check your inputs and matrix dimensions.")
        except Exception as e:
            messagebox.showerror("Input Error", f"Could not parse matrix inputs.\nDetails: {e}")

    # --- Button Click Callbacks ---
    
    def add(self):
        self.perform_operation('add')

    def subtract(self):
        self.perform_operation('subtract')

    def multiply(self):
        self.perform_operation('multiply')

    def transpose(self):
        self.perform_operation('transpose') # Note: Only uses Matrix A

    def determinant(self):
        self.perform_operation('determinant') # Note: Only uses Matrix A


if __name__ == "__main__":
    # Check for NumPy
    if np is None:
        print("Error: The 'numpy' library is not installed.")
        print("Please install it using: pip install numpy")
        sys.exit(1)
        
    root = tk.Tk()
    app = MatrixApp(root)
    root.mainloop()