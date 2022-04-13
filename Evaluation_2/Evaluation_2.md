## Evaluation 2

Your neice is learning about Ecology in school. She is a bright girl and you always look for every opportunity you can to try to pique her interest in computer science and python. Make her a similuation of a forest that has grass, rabbits and foxes. The rabbits eat the grass and the foxes eat the rabbits. The forest occurs in an 40x40 matrix where each bare square may generate grass with a 20% chance for every 5 ticks of the game clock. Rabbits and foxes move randomly in the forest. If a hungry Rabbit finds grass, it eats it, leaving a barren square and it is well-fed (ie. not hungry) for 10 ticks of the clock afterwards. If two rabbits or two foxes occupy the same square they will breed and produce a new instance of their kind. If a hungry Fox finds a Rabbit, it eats it, and it is well-fed for 12 ticks of the clock after. A Rabbit that his hungry for 10 ticks of the game clock dies and a Fox that is hungry for 12 ticks of the game clock will also perish. 

This is a console game. For each tick of the game clock, print a matrix in console with symbols to represent rabbits, grass and foxes. Also print a count of how much grass, how many rabbits and how many foxes there are. Each tick should last 3 seconds (so we can appreciate each scene) and there should be 60 ticks.


