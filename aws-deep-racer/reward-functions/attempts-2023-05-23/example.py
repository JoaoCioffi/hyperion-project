"""
Consider this official documentation for the parameters:

{
    "all_wheels_on_track": Boolean,        # flag to indicate if the agent is on the track
    "x": float,                            # agent's x-coordinate in meters
    "y": float,                            # agent's y-coordinate in meters
    "closest_objects": [int, int],         # zero-based indices of the two closest objects to the agent's current position of (x, y).
    "closest_waypoints": [int, int],       # indices of the two nearest waypoints.
    "distance_from_center": float,         # distance in meters from the track center 
    "is_crashed": Boolean,                 # Boolean flag to indicate whether the agent has crashed.
    "is_left_of_center": Boolean,          # Flag to indicate if the agent is on the left side to the track center or not. 
    "is_offtrack": Boolean,                # Boolean flag to indicate whether the agent has gone off track.
    "is_reversed": Boolean,                # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    "heading": float,                      # agent's yaw in degrees
    "objects_distance": [float, ],         # list of the objects' distances in meters between 0 and track_length in relation to the starting line.
    "objects_heading": [float, ],          # list of the objects' headings in degrees between -180 and 180.
    "objects_left_of_center": [Boolean, ], # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
    "objects_location": [(float, float),], # list of object locations [(x,y), ...].
    "objects_speed": [float, ],            # list of the objects' speeds in meters per second.
    "progress": float,                     # percentage of track completed
    "speed": float,                        # agent's speed in meters per second (m/s)
    "steering_angle": float,               # agent's steering angle in degrees
    "steps": int,                          # number steps completed
    "track_length": float,                 # track length in meters.
    "track_width": float,                  # width of the track
    "waypoints": [(float, float), ]        # list of (x,y) as milestones along the track center

}

Now build a "Follow the centerline" (Sections the track into three reward zones. The farther the car strays from the centerline, the less it’s rewarded) considering:

- the track is re:invent 2018
- it's a PPO
- the race type is time trial
- the current benchmark time is 00:55.457 (1st opponent) -> The function could, for example, get a reward if completes the lap and more reward if it is faster than benchmark_time
- I realized in the streaming video (training steps) the car sometimes got out of the track borders. How to add a penalty if the car goes outside the track boundaries? And can you please include rewards for 3 complete laps without going outside the track?

You can include even more parameters considering:
- Compare the car heading direction with the track direction.
- Compare the performance with benchmark number of steps and time to finish.
- Check whether the current waypoint is part of the straight lane.
"""



def reward_function(params):
    # Example of rewarding the agent to stay inside the two borders of the track

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    is_crashed = params['is_crashed']
    progress = params['progress']
    steps = params['steps']

    # Set benchmark time (you can adjust this value)
    benchmark_time = 20.000

    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if all wheels are on the track and the agent is within the track borders
    if all_wheels_on_track and distance_from_center <= 0.5 * track_width:
        reward = 1.0

    # Additional conditions to consider for extra rewards
    # Reward completion of the lap
    if progress == 100:
        reward += 10.0

    # Reward if the agent finishes the lap faster than the benchmark time
    if steps > 0 and (steps / 15) < benchmark_time:
        reward += 20.0

    # Subtract a penalty if the agent crashes
    if is_crashed:
        reward -= 10.0

    # Always return a float value
    return float(reward)


import math
def reward_function(params):
    # Input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    is_offtrack = params['is_offtrack']
    steps = params['steps']
    waypoints = params['waypoints']
    heading = params['heading']
    track_length = params['track_length']
    benchmark_time = 20.000  # Benchmark time in seconds

    # Define reward zones
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Initialize rewards
    reward = 1e-3  # Default reward for being off track or crashed

    # Check if car is on track
    if not is_offtrack:
        # Calculate reward for following the centerline
        if distance_from_center <= marker_1:
            reward = 1.0
        elif distance_from_center <= marker_2:
            reward = 0.5
        elif distance_from_center <= marker_3:
            reward = 0.1

        # Compare car heading direction with track direction
        next_waypoint = waypoints[params['closest_waypoints'][1]]
        track_direction = math.atan2(next_waypoint[1] - params['y'], next_waypoint[0] - params['x'])
        track_direction = math.degrees(track_direction)
        direction_diff = abs(track_direction - heading)
        if direction_diff > 180:
            direction_diff = 360 - direction_diff

        # Adjust reward based on direction difference
        direction_threshold = 10.0
        if direction_diff > direction_threshold:
            reward *= 0.8

        # Compare performance with benchmark time and number of steps
        if progress == 100:
            # Convert steps to time in seconds
            time_in_seconds = steps / 15.0
            if time_in_seconds < benchmark_time:
                reward += 10.0
            else:
                reward -= 10.0

        # Penalty for going outside the track boundaries
        boundary_penalty = 1e-3
        if distance_from_center > 0.5 * track_width:
            reward -= boundary_penalty

        # Additional rewards for completing laps without going off track
        laps_without_offtrack = params['steps'] // params['track_length']
        if laps_without_offtrack >= 3:
            reward += 100.0

    return reward


def reward_function(params):
    # Input parameters for "Follow the centerline" strategy
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    is_offtrack = params['is_offtrack']
    steps = params['steps']
    waypoints = params['waypoints']
    heading = params['heading']
    benchmark_time = 55.457  # Benchmark time in seconds

    # Define reward zones for "Follow the centerline"
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Initialize rewards for "Follow the centerline"
    reward = 1e-3  # Default reward for being off track or crashed

    # Check if car is on track for "Follow the centerline"
    if not is_offtrack:
        # Calculate reward for following the centerline for "Follow the centerline"
        if distance_from_center <= marker_1:
            reward = 1.0
        elif distance_from_center <= marker_2:
            reward = 0.5
        elif distance_from_center <= marker_3:
            reward = 0.1

        # Compare car heading direction with track direction for "Follow the centerline"
        next_waypoint = waypoints[params['closest_waypoints'][1]]
        track_direction = math.atan2(next_waypoint[1] - params['y'], next_waypoint[0] - params['x'])
        track_direction = math.degrees(track_direction)
        direction_diff = abs(track_direction - heading)
        if direction_diff > 180:
            direction_diff = 360 - direction_diff

        # Adjust reward based on direction difference for "Follow the centerline"
        direction_threshold = 10.0
        if direction_diff > direction_threshold:
            reward *= 0.8

        # Compare performance with benchmark time and number of steps for "Follow the centerline"
        if progress == 100:
            # Convert steps to time in seconds
            time_in_seconds = steps / 15.0
            if time_in_seconds < benchmark_time:
                reward += 10.0
            else:
                reward -= 10.0

    # Input parameters for "Prevent Zig-Zag" behavior
    abs_steering = abs(params['steering_angle'])  # Only need the absolute steering angle

    # Steering penalty threshold for "Prevent Zig-Zag" behavior, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the car is steering too much for "Prevent Zig-Zag" behavior
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return float(reward)


def reward_function(params):
    # Input parameters for "Follow the centerline" strategy
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    is_offtrack = params['is_offtrack']
    steps = params['steps']
    waypoints = params['waypoints']
    heading = params['heading']
    benchmark_time = 55.457  # Benchmark time in seconds
    speed = params['speed']

    # Define reward zones for "Follow the centerline"
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Initialize rewards for "Follow the centerline"
    reward = 1e-3  # Default reward for being off track or crashed

    # Check if car is on track for "Follow the centerline"
    if not is_offtrack:
        # Calculate reward for following the centerline for "Follow the centerline"
        if distance_from_center <= marker_1:
            reward = 1.0
        elif distance_from_center <= marker_2:
            reward = 0.5
        elif distance_from_center <= marker_3:
            reward = 0.1

        # Compare car heading direction with track direction for "Follow the centerline"
        next_waypoint = waypoints[params['closest_waypoints'][1]]
        track_direction = math.atan2(next_waypoint[1] - params['y'], next_waypoint[0] - params['x'])
        track_direction = math.degrees(track_direction)
        direction_diff = abs(track_direction - heading)
        if direction_diff > 180:
            direction_diff = 360 - direction_diff

        # Adjust reward based on direction difference for "Follow the centerline"
        direction_threshold = 10.0
        if direction_diff > direction_threshold:
            reward *= 0.8

        # Compare performance with benchmark time and number of steps for "Follow the centerline"
        if progress == 100:
            # Convert steps to time in seconds
            time_in_seconds = steps / 15.0
            if time_in_seconds < benchmark_time:
                reward += 10.0
            else:
                reward -= 10.0

    # Input parameters for "Prevent Zig-Zag" behavior
    abs_steering = abs(params['steering_angle'])  # Only need the absolute steering angle

    # Steering penalty threshold for "Prevent Zig-Zag" behavior, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the car is steering too much for "Prevent Zig-Zag" behavior
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    # Adjust reward based on speed for straight lines
    straight_reward = 1.0  # Base reward for straight lines
    straight_line_speed_threshold = 3.0  # Adjust the threshold as needed
    if abs(heading) < 5.0 and speed > straight_line_speed_threshold:  # Consider small heading angles as straight lines
        straight_reward *= speed / straight_line_speed_threshold  # Increase reward proportionally with speed

    # Combine the rewards from "Follow the centerline" and "Prevent Zig-Zag"
    reward = max(reward, straight_reward)

    return float(reward)
