import vtk

#source başlangıç
cube = vtk.vtkCubeSource()
cube.SetXLength(10)
cube.SetYLength(5)
cube.SetZLength(20)
#source bitiş

#mapper başlangıç
mapper = vtk.vtkPolyDataMapper()
#mapper.SetInputData(cube)#dosya olduğu gibi gönderilir
mapper.SetInputConnection(cube.GetOutputPort())
#mapper bitiş

#actor başlangıç
actor = vtk.vtkActor()
actor.SetMapper(mapper)
#actor bitiş

#renderer başlangıç
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
#renderer bitiş

#window başlangıç
window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)
#window bitiş

inter = vtk.vtkRenderWindowInteractor()
inter.SetRenderWindow(window)

window.Render()
inter.Start()
