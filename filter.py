import os

def remove_duplicates_and_filter(input_file, output_file):
    # Use a set to store unique lines
    unique_lines = set()
    duplicate_count = 0

    try:
        # Open the input file in read mode with UTF-8 encoding
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                # Strip leading and trailing whitespaces
                cleaned_line = line.strip()
                if cleaned_line and not cleaned_line.startswith(('UNKNOWN', ':', ' ')) and ':' in cleaned_line:
                    if cleaned_line in unique_lines:
                        duplicate_count += 1
                    else:
                        unique_lines.add(cleaned_line)

        # Construct the output file path
        if not os.path.dirname(output_file):
            output_file = os.path.join(os.path.dirname(os.path.abspath(input_file)), output_file)

        # Open the output file in write mode with UTF-8 encoding and write the unique lines
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join(sorted(unique_lines)))

        print(f"Filtered lines removed. Unique lines written to '{output_file}'.")
        print(f"Removed {duplicate_count} duplicate lines.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Select an action:")
    print("1. Remove duplicate lines and filter")
    print("2. Other action (to be implemented)")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        input_file_name = input("Enter the input file name: ").strip()

        # Check if input file exists
        if not os.path.isfile(input_file_name):
            print(f"Error: Input file '{input_file_name}' not found.")
            return

        output_file_name = input("Enter the output file name: ").strip()

        remove_duplicates_and_filter(input_file_name, output_file_name)
    elif choice == '2':
        print("Other action to be implemented.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
