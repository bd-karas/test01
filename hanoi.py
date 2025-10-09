def hanoi(n, source, target, auxiliary):
    """
    Solve the Tower of Hanoi problem.

    Parameters:
    - n (int): Number of disks.
    - source (str): The name of the source rod.
    - target (str): The name of the target rod.
    - auxiliary (str): The name of the auxiliary rod.
    """
    if n == 1:
        # Base case: Move one disk directly from source to target
        print(f"Move disk 1 from {source} to {target}")
        return

    # Step 1: Move n-1 disks from source to auxiliary using target as auxiliary
    hanoi(n - 1, source, auxiliary, target)

    # Step 2: Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")

    # Step 3: Move the n-1 disks from auxiliary to target using source as auxiliary
    hanoi(n - 1, auxiliary, target, source)


# Example usage
if __name__ == "__main__":
    num_disks = 3  # Number of disks
    hanoi(num_disks, "A", "C", "B")
