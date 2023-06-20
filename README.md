# BRUTER Tool

The `bruter.py` tool is a command-line utility for replacing the string `FUZZING` in a URL with lines from a file. The resulting URLs can be written to an output file or to standard output.

## Installation

To use the `bruter.py` tool, you need to have Python 3 installed on your system. You can download Python 3 from the official website: https://www.python.org/downloads/

Once you have installed Python 3, you can download the `bruter.py` script from the GitHub repository:

```
$ git clone https://github.com/Hunt3r0x/bruter.git
```

## Usage

The `bruter.py` tool is a command-line utility that accepts the following options:

```
usage: bruter.py [-h] -f FILE -u URL [-o OUTPUT]

Fuzz a URL with lines from a file

optional arguments:
  -h, --help        show this help message and exit
  -f FILE, --file FILE  File containing the lines to replace 'FUZZING' with
  -u URL, --url URL   URL containing 'FUZZING' to replace with each line in the file
  -o OUTPUT, --output OUTPUT
        Output file to write the resulting URLs
```

To use the `bruter.py` tool, run the script with the `-f` and `-u` options to specify the input file and URL, respectively. You can also use the `-o` option to specify an output file.

Examples:

#### Replace 'FUZZING' with lines from 'payloads.txt' and write the resulting URLs to 'output.txt'

```
python3 bruter.py -f ~/mywordlists/subdomains.txt -u https://test-FUZZING.hackerone.com
