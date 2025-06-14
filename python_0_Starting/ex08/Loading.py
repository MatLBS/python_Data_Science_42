import shutil
from time import sleep


def ft_tqdm(lst: range):
    """
    Simulate a progress bar for iterating through a range.

    Args:
        lst (range): The range to iterate through.

    Yields:
        is a keyword in Python used in the context of creating generators.
        Generators are a way to create iterators, which are objects used to
        iterate over a sequence of values without having to store all those
        values in memory at once. Instead of generating allvalues and returning
        them in one go, a generator yields one value at a time whenever the
        yield statement is encountered.
    """
    terminal_size = shutil.get_terminal_size().columns - 30
    bar_width = terminal_size - 10
    max_value = max(lst) + 1

    i = 0
    while i <= max_value:
        yield
        pourcentage = int(i / max_value * 100)
        done = int((pourcentage / 100) * bar_width)
        bar = "█" * done + " " * (bar_width - done - 1)
        print(f"{pourcentage}%|{bar}| {i}/{max_value}", end='\r')
        i += 1


if __name__ == "__main__":
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
