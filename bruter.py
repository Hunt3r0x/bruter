#!/usr/bin/env python3

import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Fuzz a URL or a list of URLs with lines from a file")
    parser.add_argument('-f', '--file', required=True,
                        help="File containing the lines to replace 'FUZZING' with")
    parser.add_argument('-u', '--url', help="URL containing 'FUZZING' to replace with each line in the file")
    parser.add_argument('-l', '--url-list', nargs='+', help="List of URLs containing 'FUZZING' to replace with each line in the file or a file containing URLs")
    parser.add_argument('-o', '--output',
                        help="Output file to write the resulting URLs")
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f"Error: File '{args.file}' does not exist")
        return

    if args.output is None:
        output_file = sys.stdout
    else:
        try:
            output_file = open(args.output, 'w')
        except OSError as e:
            print(
                f"Error: Could not write to output file '{args.output}': {e}")
            return

    try:
        with open(args.file, 'r') as f:
            lines = f.readlines()

        if args.url:
            urls = [args.url]
        elif args.url_list:
            urls = []
            for url_input in args.url_list:
                if os.path.isfile(url_input):
                    with open(url_input, 'r') as url_file:
                        urls.extend(url_file.read().splitlines())
                else:
                    urls.append(url_input)
        else:
            print("Error: Either --url or --url-list must be specified")
            return

        for url in urls:
            for line in lines:
                replaced = url.replace("FUZZING", line.strip())
                output_file.write(replaced + "\n")
    except KeyboardInterrupt:
        print("Program stopped by user")
    finally:
        if args.output is not None:
            output_file.close()
            print(f"Wrote results to '{args.output}'")
        else:
            if output_file != sys.stdout:
                output_file.close()
            else:
                output_file.flush()
            sys.stdout.flush()


if __name__ == '__main__':
    main()
