import sys
import shutil
import os

if len(sys.argv) != 3:
    print("Usage: python file_copy.py <source_file> <destination_file>")
    sys.exit(1)

src = sys.argv[1]
dst = sys.argv[2]

if not os.path.isfile(src):
    print(f"Error: Source file '{src}' does not exist.")
    sys.exit(1)

try:
    shutil.copy(src, dst)
    print(f"File copied successfully from {src} to {dst}")
except Exception as e:
    print(f"Failed to copy file: {e}")

