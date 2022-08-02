import matplotlib.pyplot as plt
import numpy as np

# Name Of your Map
track_name = "2022_july_open"

# Folder Path Where Your .NPY Files are saved
absolute_path = "./Maps-Waypoints-NPY-Files/"

waypoints = np.load("%s/%s.npy" % (absolute_path, track_name))

print("Number of waypoints = " + str(waypoints.shape[0]))   

for x in range(int((waypoints.size)/6)):
  waypoint = waypoints[x]
  str1="$"
  str2=str(x+1)
  str3=str1+str2+str1
  for y in range(3):
    waypoint_x = waypoint[2*y]
    waypoint_y = waypoint[2*y+1]
    plt.scatter(waypoint_x, waypoint_y, marker=str3, s=50, c='black')

plt.show()