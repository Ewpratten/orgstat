# orgstat
`orgstat` is a simple python CLI tool that will produce a ranked list of contributors for a GitHub organization based on commit count across all repos.

## Installation

To install, ensure you have `python3` and `python3-pip` installed, then run:

```sh
python3 -m pip install git+https://github.com/ewpratten/orgstat.git
```

## Usage

```
usage: orgstat [-h] -k KEY org

positional arguments:
  org                Name of GitHub organization

optional arguments:
  -h, --help         show this help message and exit
  -k KEY, --key KEY  GitHub API key
```