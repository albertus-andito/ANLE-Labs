import os, random, math

TRAINING_DIR = "./sentence-completion/Holmes_Training_Data"  # this needs to be the parent directory for the training corpus


def get_training_testing(training_dir=TRAINING_DIR, split=0.5):
    filenames = os.listdir(training_dir)
    n = len(filenames)
    print("There are {} files in the training directory: {}".format(n, training_dir))
    # random.seed(53) #if you want the same random split every time
    random.shuffle(filenames)
    index = int(n * split)
    return filenames[:index], filenames[index:]


trainingfiles, heldoutfiles = get_training_testing()
print(trainingfiles)
