import os
import csv
import argparse


def split_csv(input_file, output_dir, max_bytes, max_lines):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    with open(input_file, "r") as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header

        split_count = 1
        current_bytes = 0
        current_lines = 0
        current_chunk = []

        for row in reader:
            current_chunk.append(row)
            current_bytes += len(",".join(row).encode())
            current_lines += 1

            if current_bytes > max_bytes or current_lines > max_lines:
                output_file = os.path.join(output_dir, f"split_{split_count}.csv")
                with open(output_file, "w", newline="") as output:
                    writer = csv.writer(output)
                    writer.writerow(header)
                    writer.writerows(current_chunk)

                # Reset the counters and the current chunk
                split_count += 1
                current_bytes = 0
                current_lines = 0
                current_chunk = []

        # Write the last chunk if it's not empty
        if current_chunk:
            output_file = os.path.join(output_dir, f"split_{split_count}.csv")
            with open(output_file, "w", newline="") as output:
                writer = csv.writer(output)
                writer.writerow(header)
                writer.writerows(current_chunk)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split a CSV file.")
    parser.add_argument("input_file", help="Input CSV file name")
    parser.add_argument("output_dir", help="Output directory")
    parser.add_argument("max_bytes", type=int, help="Maximum number of bytes per split")
    parser.add_argument("max_lines", type=int, help="Maximum number of lines per split")

    args = parser.parse_args()

    split_csv(args.input_file, args.output_dir, args.max_bytes, args.max_lines)
