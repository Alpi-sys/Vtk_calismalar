import vtk

actor = vtk.vtkActor()

# Sınıf adını öğrenme
print(f"Sınıf adı: {actor.GetClassName()}")

# Tür kontrolü
print(f"Bu nesne vtkActor mı? {actor.IsA('vtkActor')}")
print(f"Bu nesne vtkObjectBase mi? {actor.IsA('vtkCamera')}")

