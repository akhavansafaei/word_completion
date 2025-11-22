import random

# Define the input and output file names
input_filename = "sampleData.txt"  # or "sampleData200k.txt" depending on the dataset size
sample_size = 500  # Specify the desired sample size (e.g., 500, 1,000, 2,000, etc.)
output_filename = f"sampleData{sample_size}.txt"  # Specify the desired output file name

# Read the original dataset and store it in a list of (word, frequency) tuples
with open(input_filename, 'r') as file:
    dataset = [line.strip().split() for line in file]

# Check if the dataset contains at least the desired sample size
if len(dataset) < sample_size:
    print("The dataset is smaller than the desired sample size.")
else:
    # Randomly sample words from the dataset to create the new dataset
    sampled_data = random.sample(dataset, sample_size)

    # Write the sampled data to a new file
    with open(output_filename, 'w') as output_file:
        for word, frequency in sampled_data:
            output_file.write(f"{word} {frequency}\n")

print(f"Sampled dataset with {sample_size} words saved to {output_filename}.")
