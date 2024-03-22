import sys
print(sys.path)


import pyautogui
import time

# Function to get the mouse coordinates
def get_click_coordinates():
    print("Move the mouse to the desired position and press Ctrl+C to exit...")
    try:
        while True:
            x, y = pyautogui.position()
            position_str = f"X: {x} Y: {y}"
            print(position_str, end='\r', flush=True)
    except KeyboardInterrupt:
        print("\nCoordinates captured.")

# Set a delay before starting (in case you need to position the cursor)
time.sleep(5)

# Function to write the results to a file
def write_results(results_file, success_count, failure_count, entry):
    with open(results_file, 'a') as file:
        if entry:
            file.write(f"Entry {entry}: Success\n")
            print(f"Entry {entry}: Success")
        else:
            file.write(f"Entry {entry}: Failure\n")
            print(f"Entry {entry}: Failure")

# Get the click coordinates
get_click_coordinates()

#placehodler text

# Set the coordinates here
click_x = int(input("Enter the X coordinate: "))
click_y = int(input("Enter the Y coordinate: "))

results_file = "results.txt"  # File to store the results
success_count = 0
failure_count = 0

# Loop through all four-digit numbers
with open(results_file, 'w') as file:
    for i in range(10000):
        number = str(i).zfill(4)

        pyautogui.write(number, interval=0.1)
        pyautogui.click(click_x, click_y)

        # Add a delay between each iteration (adjust as needed)
        time.sleep(1)

        # Simulating success/failure (modify as per your validation logic)
        success = True  # Replace this with your success validation logic
        if success:
            success_count += 1
            write_results(results_file, success_count, failure_count, number)
        else:
            failure_count += 1
            write_results(results_file, success_count, failure_count, number)

print(f"Total Successes: {success_count}, Total Failures: {failure_count}")
