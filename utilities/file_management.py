from os import path, makedirs


def create_folder(folder_name):
    """Creates a folder in the project root.

    folder_name -- string - the name of the folder to be created."""
    if not path.exists(folder_name):
        makedirs(folder_name)


def write_data_to_file(data, filename, mode):
    """Writes the given data in a file.

    data -- string - the data to be written in the file.
    filename -- string - the name of the file.
    mode -- string - the mode indicating how the file is going to be opened."""
    with open(filename, mode) as results_file:
        results_file.write(data)


def log(results):
    """Keeps record of the results in a file and prints them in the console.

    results -- string - the results to be recorded and printed."""
    create_folder('results')
    write_data_to_file(results + '\n', 'results/results.txt', 'a')
    print results
