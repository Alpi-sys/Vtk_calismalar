import vtk

texture_reader = vtk.vtkJPEGReader()
texture_reader.SetFileName("Assets/Textures/Cat_diffuse.jpg")
texture_reader.Update()

reader = vtk.vtkOBJReader()
reader.SetFileName("Assets/Sources/cat_1.obj")
reader.Update()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())

texture = vtk.vtkTexture()
texture.SetInputConnection(texture_reader.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.SetTexture(texture)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

inter = vtk.vtkRenderWindowInteractor()
inter.SetRenderWindow(window)

window.Render()
inter.Start()