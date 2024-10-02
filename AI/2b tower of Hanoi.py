print("04_Jayprabha Nadar")

def move_tower(height, source, target, auxiliary):
    if height >= 1:
        # Move the tower of height-1 to the auxiliary pole
        move_tower(height - 1, source, auxiliary, target)
        # Move the bottom disk to the target pole
        move_disk(source, target)
        # Move the tower from the auxiliary pole to the target pole
        move_tower(height - 1, auxiliary, target, source)

def move_disk(source, target):
    print(f"Moving disk from {source} to {target}")

# Solve the Tower of Hanoi puzzle with 3 disks
move_tower(3, "A", "B", "C")
