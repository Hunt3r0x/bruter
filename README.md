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
usage: bruter.py [-h] -f FILE [-u URL] [-l URL_LIST [URL_LIST ...]] [-o OUTPUT]

Fuzz a URL or a list of URLs with lines from a file

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File containing the lines to replace 'FUZZING' with
  -u URL, --url URL     URL containing 'FUZZING' to replace with each line in the file
  -l URL_LIST [URL_LIST ...], --url-list URL_LIST [URL_LIST ...]
                        List of URLs containing 'FUZZING' to replace with each line in the file or a file containing URLs
  -o OUTPUT, --output OUTPUT
                        Output file to write the resulting URLs
```

To use the `bruter.py` tool, run the script with the `-f` and `-u` options to specify the input file and URL, respectively. You can also use the `-o` option to specify an output file.

### Examples :

#### Replace 'FUZZING' with lines from 'payloads.txt' and write the resulting URLs to 'output.txt'
```
python3 bruter.py -f ~/mywordlists/payloads.txt -u https://test-FUZZING.hackerone.com -o output.txt
```
#### USE for multiple URLs at one line

```
python3 bruter.py -f ~/mywordlists/payloads.txt -l https://test-FUZZING.hackerone.com https://test-FUZZING.bugcrowd.com -o output.txt
```
#### USE for multiple URLs from TXT file
```
python3 bruter.py -f ~/mywordlists/payloads.txt -l urls.txt -o output.txt
```
