# docker-stats-parser

Simple python parser for docker stats output.

## Installation

```
git clone https://github.com/MaximSinyaev/docker-stats-parser
cd docker-stats-parser
pip install -r requirements.txt
pip install .
```

## Usage

If no arguments are provided, the script will save the output to a file `docker_stats.csv` in the current directory.

```docker stats | python -m docker_stats_parser```

You can also specify the output file:

```docker stats | python -m docker_stats_parser output.csv```