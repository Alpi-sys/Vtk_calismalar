import vtk

# 1. Veri nesnesi oluştur
dataObject = vtk.vtkDataObject()

# 2. FieldData oluştur ve ekle
fieldData = vtk.vtkFieldData()
array = vtk.vtkDoubleArray()
array.SetName("MyData")
array.SetNumberOfValues(3)
array.SetValue(0, 1.0)
array.SetValue(1, 2.0)
array.SetValue(2, 3.0)

fieldData.AddArray(array)
dataObject.SetFieldData(fieldData)

# 3. Veriyi kopyala
copiedObject = vtk.vtkDataObject()
copiedObject.DeepCopy(dataObject)

# 4. FieldData içeriğini yazdır
field = copiedObject.GetFieldData()
print(f"Array Name: {field.GetArray(0).GetName()}")
print(f"Values: {[field.GetArray(0).GetValue(i) for i in range(field.GetArray(0).GetNumberOfValues())]}")

# 5. Tür bilgisi yazdır
print("Data Type:", copiedObject.GetDataObjectType())