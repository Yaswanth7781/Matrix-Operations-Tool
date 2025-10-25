# Matrix Operations Tool

A simple desktop application built with Python, NumPy, and Tkinter. This tool provides a user-friendly graphical interface (GUI) to perform common matrix operations.



## Features

* **Interactive GUI:** Easily enter matrix data into text boxes.
* **Matrix Addition (A + B):** Adds two matrices of the same dimensions.
* **Matrix Subtraction (A - B):** Subtracts one matrix from another of the same dimensions.
* **Matrix Multiplication (A × B):** Performs matrix multiplication (dot product).
* **Matrix Transpose (Aᵀ):** Calculates the transpose of Matrix A.
* **Matrix Determinant (det(A)):** Calculates the determinant of Matrix A (must be a square matrix).
* **Structured Output:** Displays results in a clean, readable format.
* **Error Handling:** Provides pop-up alerts for mathematical errors (e.g., mismatched dimensions) or input-parsing errors.

## How to Use

There are two ways to use this application: by running the standalone app (easiest) or by running the Python script directly.

### Option 1: Using the Standalone Application

This is the recommended method for most users, as it does not require Python or any libraries to be installed.

1.  Go to the "Releases" page of this project's repository.
2.  Download the `MatrixTool.exe` (for Windows) or `MatrixTool.app` (for macOS) file.
3.  Double-click the file to run it.
4.  Enter your matrices into the **"Matrix A"** and **"Matrix B"** text boxes.
    * Separate numbers with a **space** (e.g., `1 2 3`).
    * Start each new row on a **new line**.
5.  Click the operation button you wish to perform.
6.  The result will appear in the "Result" box at the bottom.

### Option 2: Running from the Python Source

This method is for developers or users who have Python installed and want to run the code directly.

#### Prerequisites

* [Python 3.x](https://www.python.org/downloads/)
* [NumPy](https://numpy.org/install/)
* [Tkinter](https://docs.python.org/3/library/tkinter.html) (This is included by default with most Python installations for Windows and macOS).

#### Steps

1.  Clone this repository or download the source code:
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  Install the required `numpy` library:
    ```bash
    pip install numpy
    ```

3.  Run the application:
    ```bash
    python matrix_gui.py
    ```

## How to Build from Source (Optional)

If you want to create your own standalone executable (`.exe` or `.app`) from the Python script, you can use **PyInstaller**.

1.  Install PyInstaller:
    ```bash
    pip install pyinstaller
    ```

2.  Navigate to the project directory and run the following command in your terminal:
    ```bash
    pyinstaller --onefile --windowed --name "MatrixTool" matrix_gui.py
    ```
    * `--onefile`: Bundles everything into a single executable.
    * `--windowed`: Prevents the console window from appearing when the GUI app runs.

3.  Your new executable file will be located in the `dist` folder.

