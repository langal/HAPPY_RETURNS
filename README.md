# HAPPY_RETURNS

NOT Very happy with my code here.

If I had more time, I would obviously utilize separate files for test, "Sort", and business objects like Card.

I would also like to abstract the Sort so it wasn't so tightly bound to direct fields like "origin", "destination", etc.

In a real world, I would create some sort of Interface that would define some methods like "origin" and "destination" so the sorter could handle anything that defined those methods.

I sort of cheated to since I rushed and put references to "next" and "previous" directly into the "Card" class.  If given more time, I would obviously create some sort of "Node" class that would contain a reference to the business entity ("Card").


TO RUN:

"python Card.py"

There is output that I have commented out.   The program basically runs several iterations of sorting a random set of cards.
