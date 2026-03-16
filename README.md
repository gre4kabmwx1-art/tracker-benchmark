# tracker-benchmark

Benchmark tool for computer vision trackers.

## Features

- IoU calculation
- CLI interface
- Unit tests with pytest
- GitHub Actions CI

## Installation

```bash
pip install -e .
```

## Usage

```bash
tracker-benchmark run --box-a 0,0,100,100 --box-b 50,50,150,150
```

## Example output

```text
IoU score: 0.1429
```

## Development

Run tests:

```bash
pytest
```
