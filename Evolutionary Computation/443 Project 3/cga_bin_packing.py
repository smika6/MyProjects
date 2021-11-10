# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:34:45 2020

BIN-PACKING:
    Given a set of B bins, each with capacity b, 
    and a set of n packages, each with positive size si in [1,b/2], 
    assign packages to the minimum number of bins 
    without allowing the total size of the packages in any bin to exceed b.

GA Structure:
      initialize the population with random chromosomes;
      evaluate all the chromosomes;

      repeat
      {
        for i from 1 to the population size
        {
          decide whether to use crossover or mutation;
          if crossover
            select two parents;
            cross them to produce an offspring;
          else
            select one parent;
            mutate it to produce an offspring;
          evaluate the offspring;
          record the offspring in the next generation;
        }
        offspring replace parents;

      } until enough generations have passed;

      report the solution the best chromosome represents;
    
@author: smika
"""


import random
import collections
import matplotlib.pyplot as plt

#named tuple for pretty display
Package = collections.namedtuple("Package","id size")

#create the packages
def create_randomly_sized_packages(packages, packages_amount, si):
    p_id = 0
    while (len(packages) < packages_amount):
        random_size = random.randint(si[0],si[1])
        package = Package(p_id, random_size)
        if package not in packages:
            packages.append(package)
            p_id += 1

#function for creating a random permutation of the packages
#chromosomes are these permutations the length of packages_amount
def new_permutation(pckgs):
    ps = pckgs.copy()
    perm = []
    
    for _ in range(len(pckgs)):
        p = random.choice(ps)
        perm.append(p)
        ps.remove(p)
    
    return perm

def fill(some_bin):
    fill = 0
    for p in some_bin: #for each package
        fill += p[1] # grab the size of the package
    return fill # return the sum

def bin_packages(packages, bin_capacity, show = False):
    b = []
    
    for package in packages:
        if len(b) == 0 or fill(b[-1]) + package[1] > bin_capacity:
            b.append([package])
        else:
            b[-1].append(package)
    
    if show:
        print("bin count: ", len(b))
        for bins in b:
            print("fill: " + str(fill(bins)) + "/" + str(bin_capacity), bins)
        print()
    
    return b

def evaluate_fitness(candidate, bin_cap):
    
    #fill bins
    bns = bin_packages(candidate,bin_cap)
    k = 1
    
    fit = 0
    
    for b in bns:
        fit += (fill(b) / bin_cap)**k
    
    
    return fit/len(bns)
        

def best_in_population(pop):
    best_fit = float("-inf")
    best = []
    for p in pop:
        if p[1] > best_fit:
            best_fit = p[1]
            best = p
    return best


def order_1_cross_over(parent1, parent2):
    
    child = [Package(0,0) for _ in range(len(parent1))]
    
    # Copy randomly selected set from first parent
    
    random_crossover_start_point = random.randint(0, len(parent1)) #random start index
    
    random_crossover_end_point = random.randint(0, len(parent1))   #random stop index
    
    if random_crossover_start_point > random_crossover_end_point:  #reversing them if start is greater
        random_crossover_start_point, random_crossover_end_point = random_crossover_end_point, random_crossover_start_point #tuple unpacking

    for i in range(random_crossover_start_point, random_crossover_end_point):    
        child[i] = parent1[i]
    
    # Copy rest from second parent in order
    
    unused = [] 
    
    #loop for length of parent2
    for a in range(len(parent2)):
        
        #index is the end point of currently copied chromosome + the next interation
        index = random_crossover_end_point + a
        
        #if index reaches the end of the chromosome make it wrap around
        if index >= len(child):
            index -= len(child)
        
        #check if it is in the child or not and if not save it
        if parent2[index] not in child:
            unused.append(parent2[index])
        
    #the stop minus the start is the length of the range
    size_of_copied_set = random_crossover_end_point - random_crossover_start_point
    
    #the size of the chromosome minus whats already placed
    ammount_of_items_left = len(child) - size_of_copied_set
    
    #loop the ammount of items unplaced
    for b in range(ammount_of_items_left):
        
        #index is the end point of currently copied chromosome + the next interation
        index = random_crossover_end_point + b
        
        #if index reaches the end of the chromosome make it wrap around
        if index >= len(child):
            index -= len(child)
        
        #child at the index unplaced is assigned the next value in the list of unused ones
        child[index] = unused[b]
    
    #return the rebuilt child
    return child

def fitness_sorter(e):
  return e[1]

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def bin_count_compare(x,y):
    return x[2] - y[2]

def bin_count_sort(mp, bin_capacity):
    modded_mp = []
    
    for c in mp:
        bc = bin_packages(c[0], bin_capacity)
        modded_mp.append((c[0],c[1],len(bc)))
    
    sorted(modded_mp, key=cmp_to_key(bin_count_compare))
    
    return [(c[0],c[1]) for c in modded_mp]
    
    

def selection(pop, new_gen, packages_amount, bin_capacity):
    elite_count = round(len(pop)/4)
    
    pop_sort = pop.copy()
    
    new_gen_sort = new_gen.copy()
    
    new_pop = []
    
    mating_pool = pop_sort + new_gen_sort
    
    mating_pool.sort(key=fitness_sorter)
        
    for c in mating_pool:
        if c not in new_pop:
            new_pop.append(c)
    
    new_pop = new_pop[-(packages_amount-elite_count):]
    
    mating_pool = bin_count_sort(mating_pool, bin_capacity)
    
    elites = mating_pool[-elite_count:]
    
    for e in elites:
        new_pop.append(e)
    
    return new_pop
        

def genetic_bin_packing(packages, bin_capacity, packages_amount, plot = True):
    if plot:
        best_candidate_solutions = []
        gen_change = []
    
    #population of chromosomes
    population = []
    
    #size of the population
    population_size = 20
    
    #fill the population of chromosomes randomly initially and evaluate their initial fitness
    for p in range(population_size):
        new_p = new_permutation(packages)
        fit = evaluate_fitness(new_p, bin_capacity)
        population.append((new_p, fit))   #-1 for the unkown fitness (Package, fitness)
        #plt.title('Bin Count Across Generations for All Tests')
    
    #keep track of the current best candidate solutions
    best_candidate_solution = best_in_population(population)

    #print(best_candidate_solution)
    
    #variable to count how many times the best in the population has not canged
    unchanged = 0
    
    #the cutoff for when unchanged should stop
    CUTOFF = 2
    
    #mutation rate of genetic algorithm (x/100)
    mutation_rate = 10
    
    #counter of the generation
    generation_count = 0
    
    while True:                
        generation_count += 1
        
        if plot:
            bns = bin_packages(best_candidate_solution[0], bin_capacity)
            best_candidate_solutions.append(len(bns))
            gen_change.append(generation_count)
        
        new_generation = []
        
        for candidate in population:
            
            #print(candidate)
            #print()
            
            mutation_chance = random.randint(1,100)
            
            if mutation_chance <= mutation_rate:
                
                old_mutation_location = random.randint(1,len(candidate[0])-1)
                new_mutation_location = random.randint(1,len(candidate[0])-1)
                pckgs = candidate[0]
                
                tmp = pckgs[old_mutation_location]
                pckgs[old_mutation_location] = pckgs[new_mutation_location]
                pckgs[new_mutation_location] = tmp
                
                new_generation.append((pckgs, evaluate_fitness(pckgs, bin_capacity)))
            
            else:
                #crossover
                
                partner = random.choice(population)
                
                child_pckgs = order_1_cross_over(candidate[0], partner[0])
                
                new_generation.append((child_pckgs, evaluate_fitness(child_pckgs, bin_capacity)))

        new_gen_best_in_population = best_in_population(new_generation)

        if new_gen_best_in_population[1] > best_candidate_solution[1]:
            best_candidate_solution = new_gen_best_in_population
            unchanged = 0
        else:
            unchanged += 1
        
        if unchanged >= CUTOFF:
            #print(best_candidate_solution)
            if plot:
                plt.plot(gen_change, best_candidate_solutions)
                plt.ylabel('bin count')
                plt.xlabel('generation count')
            return best_candidate_solution
        
        population = selection(population, new_generation, packages_amount, bin_capacity)
        
        #print('Gen: ' + str(generation_count), ', mutation rate:' + str(mutation_rate), ',unchanged: ' + str(unchanged), "best fit:" + str(best_candidate_solution[1]))

def printbins(bins, bin_capacity):
    
    print("bin count", len(bins))
    for b in bins:
        print("fill: " + str(fill(b)) + "/" + str(bin_capacity), b)
    print()
        
def firstfit(packages, bin_capacity):
    
    bins = [[]]
    
    for p in packages:
        for b in bins:
            fill_with_package = fill(b) + p[1]
            if fill_with_package <= bin_capacity:
                b.append(p)
                break
        else:
            bins.append([p])
    
    return bins
    
def nextfit(packages, bin_capacity):

    o = 0
    bins = [[]]
    
    for p in packages:
        placed = False
        while not placed:
            open_bin = bins[o]
            
            if fill(open_bin) + p[1] <= bin_capacity:
                open_bin.append(p)
                placed = True
            elif o < len(bins) - 1:
                o += 1
            else:
                bins.append([p])
                placed = True
    
    return bins

def bestfit(packages, bin_capacity):
    
    bins = []
    
    for p in packages:
        bestfit_bin = []
        min_delta = float('inf')
        for b in bins:
            fill_with_package = (fill(b) + p[1])
            if  fill_with_package <= bin_capacity:
                space_left = bin_capacity - fill_with_package
                if space_left < min_delta:
                    min_delta = space_left
                    bestfit_bin = b
        
        if bestfit_bin == []:
            bins.append([p])
        else:
            bestfit_bin.append(p)
        
    return bins

def worstfit(packages, bin_capacity):
    bins = []
    
    for p in packages:
        bestfit_bin = []
        max_delta = float('-inf')
        for b in bins:
            fill_with_package = (fill(b) + p[1])
            if  fill_with_package <= bin_capacity:
                space_left = bin_capacity - fill_with_package
                if space_left > max_delta:
                    max_delta = space_left
                    bestfit_bin = b
        
        if bestfit_bin == []:
            bins.append([p])
        else:
            bestfit_bin.append(p)

    return bins

def main(b, p):
    import time
    
    #capacity of bins
    bin_capacity = b #50 #int(input("Input bin capacity: "))
    
    #set of packages
    packages = []
    
    #count of packages
    packages_amount = p #100 #int(input("Input count of packages: "))
    
    #package size limit si
    si = (1,int(bin_capacity/2))
    
    create_randomly_sized_packages(packages, packages_amount, si)
    
    #print("\n\nGA")
    
    ga_t1 = time.time()
    ga_solution = genetic_bin_packing(packages, bin_capacity, packages_amount, si)
    ga_t2 = time.time()
    
    bn = bin_packages(ga_solution[0], bin_capacity, False)
    #print("bin count: " + str(len(bn)), '\ncompute time: ' + str(ga_t2 - ga_t1))
    
    
    #print("\nFF")
    
    ff_t1 = time.time()
    ff_solution = firstfit(packages, bin_capacity)
    ff_t2 = time.time()
    
    #print("bin count: " + str(len(ff_solution)), '\ncompute time: ' + str(ff_t2 - ff_t1))
    
    
    #printbins(ff_solution, bin_capacity)
    
    #print("\nBF")
    
    bf_t1 = time.time()
    bf_solution = bestfit(packages, bin_capacity)
    bf_t2 = time.time()
    
    #print("bin count: " + str(len(bf_solution)), '\ncompute time: ' + str(bf_t2 - bf_t1))
    #printbins(bf_solution, bin_capacity)
    
    #print("\nWF")
    
    wf_t1 = time.time()
    wf_solution = worstfit(packages, bin_capacity)
    wf_t2 = time.time()
    #print("bin count: " + str(len(wf_solution)), '\ncompute time: ' + str(wf_t2 - wf_t1))
    #printbins(wf_solution, bin_capacity)
    
    #print("\nNF")
    
    nf_t1 = time.time()
    
    nf_solution = nextfit(packages, bin_capacity)
    
    nf_t2 = time.time()
    #print("bin count: " + str(len(nf_solution)), '\ncompute time: ' + str(nf_t2 - nf_t1))
    #printbins(nf_solution, bin_capacity)
    
    return [('GA', len(bn), ga_t2 - ga_t1),
            ('FF', len(ff_solution), ff_t2 - ff_t1),
            ('BF', len(bf_solution), bf_t2 - bf_t1),
            ('WF', len(wf_solution), wf_t2 - wf_t1),
            ('NF', len(nf_solution), nf_t2 - nf_t1)]

if __name__ == "__main__":
    test_count = 25
    bin_caps = [20,20,50,50]
    pack_cnts = [50,100,50,100]
    solutions = []
    for t in range(len(bin_caps)):
        #print('\n\nINPUTS: bin_capacity:',  bin_caps[t], '| package_count:', pack_cnts[t])
        for r in range(test_count):
            #print('RUN', r)
            results = main(bin_caps[t], pack_cnts[t])
            solutions.append(((bin_caps[t], pack_cnts[t]), results))
        plt.title('Bin Count Across Generations for Test Inputs: bc:' + str(bin_caps[t]) + ' pc:' + str(pack_cnts[t]))
        plt.show()
    #wait = input('\n\nEnter to close...')
    
    input_config = solutions[0][0]
    cnt = 0
    ga_avg, ff_avg, bf_avg, wf_avg, nf_avg = 0, 0, 0, 0, 0
    ga_avg_b, ff_avg_b, bf_avg_b, wf_avg_b, nf_avg_b = 0, 0, 0, 0, 0
    titles = ['GA', 'FF', 'BF', 'WF', 'NF']
    ga_values = []
    ff_values = []
    bf_values = []
    wf_values = []
    nf_values = []
    for s in solutions:  
        if s[0] != input_config:
            input_config = s[0]
            print("Average Time(GA): ", ga_avg/cnt)
            print("Average Bin Count(GA): ", ga_avg_b/cnt)
            print("\nAverage Time(FF): ", ff_avg/cnt)
            print("Average Bin Count(FF): ", ff_avg_b/cnt)
            print("\nAverage Time(BF): ", bf_avg/cnt)
            print("Average Bin Count(BF): ", bf_avg_b/cnt)
            print("\nAverage Time(WF): ", wf_avg/cnt)
            print("Average Bin Count(WF): ", wf_avg_b/cnt)
            print("\nAverage Time(NF): ", nf_avg/cnt)
            print("Average Bin Count(NF): ", nf_avg_b/cnt)
            ga_avg, ff_avg, bf_avg, wf_avg, nf_avg, cnt = 0, 0, 0, 0, 0, 0
            ga_avg_b, ff_avg_b, bf_avg_b, wf_avg_b, nf_avg_b = 0, 0, 0, 0, 0
            print()
        ga_values.append(s[1][0][1])
        ff_values.append(s[1][1][1])
        bf_values.append(s[1][2][1])
        wf_values.append(s[1][3][1])
        nf_values.append(s[1][4][1])
        ga_avg += s[1][0][2]
        ga_avg_b += s[1][0][1]
        ff_avg += s[1][1][2]
        ff_avg_b += s[1][1][1]
        bf_avg += s[1][3][2]
        bf_avg_b += s[1][3][1]
        wf_avg += s[1][4][2]
        wf_avg_b += s[1][4][1]
        nf_avg += s[1][4][2]
        nf_avg_b += s[1][4][1]
        cnt += 1
        print(s)
    print("Average Time(GA): ", ga_avg/cnt)
    print("Average Bin Count(GA): ", ga_avg_b/cnt)
    print("\nAverage Time(FF): ", ff_avg/cnt)
    print("Average Bin Count(FF): ", ff_avg_b/cnt)
    print("\nAverage Time(BF): ", bf_avg/cnt)
    print("Average Bin Count(BF): ", bf_avg_b/cnt)
    print("\nAverage Time(WF): ", wf_avg/cnt)
    print("Average Bin Count(WF): ", wf_avg_b/cnt)
    print("\nAverage Time(NF): ", nf_avg/cnt)
    print("Average Bin Count(NF): ", nf_avg_b/cnt)
    
    x = list(zip(ga_values, ff_values, bf_values, wf_values, nf_values))
    import pandas as pd
    
    for t in range(len(bin_caps)):
        table = pd.DataFrame(data = x[(t*test_count):((t+1)*test_count)], columns = titles)
        print(table)
        print()







