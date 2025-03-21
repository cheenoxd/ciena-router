import subprocess
import sys
import time
import select

from simulation import read_hardware_state, write_hardware_state, calculate_f, mutate_hardware, mutate_database, create_hardware_file, file_path

def print_cli_history(history):
    for entry in history:
        print(entry)

#Added comments
def process_cli_input(file_path, history, t):
    # Process CLI input here
    try:
        user_input = input("Enter CLI command: ")
        command, *args = user_input.split()
        if command == "set":
            index = int(args[0]) - 1
            value = int(args[1])
            if index < 0 or index >3 :
                print(f"Invalid Input - Error: {index}")
            else:
                mutate_database(file_path, index, value)
                history.append(f"{t} set {index} {value}")
    except Exception as e:
        print(f"Invalid Input - Error: {str(e)}")

def main():
    history = []
    t = 0


    while t < 60:
        state_values, control_values, signal_values = read_hardware_state(file_path)
        t += 1

        # Write Your Code Here Start

        #Case2
         # Write Your Code Here End
        # replace x index with y value
        control_values[signal_values[0] - 1] = signal_values[1]
        write_hardware_state(file_path, state_values, control_values, signal_values)
        history.append(f"{t} set control value {x} to {signal_values[y - 1]}")

        # Case 3
        process_cli_input(file_path, history, t)
    
        # Handle Cron Job (Use Case 4)
        if t % 10 == 0:
            # swap values
            state_values[0], state_values[1] = state_values[1], state_values[0]

            write_hardware_state(file_path, state_values, control_values, signal_values)

            history.append(f"{t} swap {state_values[1]} {state_values[0]}")

  
        # Write Your Code Here End

        time.sleep(1)  # Wait for 1 second before polling again
    print(history)

if __name__ == '__main__':
    main()