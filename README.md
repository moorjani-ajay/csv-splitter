# CSV Splitter

This is a Python script that allows you to split a large CSV (Comma-Separated Values) file into smaller chunks based on the specified maximum number of bytes and lines per split. It can be useful when dealing with large datasets that need to be processed or loaded in smaller portions.

## Prerequisites

- Python 3.x
- `csv` module
- `argparse` module

## Usage

1. Ensure that you have Python 3.x installed on your system.
2. Install the required modules by running the following command:
   ```
   pip install argparse
   ```
3. Save the script to a file, e.g., `csv_splitter.py`.
4. Open a terminal or command prompt and navigate to the directory where the script is saved.
5. Run the script using the following command:

   ```
   python csv_splitter.py input_file output_dir max_bytes max_lines
   ```

   - `input_file`: The name of the input CSV file you want to split.
   - `output_dir`: The directory where the output CSV chunks will be saved. If the directory doesn't exist, it will be created.
   - `max_bytes`: The maximum number of bytes per split. Once the total size of the split exceeds this value, a new split file will be created.
   - `max_lines`: The maximum number of lines per split. Once the total number of lines in the split exceeds this value, a new split file will be created.

6. The script will process the input file and generate multiple CSV files in the output directory, each containing a portion of the original data.

## Example

Suppose you have a large CSV file named `data.csv` and you want to split it into smaller chunks, limiting each split to a maximum of 10,000 bytes and 1,000 lines. You can use the following command:

```
python csv_splitter.py data.csv output_chunks 10000 1000
```

The script will create a directory named `output_chunks` (if it doesn't exist) and save the split CSV files inside it, named `split_1.csv`, `split_2.csv`, and so on.

## License

This script is licensed under the [MIT License](LICENSE). Feel free to modify and use it according to your needs.

## Contributions

Contributions to the script are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/your-repo-url).

## Disclaimer

This script is provided as-is without any warranty. Use it at your own risk. The author is not responsible for any damage or loss caused by the use of this script.

## Contact

For any questions or inquiries, please contact [your-email-address].
