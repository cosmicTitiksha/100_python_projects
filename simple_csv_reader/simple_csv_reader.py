# This program is a simple CSV reader
IRIS_FILE = 'Iris.csv'

def load_data():
    try:
        with open(IRIS_FILE, 'r') as f:
            data = [lines.strip() for lines in f.readlines()]
        return data[1:]
    except FileNotFoundError:
        print(f"Error: The file '{IRIS_FILE}' was not found.")
        return []
    
def view_data(iris):
    for data in iris:
        print(data.split(","))

iris = load_data()
view_data(iris)