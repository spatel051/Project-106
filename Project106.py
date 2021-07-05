import csv
import numpy as np
import plotly.express as px

def get_data_source(data_path):
    coffee = []
    sleep = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    
    return {"x": coffee, "y": sleep}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between Coffee in ml and sleep in hours :- " + str(correlation[0, 1]))

def plot_figure():
    with open('data2.csv') as f:
        df = csv.DictReader(f)

        fig = px.scatter(df, x = 'Coffee in ml', y = 'sleep in hours')
        fig.show()

def set_up():
    data_path = 'data2.csv'
    data_source = get_data_source(data_path)
    find_correlation(data_source)
    plot_figure()

set_up()