import shapes

rectangle = shapes.Rectangle(16, 18)
print("perimeter_rectangle: ", rectangle.perimeter)
print("area_rectangle: ", rectangle.area)

square = shapes.Square(2)
print("area_square: ", square.area)
print("perimeter_square: ", square.perimeter)

circle = shapes.Circle(7)
print("circle_area: ", circle.area)
print("circle_perimeter", circle.perimeter)

tangle = shapes.Triangle(A=2, B=3, C=3)
print(tangle.perimeter)

cylinder = shapes.Cylinder(5, 2)
print("cylinder_lateral_surface_area: ", cylinder.lateral_surface_area)
print("cylinder_total_surface_area: ", cylinder.total_surface_area)
print("cylinder_volume: ", cylinder.volume)

sphere = shapes.Sphere(5)
print("sphere_area: ", sphere.area)
print("sphere_volume: ", sphere.volume)

ellipse = shapes.Ellipse(10, 20)
print("ellipse_area: ", ellipse.area)
print("ellipse_perimeter: ", ellipse.perimeter)
