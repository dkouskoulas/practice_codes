

def tower_of_hanoi(n, source, destination, auxiliary):


    if n == 1:
        print(f'Move disk 1 from {source} to {destination}')
        return 
    
    # move n-1 disks from source to auxiliary
    tower_of_hanoi(n-1, source, auxiliary, destination)

    print(f'Move disk {n} from {source} to {destination}')
    # move n-1 disks from auxiliary to destination
    tower_of_hanoi(n-1, auxiliary, destination, source)