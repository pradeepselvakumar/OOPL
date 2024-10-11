### HW 4 Requirements

This folder (Book) contains the chapters outlining the contents of a Python book, stored as HTML files. There are also some addtional folders for HTML assets like javascript, CSS, and images.

When the HTML files were originally created, a few mistakes crept in, and now all the files need to be updated in certain ways:

1. Replace colors as laid out in the table below.  

| Old Color | New Color |
| :-------: | :-------: | 
| #007bff   |  #070707  | 
| #e7f3fe   |  #e3fafc  | 
| #0b5294   |  #087f8c  | 
| #e8f5e9   |  #d1f7d7  | 
| #33691e   |  #0a582f  | 

2. Every chapter has an `<img>` tag at the bottom with `alt="Python Logo"`. The `href` value of that tag needs to be set to `images\Python-logo-notext.png` in all files.

1. The `index.html` file has a `<nav>` section that displays the Table of Contents. That entire node needs to be added to every chapter file, right before the `<main id="content">` node. This will add a Table of Contents to every chapter.


### Instructions 
1. Clone this repository so the Book folder is available on your computer locally.  

1. In your homework repository, create a `HW4 - Converter` folder. Create a script named `converter.py` within that folder that accepts a path to a folder.

1. This script will look for all HTML files within all subfolders of the specified folder. For each HTML file, the above changes will be applied.

1. The entire contents of the `Book` folder, including the modified files, should be saved to an output folder of the format `Output_YYYYMMDD_HHmmSS` where `YYYYMMDD_HHmmSS` represents the date and time when the script was run.
