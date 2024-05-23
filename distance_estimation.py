known_speed_bump_height = 0.1    #The actual height of the speed bump in meters.
focal_length = 0.0035            #The focal length of the camera in meters
image_width = 640                #The width of the image captured by the camera in pixels
bbox={
    "width": 0,
    "height": 0
}

def estimate_distance(known_speed_bump_height, focal_length, image_width, bbox):
  """
  Estimates distance based on bounding box information and camera parameters.

  Args:
      known_speed_bump_height: Actual height of the speed bump in meters.
      focal_length: Focal length of the camera in meters.
      image_width: Width of the image captured by the camera in pixels.
      bbox: Bounding box information (e.g., dictionary containing width and height).

  Returns:
      Estimated distance between camera and speed bump in meters.
  """
  pixel_width, pixel_height = bbox["width"], bbox["height"]  # Assuming dictionary format
  distance = (known_speed_bump_height * focal_length * image_width) / (pixel_width * pixel_height)
  return distance
