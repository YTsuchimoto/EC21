Eric Vernon, Student #2200104065

I found the  [example one-max notebook](https://github.com/DEAP/notebooks/blob/master/OneMax.ipynb) from the official DEAP repository to be very useful in learning about DEAP.

I decided to make a variant of the one-max problem.  In this problem,

- Each gene is represented by an integer (instead of just a bit)
- In the mutation stage, each gene has a chance to increase by 1, or decrease by 1
- The fitness is the sum of the genes
- Example: The individual `[0, -1, 5, 0]` has fitness 4.

I set a population size of 20.  A binary tournament is used for selection,
two point crossover for mating, and the mutation operator described above.  Individuals have 10 genes, and each gene is
randomly generated from the set (-1, 0, 1).

The results are copied below.  We can see that in general the fitness values increase over time, however the fitness
occasionally decreases between generations.

The best individual found had a fitness value of 21.  (The maximum fitness value, of course, is infinity!)

```
gen	nevals	avg 	min	max
0  	20    	0.35	-6 	6  
1  	13    	1.6 	-3 	6  
2  	11    	3.45	0  	6  
3  	20    	3.7 	0  	6  
4  	12    	5.1 	3  	6  
5  	15    	5.65	4  	8  
6  	13    	6.3 	1  	8  
7  	15    	6.8 	4  	11 
8  	15    	7.55	5  	10 
9  	6     	8.5 	6  	10 
10 	15    	9.4 	7  	11 
11 	12    	10.1	9  	13 
12 	7     	10.6	8  	13 
13 	13    	11.45	9  	15 
14 	16    	12.2 	10 	15 
15 	10    	12.75	11 	15 
16 	12    	13.35	11 	18 
17 	10    	14.4 	11 	18 
18 	7     	15.1 	11 	19 
19 	15    	16.1 	13 	19 
20 	13    	17.4 	13 	21 
Best: [2, 4, 0, 2, 2, 3, 0, 3, 2, 3]
```
