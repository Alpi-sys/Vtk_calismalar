import vtk

# 1. FieldData oluştur
fieldData = vtk.vtkFieldData()

# 2. Birinci dizi ekle
array1 = vtk.vtkDoubleArray()
array1.SetName("Array1")
array1.SetNumberOfValues(3)
array1.SetValue(0, 1.0)
array1.SetValue(1, 2.0)
array1.SetValue(2, 3.0)
fieldData.AddArray(array1)

# 3. İkinci dizi ekle
array2 = vtk.vtkIntArray()
array2.SetName("Array2")
array2.SetNumberOfValues(2)
array2.SetValue(0, 10)
array2.SetValue(1, 20)
fieldData.AddArray(array2)

# 4. Dizilere eriş
print(f"Number of arrays: {fieldData.GetNumberOfArrays()}")
print("Array Names:")
for i in range(fieldData.GetNumberOfArrays()):
    print(f"  - {fieldData.GetArrayName(i)}")

# 5. Bir dizinin içeriğini yazdır
array = fieldData.GetArray("Array1")
if array:
    print("Array1 Values:", [array.GetValue(i) for i in range(array.GetNumberOfValues())])

# 6. FieldData'yı temizle
fieldData.Initialize()
print(f"Number of arrays after initialization: {fieldData.GetNumberOfArrays()}")
