from math import dist

PRINT = True

def kmeans(points,cluster_centers,iterations=10):
    if PRINT:
        print('\nPoints')
        print(points, '\n')

    for i in range(iterations):
        if PRINT:
            print(f'\n\nIterations {i}\n')

        #assign points to each cluster
        assigned_points = []
        for point in points:
            distances_from_point_to_centers = [ ( round(dist(point, cluster_center),2), cluster_center ) for cluster_center in cluster_centers]

            cluster_assigned_to_point = min(distances_from_point_to_centers)
            
            assigned_points.append( ( point, cluster_assigned_to_point[1], cluster_assigned_to_point[0] ) )

        #seperate the points into a tuple with assigned cluster labels
        points_by_cluster_centers = []
        for cluster_center in cluster_centers:
            points_in_cluster = [ assigned_point[0] for assigned_point in assigned_points if assigned_point[1] == cluster_center]

            points_by_cluster_centers.append((cluster_center,points_in_cluster))
        
        if PRINT:
            print('Points by cluster.')
            print(points_by_cluster_centers)

        # determine the new cluster centers
        new_cluster_centers = []
        for cluster_and_points in points_by_cluster_centers:
            new_cluster_center = (0,0)
            for point_in_cluster in cluster_and_points[1]:
                new_cluster_center = (new_cluster_center[0] + point_in_cluster[0], new_cluster_center[1] + point_in_cluster[1])
            
            new_cluster_centers.append( ( new_cluster_center[0]/len(cluster_and_points[1]),new_cluster_center[1]/len(cluster_and_points[1]) ) )
        
        if PRINT:
            print('\nNew Cluster Centers')
            print(new_cluster_centers)

        if new_cluster_centers == cluster_centers:
            return cluster_centers
            
        cluster_centers = new_cluster_centers

POINTS = [(2,10),(2,5),(8,4),(5,8),(7,5),(6,4),(1,2),(4,9)]

CLUSTER_CENTERS = [(2,10),(5,8),(1,2)]

print( 'Results: ', kmeans(POINTS,CLUSTER_CENTERS, 3) )
