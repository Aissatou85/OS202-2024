import random

def calculate_pi_sequential(num_points):
  points_in_circle = 0

  for i in range(num_points):
   x , y = random.uniform(-1, 1), random.uniform(-1,1)
   distance = x**2 + y**2
   if distance <= 1:
     points_in_circle += 1

   pi_approximation = 4 * (points_in_circle / num_points)
   return pi_approximation

num_points = 100000
pi_sequential = calculate_pi_sequential(num_points)
print("approximation de pi en séquentiel", pi_sequential)




