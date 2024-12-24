import vtk

# 1. Dizin açma
directory = vtk.vtkDirectory()
path = "/path/to/directory"

if directory.Open(path):
    print(f"Opened directory: {directory.GetPath()}")
    print(f"Number of files: {directory.GetNumberOfFiles()}")

    # 2. Dizin içeriğini listeleme
    for i in range(directory.GetNumberOfFiles()):
        file_name = directory.GetFile(i)
        if directory.FileIsDirectory(i):
            print(f"{file_name} is a directory.")
        else:
            print(f"{file_name} is a file.")
else:
    print(f"Failed to open directory: {path}")

# 3. Yeni bir dizin oluşturma
new_dir = "/path/to/new_directory"
if vtk.vtkDirectory.MakeDirectory(new_dir):
    print(f"Created directory: {new_dir}")
else:
    print(f"Failed to create directory: {new_dir}")
