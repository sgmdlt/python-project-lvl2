### Hexlet tests and linter status:
[![Actions Status](https://github.com/sgmdlt/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/sgmdlt/python-project-lvl2/actions)
[![Python CI](https://github.com/sgmdlt/python-project-lvl2/actions/workflows/python_ci.yml/badge.svg?event=push)](https://github.com/sgmdlt/python-project-lvl2/actions/workflows/python_ci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/af8221f6a553ed177b75/maintainability)](https://codeclimate.com/github/sgmdlt/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/af8221f6a553ed177b75/test_coverage)](https://codeclimate.com/github/sgmdlt/python-project-lvl2/test_coverage)

## Gendiff

### a simple utility for comparing two files

* Supports input formats as JSON and YAML
* Output in three formats: plain, tree-like and JSON
* Use as CLI utility or library

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install gendiff.

```bash
pip install --user git+https://github.com/sgmdlt/python-project-lvl2.git
```

## Usage

### As library function

```python
from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2, style)
print(diff)
```

### As CLI util

```bash
❯ gendiff -h
usage: gendiff [-h] [-f {json,plain,stylish}] first_file second_file

Generate difference of two JSON or YAML files.

positional arguments:
  first_file            path to first file
  second_file           path to second file

optional arguments:
  -h, --help            show this help message and exit
  -f [stylish, plain, json], --format [stylish, plain, json]
                        set format of output (default: stylish)
```

## Usage examples

As you can see, it's pretty straightforward

[![asciicast](https://asciinema.org/a/6PxthfHSbvWfjUpNu8DbVB2sS.svg)](https://asciinema.org/a/6PxthfHSbvWfjUpNu8DbVB2sS)

___
What about nested files?

[![asciicast](https://asciinema.org/a/Yl5lbYWFGVcUS6JSQovNRX4nL.svg)](https://asciinema.org/a/Yl5lbYWFGVcUS6JSQovNRX4nL)

___
'Plain style' output

[![asciicast](https://asciinema.org/a/yORDhCLBgLrePB5VxH5NcAenV.svg)](https://asciinema.org/a/yORDhCLBgLrePB5VxH5NcAenV)

___
Output is JSON

[![asciicast](https://asciinema.org/a/OpqfH7kf1hwAwauXwpVA1bET2.svg)](https://asciinema.org/a/OpqfH7kf1hwAwauXwpVA1bET2)
