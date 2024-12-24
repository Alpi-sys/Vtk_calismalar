import vtk


cube = vtk.vtkCubeSource()
cube.SetXLength(5)
cube.SetYLength(5)
cube.SetZLength(5)


plane = vtk.vtkPlane()
plane.SetOrigin(0.0, 0.0, 0.0)  # Düzlemin başlangıç noktası
plane.SetNormal(3.0, 1.0, 2.0)  # Düzlemin normali (x-y düzlemine paralel)

# 3. vtkCutter nesnesini oluştur ve ayarlarını yap
cutter = vtk.vtkCutter()
cutter.SetCutFunction(plane)  # Kesim düzlemini ayarla
cutter.SetInputConnection(cube.GetOutputPort())  # Küpü giriş olarak belirle
cutter.Update()  # Kesim işlemini gerçekleştir



mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cutter.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)


renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(0.1, 0.2, 0.4)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

inter = vtk.vtkRenderWindowInteractor()
inter.SetRenderWindow(window)

window.Render()
inter.Start()