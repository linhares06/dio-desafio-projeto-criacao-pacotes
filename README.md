# Text Progress Bar

A simple text progress bar for the command line.

## Installation

pip install text-progress-bar

## Usage

```python
from progress_bar.bar import ProgressBar

# Initialize ProgressBar
total_items = 100
pb = ProgressBar(total=total_items, prefix='Progress:', suffix='Complete', length=50)

# Iterate over items
for i in range(total_items):
    # Do some work
    time.sleep(0.1)
    # Update Progress Bar
    pb.print_progress(i + 1)
```

## Author
Felipe

## License
[MIT](https://choosealicense.com/licenses/mit/)
