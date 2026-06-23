# ZipZagoon Pickup ![alt text](image-1.png)
---

The actual idea came from playing a emerald ROM hack that bugged out and my zigzagoon was picking up **way** too many items and it caused a whole bunch of crashing issues. Pair that with some excel certification testing and you get a mini porject like this. Can't imagine anyone using it, and it's definetly been done better by someone else 10 years ago, but I think it's fun so moot point.

Look at this little guy! Crashing and Making a ROM save unplayable after 65 hours in! : <img src="image-3.png" height="50" width='50px'>

## Description:
---
A python program that calls to the [PokeApi](https://pokeapi.co/) RESTFul service and pulls down the lists of items and splits them going off the "Pockets" they'd occupy inside a pokemon game. The items are then written to an excel workbook with each sheet being the "Pocket" that the item belongs to.

I.E Masterball, Quick Ball, and Pokeball go to the "Balls" worksheet. Potions, Parlyz Heal, and etc. go to the potions/medicine pocket

The original prototype version simply pulled and listed the 64 Berries that exist along with their costs and pictures into an excel sheet and then split out to inspire a website which if you want the code for that it'll be [Here](https://youtu.be/omguEZ7jy5E?si=onDrf30DbVDxaKml&t=6)

## Plans
- [x] Output the results of at least the berries 

## Current Version(s)
---
0.1: MVP I guess program runs and outputs the Berries currently loaded into the API all 64 with their names, 