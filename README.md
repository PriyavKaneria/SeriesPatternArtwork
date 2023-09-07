# SeriesPatternArtwork
Beautiful patterns were seen expressing the fundamental nature of symmetry with modular arithmetic in common math sequences

I was trying to plot the sequences as visualized in a circle using python turtle.The circle was divided into "n" points. The numbers in the sequences were modded with "n" and the resulting number was used to mark the next point in the circle while connecting it with the last point.

The sequences used were:
1. Fibonacci Sequence
2. Prime Numbers
3. Square Numbers
4. Cube Numbers
5. Power Sequence
6. Recaman Sequence

> If you want to, please feel free to add more sequences to the code. Try them out with different values of "n" and share the results. If the patters are really interesting, add them to the best configs comment along with images in the screenshots folder. Also send a PR with the updated sequence classes so I can review and merge it for everyone.

## Requirements
1. Python 3.6+

### If you want to save the image, you will need to install Pillow and setup the path in the code
1. Install Pillow using pip
```bash
pip install pillow
```
2. Install Ghostscript from [here](https://www.ghostscript.com/download/gsdnld.html)
2. Setup the path in the code if you have a custom installation and not added to system path
```python
EpsImagePlugin.gs_windows_binary =  r'[Enter the path to exe]'
```

## How to run the code
1. Clone the repo
2. Set your configuration options if any or run as it is
3. Run the pattern.py file
```bash
python pattern.py
```