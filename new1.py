import pandas as pd

# Read the traffic trajectory data from the Excel file
data =pd.read_excel('/Users/mdehteshamazam/Downloads/traffic_data.xlsx')

# Calculate the microscopic parameters of traffic flow
microscopic_parameters = calculate_microscopic_parameters(data)

# Calculate the macroscopic parameters of traffic flow
macroscopic_parameters = calculate_macroscopic_parameters(data)

# Calculate the capacity of the road
capacity = calculate_capacity(data)

# Print the results
print(microscopic_parameters.to_string())
print(macroscopic_parameters.to_string())
print('Capacity of the road:', capacity)

def calculate_microscopic_parameters(data):
  """Calculates microscopic parameters of traffic flow.

  Args:
    data: A Pandas DataFrame containing the following columns:
      - frame: Frame number
      - vehicle_id: Vehicle ID
      - x: X coordinate of vehicle
      - y: Y coordinate of vehicle
      - length: Length of vehicle
      - width of vehicle
      - lane_number: Lane number

  Returns:
    A Pandas DataFrame containing the following columns:
      - vehicle_id: Vehicle ID
      - headway: Headway
      - spacing: Spacing
      - time_headway: Time headway
  """

  # Calculate headway
  headway = data['x'].diff()

  # Calculate spacing
  spacing = headway * data['speed']

  # Calculate time headway
  time_headway = spacing / data['speed']

  # Return a Pandas DataFrame containing the microscopic parameters
  return pd.DataFrame({'vehicle_id': data['vehicle_id'],
                       'headway': headway,
                       'spacing': spacing,
                       'time_headway': time_headway})

def calculate_macroscopic_parameters(data):
  """Calculates macroscopic parameters of traffic flow.

  Args:
    data: A Pandas DataFrame containing the following columns:
      - frame: Frame number
      - vehicle_id: Vehicle ID
      - x: X coordinate of vehicle
      - y: Y coordinate of vehicle
      - length: Length of vehicle
      - width of vehicle
      - lane_number: Lane number

  Returns:
    A Pandas DataFrame containing the following columns:
      - traffic_density: Traffic density
      - traffic_flow: Traffic flow
      - speed: Speed
  """

  # Calculate traffic density
  traffic_density = data['vehicle_id'].count() / data['length_of_road_section']

  # Calculate traffic flow
  traffic_flow = data['vehicle_id'].count() / data['time_period']

  # Calculate speed
  speed = data['distance_traveled'] / data['time_taken']

  # Return a Pandas DataFrame containing the macroscopic parameters
  return pd.DataFrame({'traffic_density': traffic_density,
                       'traffic_flow': traffic_flow,
                       'speed': speed})

def calculate_capacity(data):
  """Calculates the capacity of the road.

  Args:
    data: A Pandas DataFrame containing the following columns:
      - frame: Frame number
      - vehicle_id: Vehicle ID
      - x: X coordinate of vehicle
      - y: Y coordinate of vehicle
      - length: Length of vehicle
      - width of vehicle
      - lane_number: Lane number

  Returns:
    The capacity of the road (in vehicles per hour)
  """

  # Calculate the average headway
  average_headway = data['time_headway'].mean()

  # Calculate the capacity of the road
  capacity = (data['speed'].mean() * data['traffic_density'].mean()) / average_headway

  return capacity
