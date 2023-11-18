import pandas as pd
import os

class csvExporter:
    def read_csv(self, source_file_path, directory, filename):
        # Read data from source CSV file
        try:
            df = pd.read_csv(source_file_path)
        except Exception as e:
            print(f"Error reading the file: {e}")
            return

        # Save the DataFrame to a new CSV file
        if not filename.endswith(".csv"):
            filename += ".csv"
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = os.path.join(directory, filename)
        df.to_csv(file_path, index=True)

        print(f"File saved successfully at {file_path}")

# Get user input for source file, new filename, and directory
source_file_path = input("Enter the path of the source CSV file: ")
filename = input("Name of new csv file: ")
directory = input(r"Directory address for the new file: ")

# Create an instance of the class and call the method
exporter = csvExporter()
exporter.read_csv(source_file_path, directory, filename)
