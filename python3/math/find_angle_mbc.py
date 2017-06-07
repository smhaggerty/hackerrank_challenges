import math
# a straight line drawn from the midpoint of the hypotenuse of a right-angled
# triangle to the right angle creates two isosceles triangles. Since triangle
# BCM is isosceles, angle MBC is equal to angle MCB. Angle MCB is equal to
# atan(AB / BC)
ab, bc = int(input()), int(input())
print(str(round(math.degrees(math.atan2(ab,bc)))) + '°')
