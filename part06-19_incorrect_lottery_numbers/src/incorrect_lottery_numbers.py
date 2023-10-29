# Write your solution here
# import re

# def is_valid_line(line):
#     # Regular expression pattern to validate the line format
#     pattern = r'^week (\d+);([1-9]|[1-3]\d|39)(,[1-9]|[1-3]\d|39){6}$'
#     return bool(re.match(pattern, line))

# def filter_incorrect(input_file, output_file):
#     try:
#         with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
#             for line in input_file:
#                 if is_valid_line(line.strip()):
#                     output_file.write(line)
#     except FileNotFoundError:
#         print(f"Error: Input file '{input_file}' not found.")
#     except PermissionError:
#         print(f"Error: Cannot read from input file '{input_file}' or write to output file '{output_file}'. Check file permissions.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage:
# if __name__ == '__main__':
#     input_file = 'lottery_numbers.csv'
#     output_file = 'correct_numbers.csv'
#     filter_incorrect(input_file, output_file)

import re

def is_valid_line(line):
    # Regular expression pattern to validate the line format
    pattern = r'^week (\d+);([1-9]|[1-3]\d|39)(,[1-9]|[1-3]\d|39){6}$'
    return bool(re.match(pattern, line))

def filter_incorrect(input_file, output_file):
    def validate_and_write(line):
        if is_valid_line(line.strip()):
            return line
        return None

    try:
        with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
            valid_lines = map(validate_and_write, input_file)
            filtered_lines = filter(None, valid_lines)
            output_file.writelines(filtered_lines)
    except FileNotFoundError:
        return f"Error: Input file '{input_file}' not found."
    except PermissionError:
        return f"Error: Cannot read from input file '{input_file}' or write to output file '{output_file}'. Check file permissions."
    except Exception as e:
        return f"An error occurred: {e}"

    return f"Filtering completed successfully. Valid lines written to '{output_file}'."

# Example usage:
if __name__ == '__main__':
    input_file = 'lottery_numbers.csv'
    output_file = 'correct_numbers.csv'
    result = filter_incorrect(input_file, output_file)
    print(result)


