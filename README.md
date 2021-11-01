## ASCII art Maker
 
A program which accepts an input for a path of photo and prints its ASCII art equivalent on the console and also saves that art in a text file.

### How does it work?

This repository includes a python program, which takes a normal photo and transforms it in to ASCII art. This works by first resizing the photo and then graifying it to accurately determine the 'brightness' of each pixel. 
> Note: The photo is grayified to accurately determine the brightness of each pixel

Afterwards, a function takes the graifyed and adjusted picture and makes a list of ASCII character for every pixel in that photo, where the character added depends on the brightness of that pixel. 

> Bigger characters like a # or % are used for darker pixels and smaller ones like . for brighter ones.

This list is then formatted into a printable format by adding some break lines and its contents are printed and also saved into a text file.

### Who created this?
I am NOT the creator of this program. This program was programmed as part of a tutorial by the youtube channel kite. The link can be found [here](https://www.youtube.com/watch?v=v_raWlX7tZY).

### About the creator
![This is an image](http://images3.memedroid.com/images/UPLOADED275/5eb2c43f97efa.jpeg)

