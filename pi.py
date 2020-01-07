import math

def caclulate_area_of_polygon(n):
    """
    Calculates the area of a regular polygon with n sides inscribed
    within a circle of radius 1.

    Calculation is done by splitting the polygon into n triangles,
    each with a vertex at the center of the polygon and with two
    vertices at adjacent corners of the polygon. The sum of the area
    of these triangles is the area of the polygon.

    As the number of sides approaches infinity, the polygon's area
    will approach pi.
    """
    # Calculate the angle of the triangles' vertices in the center of
    # the polygon.
    inner_angle = 360 / n

    # Calculate the angle of the triangles' vertices on the perimeter
    # of the polygon.
    outer_angle = (180 - inner_angle) / 2

    # Calculate the area of the triangle.
    # NOTE: each triangle is isosceles, and may be split into two
    #       equivalent right triangles. This is useful for calculating
    #       the area of the triangle.
    triangle_area = math.sin(math.radians(inner_angle/2)) * math.cos(math.radians(inner_angle/2))
    return n * triangle_area

def main():
    pi = caclulate_area_of_polygon(10**10)
    print(f'pi ~= {pi:.14}')

if __name__ == '__main__':
    main()
