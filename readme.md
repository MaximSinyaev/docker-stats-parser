# docker-stats-parser

Simple python parser for docker stats output.

## Installation

```bash
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

You will see output like this:

```text
CONTAINER ID    NAME    CPU %   MEM USAGE       MEM  LIMIT      MEM %   NET I   NET O   BLOCK I BLOCK O PIDS    timestamp
f40b78cb8d28    unruffled_pike  3.44%   499.2MiB         7.667GiB       6.36%   2.15kB   564B   12.7MB   7.34MB 223     2023-02-22 12:23:08
504b213c51f4    milvus-etcd     2.02%   8.52MiB          7.667GiB       0.11%   1.58kB   0B     0B       0B     11      2023-02-22 12:23:08
```

During work will be generating a file `docker_stats.csv` with the following content:

```csv
CONTAINER ID,NAME,CPU %,MEM USAGE ,MEM  LIMIT,MEM %,NET I,NET O,BLOCK I,BLOCK O,PIDS,timestamp
f40b78cb8d28,unruffled_pike,1.49%,499MiB , 7.667GiB,6.36%,2.15kB , 564B,12.7MB , 7.29MB,223,2023-02-22 12:21:19
504b213c51f4,milvus-etcd,0.66%,8.516MiB , 7.667GiB,0.11%,1.58kB , 0B,0B , 0B,11,2023-02-22 12:21:19
f40b78cb8d28,unruffled_pike,1.49%,499MiB , 7.667GiB,6.36%,2.15kB , 564B,12.7MB , 7.29MB,223,2023-02-22 12:21:20
504b213c51f4,milvus-etcd,0.66%,8.516MiB , 7.667GiB,0.11%,1.58kB , 0B,0B , 0B,11,2023-02-22 12:21:20
f40b78cb8d28,unruffled_pike,7.13%,499MiB , 7.667GiB,6.36%,2.15kB , 564B,12.7MB , 7.29MB,223,2023-02-22 12:21:20
504b213c51f4,milvus-etcd,9.28%,8.516MiB , 7.667GiB,0.11%,1.58kB , 0B,0B , 0B,11,2023-02-22 12:21:20
```

## License

MIT