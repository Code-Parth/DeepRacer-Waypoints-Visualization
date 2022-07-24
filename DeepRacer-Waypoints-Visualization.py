import matplotlib.pyplot as plt
import numpy as np

# Name Of your Map
track_name = "2022_june_open"

# Folder Path Where Your .NPY Files are saved
absolute_path = "./Maps-Waypoints-NPY-Files/"

waypoints = np.load("%s/%s.npy" % (absolute_path, track_name))

print("Number of waypoints = " + str(waypoints.shape[0]))
for i, point in enumerate(waypoints):
    waypoint = (point[2], point[3])
    plt.scatter(waypoint[0], waypoint[1])
    print("Waypoint " + str(i) + ": " + str(waypoint))

plt.show()
