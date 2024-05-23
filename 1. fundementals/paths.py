from pathlib import Path

# Check if path exists
path = Path("basics")
print(path.exists())

# Return all files matching a glob pattern
python_files = path.glob("*.py")
for file in python_files:
    print(file)


# Return all files in current path
python_files = path.glob("*")
for file in python_files:
    print(file)
