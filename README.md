# Comment Header Creator
Create a "header" for separating/describing sections of your Python code.

I don't know about you but I like to "organize" my Python methods and functions by putting some sort of comment 
seperator between them.  This helps me when scrolling through my code to find particular categories of routines.

There are basically 2 main methods:  Basic or Fancy
 - Basic (the uniline() method) returns a formatted string that is a single line with the 'title' centered.
 - Fancy (the multiline() method) returns a formatted string that is 3 lines long with the 'title' centered in the 
   center line.

The last "hidden" function, _generate_line(), is the secret sauce to generating the lines.  You can call this 
directly but bear in mind it returns a Tuple (string and a boolean).

See example.py for how to use.