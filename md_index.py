"""
Description:

Automated Markdown index creation including Bookmark-links.
The source file name is required to be given (`FILE_NAME`).
A given output file will be created with the Markdown index.
"""

import os

FILE_NAME: str = "playbook.md"
TAB_SIZE: int = 4
DESTINATION_FILE_NAME: str = "index.md"

DIR_PATH: str = os.path.dirname(os.path.realpath(__file__))
PARENT_PATH: str = os.path.abspath(os.path.join(DIR_PATH, os.pardir))
FILE_PATH: str = os.path.join(PARENT_PATH, FILE_NAME)
DESTINATION_PATH: str = os.path.join(DIR_PATH, DESTINATION_FILE_NAME)


def main() -> None:
    # Read all the lines from the file
    file_lines: list[str] = read_file_lines(FILE_PATH)
    # Get all headings (lines starting with #)
    file_headings: list[str] = get_file_headings(file_lines)
    # Create the Markdown index
    file_index: str = create_file_index(file_headings)
    # Write the Markdown index to the destination path
    destination_file: str = write_index(DESTINATION_PATH, file_index)
    # Print info
    print(f"Index of selected Markdown file: '{FILE_PATH}'")
    print(f"is successfully written to:      '{DIR_PATH}/{destination_file}'")


def write_index(file_path: str, index: str) -> str:
    with open(file_path, "w") as f:
        f.write(index)
    return file_path


def set_line(line: str) -> str:
    bookmark: str = ""
    if line.startswith("["):
        line = line[1:].rsplit("]", 1)[0]
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
    index: str = ""
    prefix: str = ""
    line: str = ""
    for heading in headings:
        prefix, line = heading.split(" ", 1)
        prefix = set_prefix(prefix)
        line = set_line(line)
        index += f"{prefix}-   {line}\n"
    return index


def get_file_headings(lines: list[str]) -> list[str]:
    headings: list = []
    for line in lines:
        if line.startswith("#"):
            headings.append(line)
        elif line.startswith("-   #") or line.startswith("- #"):
            headings.append(line.replace("-", "").strip())
    return headings


def read_file_lines(file_path: str) -> list[str]:
    data: list = []
    with open(file_path, "r") as f:
        for x in f:
            data.append(x.replace("\n", ""))
    return data


if __name__ == "__main__":
    main()
