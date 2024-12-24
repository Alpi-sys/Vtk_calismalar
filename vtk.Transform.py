import vtk 

cube = vtk.vtkCubeSource()
cube.SetXLength(5)
cube.SetYLength(5)
cube.SetZLength(5)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cube.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

transform = vtk.vtkTransform()
transform.RotateY(45)
transform.Translate(6,0,0)
transform.Scale(1,2,3)
#transform.Identity()  sıfırlar


actor2 = vtk.vtkActor()
actor2.SetMapper(mapper)

actor.SetUserTransform(transform)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.AddActor(actor2)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

inter = vtk.vtkRenderWindowInteractor()
inter.SetRenderWindow(window)

window.Render()
inter.Start()