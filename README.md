# RandomizeTextLines

RandomizeTextLines is a Python script for randomizing the lines listed in a .txt file.

## Usage

```bash
py RandomizeTextLines.py testfile.txt
```

```python
import sys
from RandomizeTextLines import randomize_text_lines

file = "C:/Users/Strangeh21/Desktop/testfile.txt"
randomize_text_lines(file)
```
Creates a new file named testfile-SHUFFLED.txt where the text lines inside have been randomized.

## License
[MIT](https://choosealicense.com/licenses/mit/)