# Import PyMOL module
from pymol import cmd

#spectrum b, blue_white_red, minimum=0, maximum=10

# Clear any existing movie definitions
cmd.mclear()

# Initialize the movie settings (360 frames, 1 degree per frame)
cmd.mset("1 x360")

# Define the rotation for each frame
for i in range(1, 361):
    cmd.mdo(i, "turn y, 1")

# Optional: Set the display quality
cmd.set("ray_trace_frames", 1)  # Enable ray tracing for higher quality images
cmd.set("cache_frames", 0)      # Disable frame caching to save memory

# Start the movie automatically when the script is run
cmd.mplay()

# Save the frames as PNG files if desired
# Uncomment the line below to save the movie frames as PNG images
# cmd.mpng("output_frame", 1, 360)  # Saves frames from 1 to 360 as output_frame0001.png, etc.

