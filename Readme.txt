# countlines, a Python Code Counter

countlines is a tool that counts the lines of Python code in all subdirectories of the current working directory. It provides a summary of the line counts for each Python file found, allowing you to analyze the size of your Python codebase.

## Usage

1. Download the `countlines.exe` file from the releases section.
2. Place the `countlines.exe` file in the directory you want to analyze.
3. Double-click the `countlines.exe` file to run it.
4. The tool will traverse through all subdirectories and display the line counts for each Python file found in a formatted table.
5. After the process is complete, a file named `python_code_summary.txt` will be generated in the same directory, containing the output summary.

## Dependencies

The countlines tool does not require any external dependencies. It is a standalone executable that can be run on compatible systems without Python installed.

## Compilation

If you want to compile countlines from source, follow these steps:

1. Clone the repository or download the source code.
2. Install the required dependencies using pip: `pip install pyinstaller`
3. Run the following command to compile the code into an executable:
