import csv

input_path = "INTER/INTER/16144517608610/etc/txt.done.data"
output_path = "dataset/train.csv"

with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", newline='', encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["path", "sentence"])  # CSV header

    for line in infile:
        parts = line.strip().split(maxsplit=1)
        if len(parts) == 2:
            writer.writerow(parts)