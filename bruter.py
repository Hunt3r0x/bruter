#!/usr/bin/env python3

import argparse
import os
import sys


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Fuzz a URL with lines from a file")
    parser.add_argument('-f', '--file', required=True,
                        help="File containing the lines to replace 'FUZZING' with")
    parser.add_argument('-u', '--url', required=True,
                        help="URL containing 'FUZZING' to replace with each line in the file")
    parser.add_argument('-o', '--output',
                        help="Output file to write the resulting URLs")
    args = parser.parse_args()

    # Check that the file exists
    if not os.path.isfile(args.file):
        print(f"Error: file '{args.file}' does not exist")
        return

    # Set the output file to stdout if it is not provided
    if args.output is None:
        output_file = sys.stdout
    else:
        # Check that the output file can be written
        try:
            output_file = open(args.output, 'w')
        except OSError as e:
            print(
                f"Error: could not write to output file '{args.output}': {e}")
            return

    # Read the lines from the file and replace 'FUZZING' with each line
    try:
        with open(args.file, 'r') as f:
            lines = f.readlines()

        for line in lines:
            replaced = args.url.replace("FUZZING", line.strip())
            output_file.write(replaced + "\n")
    except KeyboardInterrupt:
        print("Program stopped by user")
    finally:
        # Close the output file if it's an actual file
        if args.output is not None:
            output_file.close()
            print(f"Wrote results to '{args.output}'")
        else:
            # Print the results to stdout
            if output_file != sys.stdout:
                output_file.close()
            else:
                output_file.flush()  # Flush the buffer to ensure all data is written to stdout
            sys.stdout.flush()  # Flush the buffer to ensure all data is written to stdout


if __name__ == '__main__':
    main()
