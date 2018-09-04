###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cows_local=cows.items()
    cows_local=sorted(cows_local,key=lambda x:x[1],reverse=True)
    cows_name=cows.keys()
    cows_visited=set()
    result=[]
    for cow,weight in cows_local:
        ltrip=[]
        ltrip_weight=0
        if weight>limit:
            cows_visited.add(cow)
        elif cow in cows_visited:
            continue
        else:
            ltrip_weight=weight
            ltrip.append(cow)
            cows_visited.add(cow)
            for lcow,lw in cows_local:
                if lcow!=cow and lcow not in cows_visited and cows[lcow]+ltrip_weight<=limit:
                    cows_visited.add(lcow)
                    ltrip.append(lcow)
                    ltrip_weight+=cows[lcow]
            result.append(ltrip)
    return result









# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """


    cows_local = cows.items()
    cows_local = sorted(cows_local, key=lambda x: x[1], reverse=True)
    cows_name=[x[0] for x in cows_local]

    valid_trip_list=[]
    for partition in get_partitions(cows_name):

        valid_trip=True
        #print("Starting partition:",partition)
        for i in range(len(partition)):
           l=0
           #print("Partition i",str(i),"is",partition[i])
           for cow in partition[i]:
                l+=cows[cow]
           if l>limit:
               valid_trip=False
        if valid_trip:
            valid_trip_list.append(partition)
    valid_trip_list=sorted(valid_trip_list,key=len)
    return valid_trip_list[0]

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """

    # TODO: Your code here
    cows = load_cows("ps1_cow_data.txt")
    limit = 10
    start = time.time()
    greedy_set=greedy_cow_transport(cows, limit)
    ## code to be timed
    end = time.time()
    print("Greedy set is {} takes time:{}".format(len(greedy_set),end - start))
    start = time.time()
    bf_set=brute_force_cow_transport(cows,limit)
    end = time.time()
    print("BF set is {} takes time:{}".format(len(bf_set), end - start))


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)
# cows={"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
# # cows={'MooMoo': 50, 'Horns': 25, 'Boo': 20, 'Milkshake': 40, 'Miss Bella': 25, 'Lotus': 40}
# # limit=100
print(greedy_cow_transport(cows, limit))

print(brute_force_cow_transport(cows, limit))
compare_cow_transport_algorithms()

