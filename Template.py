def reward_function(params):

    center_variance = params["distance_from_center"] / params["track_width"]

    # racing line
    left_lane = []  # Fill in the waypoints
    center_lane = []  # Fill in the waypoints
    right_lane = []  # Fill in the waypoints

    # Speed
    fast = []  # 3
    moderate = []  # 2
    slow = []  # 1

    reward = 30

    if params["all_wheels_on_track"]:
        reward += 10
    else:
        reward -= 10

    if params["closest_waypoints"][1] in left_lane and params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in right_lane and not params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in center_lane and center_variance < 0.4:
        reward += 10
    else:
        reward -= 10

    if params["closest_waypoints"][1] in fast:
        if params["speed"] > 1.5:
            reward += 10
        else:
            reward -= 10
    elif params["closest_waypoints"][1] in moderate:
        if params["speed"] > 1 and params["speed"] <= 1.5:
            reward += 10
        else:
            reward -= 10
    elif params["closest_waypoints"][1] in slow:
        if params["speed"] <= 1:
            reward += 10
        else:
            reward -= 10
            
    return float(reward)
