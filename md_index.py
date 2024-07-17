""" Description:
Automated Markdown index creation including Bookmarks.
A Markdown file can be selected with the Filedialog.
An output file will be created with the Markdown index.
"""

import tkinter as tk
from tkinter import filedialog

TAB_SIZE = 4


def main():
    # Select a Markdown file
    file_path = file_selection_dialog()
    # If no file is selected, quit the script
    if file_path == "":
        quit()
    # Read all the lines from the file
    file_lines = read_file_lines(file_path)
    # Get all headings (lines starting with #)
    file_headings = get_file_headings(file_lines)
    # Create the Markdown index
    file_index = create_file_index(file_headings)
    # Get the source path
    source_path = file_path.rsplit("/", 1)[0]
    # Write the Markdown index to the destination path
    destination_path = write_index("index.md", file_index)
    # Print info
    print(f"Index of selected Markdown file: '{file_path}'")
    print(f"is successfully written to:      '{source_path}/{destination_path}'")


def write_index(file_path: str, index: str) -> str:
    with open(file_path, "w") as f:
        f.write(index)
    return file_path


def set_line(line: str) -> str:
    bookmark = ""
    for char in line:
        if char.isalnum():
            bookmark += char.lower()
        elif char == "-" or char == " ":
            bookmark += "-"
        elif char == "_":
            bookmark += "_"
    return f"[{line}](#{bookmark})"


def set_prefix(prefix: str) -> str:
    return prefix[1:].replace("#", "\t").expandtabs(TAB_SIZE)


def create_file_index(headings: list[str]) -> str:
    index = ""
    for heading in headings:
        prefix, line = heading.split(" ", 1)
        prefix = set_prefix(prefix)
        line = set_line(line)
        index += f"{prefix}-   {line}\n"
    return index


def get_file_headings(lines: list[str]) -> list[str]:
    headings = []
    for line in lines:
        if line.startswith("#"):
            headings.append(line)
    return headings


def read_file_lines(file_path: str, encoding: str = None) -> list[str]:
    data = []
    with open(file_path, "r", encoding=encoding) as f:
        for x in f:
            data.append(x.replace("\n", ""))
    return data


def file_selection_dialog(initial_dir: str = "") -> str:
    root = tk.Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    file_path = filedialog.askopenfilename(
        filetypes=[("Markdown Files", "*.md")],
        initialdir=initial_dir,
        title="Select a Markdown file",
        parent=root,
    )
    root.destroy()
    return file_path


if __name__ == "__main__":
    main()
