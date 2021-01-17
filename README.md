# Comment Header Creator
Create a "header" for separating/describing sections of your Python code.

I don't know about you but I like to "organize" my Python methods and functions by putting some sort of comment 
seperator between them.  This helps me when scrolling through my code to find particular categories of routines.

There are basically 2 main methods:  Basic or Fancy
 - Basic (the uniline() method) returns a formatted string that is a single line with the 'title' centered.
 - Fancy (the multiline() method) returns a formatted string that is 3 lines long with the 'title' centered in the 
   center line.

> There is a "hidden" function, _generate_line(), is the secret sauce to generating the lines.  You can call this 
> directly but bear in mind it returns a Tuple (string and a boolean).

## Example Uses
See example.py for how to use or:
  - Create a single-line header but input title from user input:
```python
import comment_header_creator as chc
print(chc.uniline())
```
  yields:
```bash
Enter Title: title of section
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- TITLE OF SECTION -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
```

  - Create a multi-line header but input title from user input:
```python
import comment_header_creator as chc
print(chc.multiline())
```
  yields:
```bash
Enter Title: Another Section
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- ANOTHER SECTION -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
```

  - Create a single-line (or multi-line) header by passing title in function call:
```python
import comment_header_creator as chc
print(chc.uniline(title='Greatest Hits'))
```
  yields:
```bash
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- GREATEST HITS -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- #
```

  - You can also set your own 'expander' string:
```
import comment_header_creator as chc
chc.uniline(title="it's a flesh wound", expander='0i')
"# i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i IT'S A FLESH WOUND i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i0i #"
```
> NOTE:  In the previous example notice that we didn't use the print() function.  This will return a string, which you 
> then need to "strip" the quotes off the front and end.  Thus, I suggest print()'ing your outputs.
