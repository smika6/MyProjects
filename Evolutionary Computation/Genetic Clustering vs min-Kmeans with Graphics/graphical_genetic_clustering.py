# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:09:37 2020

picture: https://pixabay.com/vectors/dna-icon-gene-helix-double-helix-2316641/

MINIMUM k-CLUSTERING: 
    Given a set X and distances d(x,y) for each pair x, y in X that satisfy the triangle inequality,
    partition X into k disjoint subsets C1, C2, ... , Ck so as to minimize the maximum distance between any two elements of the same subset.
    Note that the elements of X may be points in the plane and the distances the Euclidean distances between the points. 


REFERENCES:
    ALGORITHM
    https://web.stcloudstate.edu/bajulstrom/cs443/projects/p2.html
    https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/
    https://stanford.edu/~cpiech/cs221/handouts/kmeans.html
    https://en.wikipedia.org/wiki/K-means_clustering
    https://www.researchgate.net/publication/220571471_A_genetic_algorithm_for_cluster_analysis
    https://support.minitab.com/en-us/minitab/18/help-and-how-to/modeling-statistics/multivariate/how-to/cluster-k-means/interpret-the-results/all-statistics-and-graphs/
    https://stackoverflow.com/questions/6645895/calculating-the-percentage-of-variance-measure-for-k-means
    https://www.youtube.com/watch?v=4b5d3muPQmA
    https://en.wikipedia.org/wiki/Silhouette_(clustering)
    https://stackoverflow.com/questions/19197715/scikit-learn-k-means-elbow-criterion
    https://stackoverflow.com/questions/6645895/calculating-the-percentage-of-variance-measure-for-k-means
    https://en.wikipedia.org/wiki/Elbow_method_(clustering)
    https://en.wikipedia.org/wiki/Determining_the_number_of_clusters_in_a_data_set
    https://reader.elsevier.com/reader/sd/pii/S0898122199000905?token=B49BABBFB5B03FD4988F91B300A89450BEC13650983C2D77C81CFFA75E0834744C1D8C375FECF6FFCB5AFC196E821417
    https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
    https://towardsdatascience.com/k-means-clustering-algorithm-applications-evaluation-methods-and-drawbacks-aa03e644b48a
    https://www.youtube.com/watch?v=aOnKnLM4eok
    https://www.geeksforgeeks.org/genetic-algorithms/
    
    
    GRAPHICS
    https://www.pygame.org/docs/ref/key.html
    https://pygame.readthedocs.io/en/latest/4_text/text.html
    https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
    
    
@author: Jacob Hopkins
"""

import pygame
import sys
import os
import time
from datetime import datetime
import colors

#variables 
WIDTH = 600
HEIGHT = 600
HUD_WIDTH = 400
INFO_BAR_WIDTH = 200
GAP = 50
HALF_GAP = GAP/2
X_RANGE = (-60,60)
Y_RANGE = (-60,60)

display_interval = 20

button_width, button_height = 120, 75

user_input = '4'

k_accepted = False
k = 4

CUTOFF = 10

solved = False

ORIGIN = (WIDTH/2 + HALF_GAP, HEIGHT/2 + HALF_GAP)

gray_color = (51,51,51)
med_gray_color = (101,101,101)
light_gray_color = (151,151,151)
bright_gray_color = (251,251,251)
white_color = (255,255,255)
black_color = (0,0,0)
red_color = (255,0,0)

button_labels = ["K-MEANS", "M K-MEANS", "GENETIC", "UNIFORM", "RANDOM", "DATA SET", "SAVE PTS"]

color_dict = colors.get_color_dictionary()

selectable = [True for s in button_labels]

color_rgb_arr = list(color_dict.values())

POINT_COUNT = X_RANGE[1]**2 * 0.1

POINTS = []

CLUSTER_COLORS = []
CLUSTER_CENTERS = []

POPULATION = []

MATING_POOL = []

ANSWERS = []
    
labels = []
unlabeled = True
delay = 0

#make the function update and wait
step_tru = False

circles = False
moons = True

solution = []

def main():
    global selectable, solved, delay, solution
    #SETUP PYGAME
    pygame.init()
    pygame.font.init()
    
    #set the size of the window
    game_window_size = (WIDTH + HUD_WIDTH + INFO_BAR_WIDTH,HEIGHT + GAP)
    game_window = pygame.display.set_mode(game_window_size)
    
    #LOAD IMAGE AND TITLE FOR WINDOW
    logo = pygame.image.load("dna.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Genetic Minimum k-Clustering")
    
    background = pygame.Surface(game_window.get_size())
    background = background.convert()
    background.fill(gray_color)
    
    game_window.blit(background, (0, 0))
    pygame.display.flip()
    
    run = True
    
    generate_points_randomly(POINT_COUNT, POINTS, white_color)
    
    font = pygame.font.Font(None, 16)
    
    labels_text = font.render("Labels:", 1, light_gray_color)
    labels.append(labels_text)
    
    unassigned_text = font.render("UNASSIGNED", 1, white_color)
    labels.append(unassigned_text)
     
    # game loop
    while run:
        pygame.time.delay(delay)
        
        for event in pygame.event.get():
            controls(event)
            
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit(0)
            
        
        #loop start
        
        draw_graph(game_window, white_color)
        display_points(game_window, POINTS)
        draw_hud(game_window)
        solution = ''
        
        if k_accepted and not unlabeled and not solved:
            if selectable[0] and not selectable[1] and not selectable[2]:
                solution = k_means(k, game_window)
                solved = True
                #print(solution)
            if selectable[1] and not selectable[0] and not selectable[2]:
                solution = min_k_means(game_window)
                solved = True
                #print(solution)
            if selectable[2] and not selectable[0] and not selectable[1]:
                solution = cga(k, game_window)
                solved = True
                #print(solution)
        
        pygame.display.update()
        pygame.display.flip()
        
def min_k_means(game_window):
    global POINTS, CUTOFF, CLUSTER_COLORS, k, unlabeled, CLUSTER_CENTERS, ANSWERS
    
    from sklearn.metrics import silhouette_score
    from sklearn.cluster import KMeans
    import time
    import matplotlib.pyplot as plt
    
    ss = []
    
    t1 = time.perf_counter()
    
    X = [ [x,-y] for x,y,c in POINTS ]
    
    min_k_labels = []
    min_k_clusters = []
    max_k_silhouette = float('-inf')
    min_k = float('inf')
       
    for n_cluster in range(2, CUTOFF):
        kmeans = KMeans(n_clusters=n_cluster).fit(X)
        label = kmeans.labels_
        clusters = kmeans.cluster_centers_
        sil_coeff = silhouette_score(X, label, metric='euclidean')
        ss.append(sil_coeff)
        #print("For n_clusters={}, The Silhouette Coefficient is {}".format(n_cluster, sil_coeff))
        if max_k_silhouette < sil_coeff:
            max_k_silhouette = sil_coeff
            min_k_clusters = clusters
            min_k_labels = label
            min_k = n_cluster
        
        if max_k_silhouette/sil_coeff < 0.1:
            max_k_silhouette = sil_coeff
            min_k_clusters = clusters
            min_k_labels = label
            min_k = n_cluster
    
    #print(min_k_clusters)
    #print(min_k_labels)
    #print(X)
    
    t2 = time.perf_counter()
    
    k = min_k
    CLUSTER_COLORS = []
    unlabeled = True
    draw_hud(game_window)
    
    #print(POINTS)
    POINTS = [ (p[0], -p[1], CLUSTER_COLORS[c] ) for p, c in zip(X, min_k_labels) ]
    #print(POINTS)
    CLUSTER_CENTERS = [ (p[0], -p[1], CLUSTER_COLORS[i]) for p, i in zip(min_k_clusters, range(len(min_k_clusters))) ]
    
    min_k_labels.sort()
    
    right = 0
    for a, b in zip(min_k_labels, ANSWERS):
        if a == b:
            right+=1
    
    if len(ANSWERS) > 0:
        success_rate = right/len(ANSWERS) * 100.0
    else:
        success_rate = ""
        
    #print()
    button_labels.append("RESET")
    selectable.append(True)
    
    print(f"\nTime to compute min K Means: {t2 - t1:0.4f} seconds" )
    
    print(f"Success Rate of min K Means: {success_rate} %" )
    
    fig = plt.figure(figsize=(14,7))
    fig.add_subplot(122)
    plt.plot(range(2,CUTOFF), ss,'b-',label='Silhouette Score')
    plt.xlabel("Number of cluster")
    plt.ylabel("Silhouette Score")
    plt.legend()
    plt.show()
    
    return (CLUSTER_CENTERS, POINTS)    
    
def k_means(k, game_window):
    #https://www.youtube.com/watch?v=4b5d3muPQmA
    
    global CLUSTER_CENTERS, POINTS, delay, step_tru
    #print("Solving with K Means: " + str(k))     
    
    # assign cluster centers randomly    
    
    import random
    import time
    import matplotlib.pyplot as plt
    
    t1 = time.perf_counter()
    attempt_count, attempt_limit = 0, 17

    kmeans_cluster_attempts = []
    
    ss = []
    
    while(attempt_count < attempt_limit):
        CLUSTER_CENTERS = []
            
        first = True
        prev_centers = []    
        
        attempted_clusters = []
        
        while(True):
        
            if first:
                cluster_c = 0
                while( len(CLUSTER_CENTERS) < k):
                    random_p = random.choice(POINTS)
                    random_center = (random_p[0], random_p[1], CLUSTER_COLORS[cluster_c])
                    if random_center not in CLUSTER_CENTERS:
                        CLUSTER_CENTERS.append(random_center)
                        cluster_c+=1
                
                CLUSTER_CENTERS.sort()
                
                #print(CLUSTER_CENTERS)
                
                first = False
            
            #print(prev_centers)
            
            if (prev_centers == CLUSTER_CENTERS):
                break
            
            reasigned_points = []
            
            for p in POINTS:
                closest_cluster = ( float('inf') , float('inf'), white_color )
                dst_to_closest_c = float('inf') 
                for c in CLUSTER_CENTERS:
                    if distance(p,c) < dst_to_closest_c:
                            dst_to_closest_c = distance(p,c)
                            closest_cluster = c
                reasigned_points.append( (p[0], p[1], closest_cluster[2]) )
            
            POINTS = reasigned_points
            
            new_cluster_centers = []
            
            for c in CLUSTER_CENTERS:
                mean_x, mean_y, count = 0, 0, 0
                for p in POINTS:
                    if c[2] == p[2]:
                        mean_x += p[0]
                        mean_y += p[1]
                        count+=1
                if count > 0:        
                    new_cluster_centers.append( ( (mean_x/count), (mean_y/count), c[2] ) )
            
            new_cluster_centers.sort()
            prev_centers = CLUSTER_CENTERS
            CLUSTER_CENTERS = new_cluster_centers
            
            if step_tru:
                pygame.time.delay(round(delay/4))
                draw_graph(game_window, white_color)
                display_points(game_window, POINTS)
                draw_hud(game_window)
                pygame.display.update()
        
        if len(CLUSTER_CENTERS) == k:
            for c in CLUSTER_CENTERS:
                attempted_clusters.append(  ( c,  avg_dist_from_centroid(c, POINTS) ) )
        
        if len(attempted_clusters) > 0:
            avg_avg_dst = 0
            for a in attempted_clusters:
                avg_avg_dst += a[1]
            avg_avg_dst = avg_avg_dst/len(attempted_clusters)
            
            avg_dst_from_avg_avg_dst = 0
            for a in attempted_clusters:
                avg_dst_from_avg_avg_dst += abs(a[1] - avg_avg_dst)
            avg_dst_from_avg_avg_dst = avg_dst_from_avg_avg_dst/len(attempted_clusters)
            
            kmeans_cluster_attempts.append( [ attempted_clusters, avg_dst_from_avg_avg_dst, POINTS] )
            
            attempt_count += 1
    
    min_dist = float("inf")
    best_clusters = []
    for k in kmeans_cluster_attempts:
        ss.append(k[1])
        if k[1] < min_dist:
            min_dist = k[1]
            best_clusters = k
        #print(k)
        #print()
    
    t2 = time.perf_counter()
        
    POINTS = best_clusters[2]
    
    CLUSTER_CENTERS = [a for a, b in best_clusters[0]]
    
    button_labels.append("RESET")
    selectable.append(True)
    
    l = []
    for p in POINTS:
        for i, c in enumerate(CLUSTER_CENTERS):
            if p[2] == c[2]:
                l.append(i)
    
    l.sort()
    
    right = 0
    for a, b in zip(l, ANSWERS):
        if a == b:
            right+=1
    
    if len(ANSWERS) > 0:
        success_rate = right/len(ANSWERS) * 100.0
    else:
        success_rate = ''
    
    print(f"\nTime to compute K Means: {t2 - t1:0.4f} seconds" )
    
    print(f"Success Rate of K Means: {success_rate} %" )
    
    fig = plt.figure(figsize=(14,7))
    fig.add_subplot(122)
    plt.plot(range(0,attempt_limit), ss,'b-',label='K Means Attempt Performance')
    plt.xlabel("Cluster Attempt")
    plt.ylabel("Average Delta from Mean Cluster Size")
    plt.legend()
    plt.show()
    
    return (CLUSTER_CENTERS, POINTS)

def avg_dist_from_centroid(c, pts):
    avg_dst = 0
    count = 0
    
    for p in pts:
        if p[2] == c[2]:
            avg_dst += distance(c,p)
            count+=1
    
    return avg_dst/(count)

def avg(ls):
    a = 0
    b = 0
    for e in ls:
        a += e[0]
        b += e[1]
    return (round(a/len(ls), 2), round(b/len(ls), 2), e[2])

def cga(k, game_window):
    import time
    import matplotlib.pyplot as plt
    
    global POPULATION
    print("Solving with CGA: " + str(k))
    
    generation_count = 0
    success_rate = 0
    #last_greatest_fitness = 0
    fitness_records = []
    
    t1 = time.time()
    
    init_population(len(POINTS))
    
    #print(POPULATION[0])
    
    calculate_fitness()
    greatest_fitness = best_fitness_in_population()
    
    
    while(True):

        fitness_records.append(greatest_fitness)
        
        if step_tru:
            update_points(game_window)
        
        print(f"Generation: {generation_count}, Fittest: {greatest_fitness}")        
        
        selection()
        
        mutation()
        
        calculate_fitness()
        
        #last_greatest_fitness = greatest_fitness
        greatest_fitness = best_fitness_in_population()
        
        generation_count += 1
        
    t2 = time.time()
    
    print(f"\nTime to compute CGA: {t2 - t1:0.4f} seconds" )
    
    print(f"Success Rate of CGA: {success_rate} %" )
    
    fig = plt.figure(figsize=(14,7))
    fig.add_subplot(122)
    plt.plot(range(0,generation_count), fitness_records,'b-',label='Fitness Per Generation')
    plt.xlabel("Generation")
    plt.ylabel("Fitness (silhouette)")
    plt.legend()
    plt.show()
    
    
    button_labels.append("RESET")
    selectable.append(True)
    return True
        

def update_points(game_window):
    pass


def crossover(parent_a, parent_b):
    global POPULATION
    import random
    
    cross_point = random.randint(0,len(parent_a[0]))
    
    child_a = parent_a[0:cross_point] + parent_b[cross_point:]
    child_b = parent_b[0:cross_point] + parent_a[cross_point:]
    
    fit_a = calc_fitness(child_a)
    fit_b = calc_fitness(child_b)
    
    better = None
    
    if fit_a > fit_b:
        better = child_a
    else:
        better = child_b
    
    return better

def mutation():
    global POPULATION
    
    import random
    to_mutate = 3
    
    new_population = []
    
    for c in POPULATION:
        #print(c)
        
        if random.randint(0,100) < 2:
            #print("Mutating")
            while to_mutate > 0:
                gene = random.randint(0,len(c[0]))
                mutagen = 1 if random.randint(0,100) > 50 else -1
                
                if c[0][gene] > 0:
                    c[0][gene] = c[0][gene] + mutagen
                    to_mutate-=1
        
        new_population.append((c[0], c[1]))
    
    POPULATION = new_population

def selection():
    global POPULATION
    import random
    new_pop = []
    
    for _ in range(len(POPULATION)):
        parent_a = random.choice(POPULATION)
        parent_b = random.choice(POPULATION)
        child = crossover(parent_a,parent_b)
        
        new_pop.append(child)
    
    POPULATION = new_pop

def init_population(population_size):
    global POPULATION, POINTS
    
    import random
    
    for _ in range(population_size):
        #new_pts = []
        
        new_chomosome = []
        
        for p in POINTS:
            c = random.randint(0, len(CLUSTER_COLORS) - 1)
            new_chomosome.append(c)
        
        POPULATION.append((new_chomosome, -1))
    
    #POINTS = new_pts

def calculate_fitness():
    global POPULATION
    from sklearn.metrics import silhouette_score
    
    X = [ [x,-y] for x,y,c in POINTS ]
    
    new_pts = []
    
    for l, c in POPULATION:
        
        fitness = silhouette_score(X, l, metric='euclidean')
        #print(fitness)
        
        new_pts.append((l,fitness))
    
    POPULATION = new_pts 

def calc_fitness(c):
    global POPULATION
    from sklearn.metrics import silhouette_score
    
    X = [ [x,-y] for x,y,c in POINTS ]

    fitness = silhouette_score(X, c[0], metric='euclidean')
    
    return fitness

def best_fitness_in_population():
    global POPULATION
    best = float("-inf")
    for l,f in POPULATION:
        if f > best:
            best = f
    
    return best


def reset():
    global selectable, k_accepted, unlabeled, labels, k, CLUSTER_COLORS, solved, CLUSTER_CENTERS, POINTS
    k_accepted = False
    unlabeled = True
    labels = []    
    CLUSTER_COLORS = []
    font = pygame.font.Font(None, 16)
    
    labels_text = font.render("Labels:", 1, light_gray_color)
    labels.append(labels_text)
    
    unassigned_text = font.render("UNASSIGNED", 1, white_color)
    labels.append(unassigned_text)
    
    button_labels.remove("RESET")
    selectable = [True for s in button_labels]
    CLUSTER_CENTERS = []
    
    pts = []
    for p in POINTS:
        pts.append((p[0], p[1], white_color))
    
    POINTS = pts
    solved = False
    
def draw_hud(game_window):
    global user_input, k_accepted, k, labels, unlabeled, button_labels
    button_font = pygame.font.Font(None, 32)
    input_font = pygame.font.SysFont(None, 48)
    
    pygame.draw.line(game_window, light_gray_color, (GAP + WIDTH, 0), (GAP + WIDTH, HEIGHT + GAP), 3)
    
    pygame.draw.rect(game_window, light_gray_color, (WIDTH + HUD_WIDTH - HALF_GAP - button_width + 5 + button_width + HALF_GAP, HALF_GAP, INFO_BAR_WIDTH- HALF_GAP, HEIGHT) )
    
    pygame.draw.line(game_window, med_gray_color, (WIDTH + HUD_WIDTH - HALF_GAP - button_width + 5 + button_width + HALF_GAP, HALF_GAP), (WIDTH + HUD_WIDTH - HALF_GAP - button_width + 5 + button_width + HALF_GAP, HEIGHT))
    
    for i,label in enumerate(button_labels):
        clr = med_gray_color
        if (selectable[i]):
            clr = light_gray_color
            
            if (i <= 2):
                clr = color_dict['emeraldgreen']
        
        pygame.draw.rect(game_window, clr, (WIDTH + HUD_WIDTH - HALF_GAP - button_width + 5, HALF_GAP + button_height * i, button_width + HALF_GAP, button_height - HALF_GAP))
        l_clr = white_color
        if (user_input == "0" or user_input == str(CUTOFF)) and i > 0: # dont color Reassign red
            l_clr = red_color
        label_text = button_font.render(label, 1, l_clr)
        game_window.blit(label_text, (WIDTH + HUD_WIDTH - HALF_GAP - button_width + 15, HALF_GAP + button_height * i + 15) )
    
    if selectable[0] and selectable[1] and selectable[2]: #IF THEY HAVE NOT SELECTED AN ALGORITHM TO RUN
        selectable[3] = True #MAKE REASSIGN AVAILABLE
        selectable[4] = True #MAKE REASSIGN AVAILABLE
        selectable[5] = True #MAKE REASSIGN AVAILABLE
        selectable[6] = True #MAKE REASSIGN AVAILABLE
    
    input_label = "INPUT:"
    input_label_text = input_font.render(input_label, 1, white_color)
    game_window.blit(input_label_text, (WIDTH + GAP + 5, 5))
    
    clr = black_color
    if (user_input == "0" or user_input == str(CUTOFF)):
        clr = red_color
    user_input_text = input_font.render(user_input, True, clr)
    rect = (WIDTH + GAP * 3 + 35, 5, 65, 30)
    pygame.draw.rect(game_window, white_color, rect)
    game_window.blit(user_input_text, (WIDTH + GAP * 3 + 36, 5))
    
    c_topleft = user_input_text.get_rect().topright
    c_topleft = (c_topleft[0] + WIDTH + GAP * 3 + 37, c_topleft[1] + 6)
    cursor = (c_topleft, (1, user_input_text.get_rect().height - 6))
    if not k_accepted and time.time() % 1 > 0.5:
        pygame.draw.rect(game_window, black_color, cursor)
    
        
    #labels
    if k_accepted and unlabeled:
        labels = []
        unlabeled = False
        
        font = pygame.font.Font(None, 16)
        
        for n in range(k):
            CLUSTER_COLORS.append(random_newish_color())
            l_text = font.render("Cluster " + str(n + 1), 1, CLUSTER_COLORS[n])
            labels.append(l_text)
    
    labels_per_column = 39
    tab, i = 0, 0
    for l in labels:
        if i == labels_per_column:
            tab+=1
            i = 2
        game_window.blit(l, (WIDTH + GAP + 5 + (tab) * (GAP+ HALF_GAP), GAP + 15 * i))
        i+=1
    
    pygame.display.flip()
    pygame.display.update()
    
def controls(event):
    global user_input, CUTOFF, k_accepted, k, POINT_COUNT, POINTS, circles, moons, ANSWERS
    
    if event.type == pygame.KEYDOWN:
        if not k_accepted:
            if event.key != pygame.K_BACKSPACE:    
                user_str = event.unicode
                if str.isnumeric(user_str):
                    if (int(user_input + event.unicode) <= CUTOFF):   
                        if user_input == "0":
                            user_input = ""
                        user_input += event.unicode
                    else:
                        user_input = str(CUTOFF)
            else:
                if (len(user_input) > 1):
                    user_input = user_input[:-1]
                else:
                    user_input = "0"
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        
        if mouse[0] < WIDTH + HUD_WIDTH - HALF_GAP and mouse[0] > WIDTH + HUD_WIDTH - HALF_GAP - button_width:
            
            #button 1: K means
            if mouse[1] > HALF_GAP and mouse[1] < button_height:
                if selectable[0] and int(user_input) > 0 and int(user_input) < CUTOFF:   
                    k = int(user_input)
                    k_accepted = True
                    selectable[0] = True
                    selectable[1] = False
                    selectable[2] = False
                    selectable[3] = False
                    selectable[4] = False
                    selectable[5] = False
                    selectable[6] = False
                    
            #button 2: mK means
            elif mouse[1] > button_height + HALF_GAP and mouse[1] < button_height * 2:
                if selectable[1] and int(user_input) > 0 and int(user_input) < CUTOFF:  
                    k = int(user_input)
                    k_accepted = True
                    selectable[0] = False
                    selectable[1] = True
                    selectable[2] = False
                    selectable[3] = False
                    selectable[4] = False
                    selectable[5] = False
                    selectable[6] = False
            
            #button 3: Genetic
            elif mouse[1] > 2 * button_height + HALF_GAP and mouse[1] < button_height * 3:
                if selectable[2] and int(user_input) > 0 and int(user_input) < CUTOFF:  
                    k = int(user_input)
                    k_accepted = True
                    selectable[0] = False
                    selectable[1] = False
                    selectable[2] = True
                    selectable[3] = False
                    selectable[4] = False
                    selectable[5] = False
                    selectable[6] = False
            
            elif mouse[1] > 3 * button_height + HALF_GAP and mouse[1] < button_height * 4:
                if selectable[3]:
                    selectable[3] = False
                    POINTS.clear()
                    generate_points_randomly(POINT_COUNT,POINTS, white_color)
            
            elif mouse[1] > 4 * button_height + HALF_GAP and mouse[1] < button_height * 5:
                if selectable[4]:
                    selectable[4] = False
                    POINTS.clear()
                    generate_points_randomly_tailored(POINT_COUNT,POINTS, white_color, int(user_input))
            
            elif mouse[1] > 5 * button_height + HALF_GAP and mouse[1] < button_height * 6:
                if selectable[5]:
                    selectable[5] = False
                    POINTS.clear()
                    
                    from sklearn.datasets import (make_circles, make_moons, load_iris, load_wine)
                    scale_up = 30
                    if int(user_input) == 1:
                        X = make_circles(factor=0.5, noise=0.05, n_samples=1500)
                        
                        x = X[0]
                        y = X[1]
                        
                        POINTS = [ (p[0] * scale_up, p[1] * scale_up, white_color) for p in x]
                        ANSWERS = y
                        
                    elif int(user_input) == 2:
                        shift = scale_up/2
                        X = make_moons(n_samples=1500, noise=0.05)
                        x = X[0]
                        y = X[1]
                        
                        ANSWERS = y
                        POINTS = [ (p[0] * scale_up - shift, p[1] * scale_up, white_color) for p in x]
                    
                    elif int(user_input) == 3:
                        X = load_iris()
                        POINTS = [ (float(x[0]) * scale_up - 6 * scale_up, float(x[1]) * scale_up - 3 * scale_up, white_color) for x in X.data[:, :2] ]
                        ANSWERS = X.target
                        #print(ANSWERS)
                    
                    elif int(user_input) == 4:
                        scale_up = 21
                        X = load_wine()
                        POINTS = [ (float(x[0]) * scale_up - 13 * scale_up, float(x[1]) * scale_up - 3 * scale_up, white_color) for x in X.data[:, :2] ]
                        ANSWERS = X.target
                        #print(POINTS)
                    
                    
            
            elif mouse[1] > 6 * button_height + HALF_GAP and mouse[1] < button_height * 7:
                if selectable[6]:
                    selectable[6] = False
                    
                    fn, ext, info, buffer, copy_c = "saves/points", ".txt", datetime.now().strftime("__d_%d-%m-%Y__t_%H-%M-%S"), "", 0
                    
                    while os.path.exists(fn + info + buffer + ext):
                        copy_c+=1
                        buffer = "__" + str(copy_c)
                        
                    with open(fn + info + buffer + ext, "w") as f:
                        for p in POINTS:
                            f.write( str( (p[0],p[1]) ) )
                            f.write(", ")
                            f.write(str(p[2]))
                            f.write("\n")
            
            else:
                if mouse[1] > 7 * button_height + HALF_GAP and mouse[1] < button_height * 8:
                    if len(selectable) > 7:
                        if selectable[7]:
                            selectable[7] = False
                            reset()


def draw_graph(game_window, color):
    dash_size = 1
    
    font = pygame.font.Font(None, 16)
    
    #background
    pygame.draw.rect(game_window, gray_color, (0,0, 2 * WIDTH, 2 * HEIGHT))
    
    #straight lines for the axis
    pygame.draw.line(game_window, color, (      HALF_GAP, HALF_GAP + HEIGHT/2),   (HALF_GAP + WIDTH,  HALF_GAP + HEIGHT/2) ) # x axis
    pygame.draw.line(game_window, color, (WIDTH/2 + HALF_GAP,        HALF_GAP), (HALF_GAP + WIDTH/2,  HALF_GAP + HEIGHT  ) ) # y axis
    
    #draw y axis dashes and labels
    LENGTH_OF_Y_RANGE = ( abs(Y_RANGE[1]) + abs(Y_RANGE[0]) )
    y_dash_spacing = HEIGHT/LENGTH_OF_Y_RANGE
    y_label = Y_RANGE[1]
    for i in range(LENGTH_OF_Y_RANGE + 1):
        y_pos = y_dash_spacing * i
        y_left_of_axis = (HALF_GAP + WIDTH/2 - dash_size, HALF_GAP + y_pos)
        y_right_of_axis = (HALF_GAP + WIDTH/2 + dash_size, HALF_GAP + y_pos)
        pygame.draw.line(game_window, color, y_left_of_axis, y_right_of_axis ) # y axis dash
        
        y_text = font.render(str(y_label), 1, color)
        y_right_of_axis_for_label = (y_right_of_axis[0] + 1, y_right_of_axis[1] - 3)
        if y_label != 0 and y_label % display_interval == 0:    
            game_window.blit(y_text, y_right_of_axis_for_label)
        y_label -= 1
        
    #draw x axis dashes and labels
    LENGTH_OF_X_RANGE = ( abs(X_RANGE[1]) + abs(X_RANGE[0]) )
    x_dash_spacing = WIDTH/LENGTH_OF_X_RANGE
    x_label = X_RANGE[0]
    for i in range(LENGTH_OF_X_RANGE+1):
        x_pos = x_dash_spacing * i
        x_beneath_of_axis = (HALF_GAP + x_pos, HALF_GAP + HEIGHT/2 - dash_size)
        x_top_of_axis = (HALF_GAP + x_pos, HALF_GAP + HEIGHT/2 + dash_size)
        pygame.draw.line(game_window, color, x_beneath_of_axis, x_top_of_axis ) # x axis dash
        
        x_text = font.render(str(x_label), 1, color)
        x_beneath_of_axis_for_label = (x_beneath_of_axis[0], x_beneath_of_axis[1] + 5)
        if x_label != 0 and x_label % display_interval == 0:   
            game_window.blit(x_text, x_beneath_of_axis_for_label)
        x_label += 1
        
def generate_points_randomly(count_of_points, p, color):
    import random
    
    #p = []
    
    while( len(p) < count_of_points):
        random_x = round(random.uniform(X_RANGE[0],X_RANGE[1]), 2)
        random_y = round(random.uniform(Y_RANGE[0],Y_RANGE[1]), 2)
        random_point = (random_x, random_y, color)
        if random_point not in p:
            p.append(random_point)
    
def generate_points_randomly_tailored(count_of_points, p, color, k):
    global ANSWERS
    import random
    clusters = []
    ANSWERS = []
    custer_range = X_RANGE[1]**0.5 * 3
    overlap = custer_range/2 * 2
    
    while(len(clusters) < k):
        random_x = round(random.uniform(X_RANGE[0],X_RANGE[1]), 2)
        random_y = round(random.uniform(Y_RANGE[0],Y_RANGE[1]), 2)
        random_center = (random_x, random_y)
        safe_dst = True
        for c in clusters:
            if (distance(c, random_center) + overlap) < 2 * custer_range + 1:
                safe_dst = False
                break
        if safe_dst:
            clusters.append(random_center)
    
    per_cluster = round(count_of_points/k)
    cluster_c = 0
    
    for c in clusters:
        
        in_cluster = 0
        while(in_cluster < per_cluster):
            random_x = round(random.uniform(X_RANGE[0],X_RANGE[1]), 2)
            random_y = round(random.uniform(Y_RANGE[0],Y_RANGE[1]), 2)
            random_point_around_center = (random_x, random_y, color)
            if(distance(random_point_around_center, c) < custer_range):
                    if random_point_around_center not in p:
                        p.append(random_point_around_center)
                        ANSWERS.append(cluster_c)
                        in_cluster+=1
        cluster_c+=1
    
    
    while (len(p) < count_of_points):
        random_x = round(random.uniform(X_RANGE[0],X_RANGE[1]), 2)
        random_y = round(random.uniform(Y_RANGE[0],Y_RANGE[1]), 2)
        random_point = (random_x, random_y, color)
        if random_point not in p:
            p.append(random_point)
        
def input_data_set(dataset, p, color):
    pass

def display_points(game_window, pts, mouse = True, lines = False):
    global CLUSTER_CENTERS
    draw_all_lines = lines
    draw_lines_near_mouse = mouse
        
    LENGTH_OF_Y_RANGE = ( abs(Y_RANGE[1]) + abs(Y_RANGE[0]) )
    y_spacing = HEIGHT/LENGTH_OF_Y_RANGE
    
    LENGTH_OF_X_RANGE = ( abs(X_RANGE[1]) + abs(X_RANGE[0]) )
    x_spacing = WIDTH/LENGTH_OF_X_RANGE
    
    draw_line_radius = round(min(y_spacing, x_spacing)/2)
    point_size = 3
    
    for p in pts:
        
        tran_p_x = round(ORIGIN[0] + (p[0] * x_spacing))
        tran_p_y = round(ORIGIN[1] + (p[1] * y_spacing))
        tran_p = (int(tran_p_x), int(tran_p_y))
        
        #draw the point
        pygame.draw.circle(game_window, p[2], tran_p, point_size )
        
        if draw_all_lines:
            pygame.draw.line(game_window, p[2], tran_p, (HALF_GAP + WIDTH/2, tran_p[1]) ) 
            pygame.draw.line(game_window, p[2], tran_p, (tran_p[0], HALF_GAP + HEIGHT/2) )
        
        if draw_lines_near_mouse:
            mouse_pos = pygame.mouse.get_pos()
            
            if distance(tran_p, mouse_pos) < draw_line_radius:
                pygame.draw.line(game_window, p[2], tran_p, (HALF_GAP + WIDTH/2, tran_p[1]) ) 
                pygame.draw.line(game_window, p[2], tran_p, (tran_p[0], HALF_GAP + HEIGHT/2) )
    
    cross_size = 7
    cross_w = 5
    for c in CLUSTER_CENTERS:
        tran_c_x = round(ORIGIN[0] + (c[0] * x_spacing))
        tran_c_y = round(ORIGIN[1] + (c[1] * y_spacing))
        tran_c = (int(tran_c_x), int(tran_c_y), c[2])
        
        pygame.draw.line(game_window, tran_c[2], (tran_c[0]-cross_size,tran_c[1]-cross_size), (tran_c[0]+cross_size,tran_c[1]+cross_size), cross_w ) 
        pygame.draw.line(game_window, tran_c[2], (tran_c[0]+cross_size,tran_c[1]-cross_size), (tran_c[0]-cross_size,tran_c[1]+cross_size), cross_w )
            
def distance(pos1, pos2):
    return ((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2) ** 0.5

def random_newish_color():
    import random
    clr = random.choice(color_rgb_arr)
    while clr in CLUSTER_COLORS:
        clr = random.choice(color_rgb_arr)
    return clr

if __name__ == "__main__":
    main()
    
