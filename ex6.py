weight = float(input())
height = float(input())
weight_kg = weight / 2.2046
height_m = height * 0.0254
print('%.2f' % (weight_kg / (height_m ** 2)))
