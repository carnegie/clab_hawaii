'''
This code identifies outliers in the data by computing the median and iqr and using q1-1.5iqr or q3+1.5iqr as the limit for non-outlier data.
It then performs regression imputation to replace those outliers with appropriate values
'''
import csv
import statistics
from sklearn.linear_model import LinearRegression

def find_outlier_indices(csv_file, column_index):
    data = []
    indices = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i >= 12:  # Start reading from row 13 (index 12)
                data.append(float(row[column_index]))
                indices.append(i)

    sorted_data_indices = [i for _, i in sorted(zip(data, indices))]
    sorted_data = sorted(data)

    q1 = statistics.median(sorted_data[:len(sorted_data)//2])
    q3 = statistics.median(sorted_data[(len(sorted_data)+1)//2:])
    iqr = q3 - q1
    threshold_upper = q3 + 1.5 * iqr
    threshold_lower = q1 - 1.5 * iqr

    outlier_indices = []
    for value, index in zip(data, indices):
        if value > threshold_upper or value < threshold_lower:
            outlier_indices.append(index)

    return q1, q3, statistics.median(data), iqr, outlier_indices

def change_outlier_values_to_zero(csv_file, column_index, outlier_indices):
    with open(csv_file, 'r') as file:
        data = list(csv.reader(file))
        for index in outlier_indices:
            data[index][column_index] = '0'  # Change the value at the outlier index in column 5 to 0

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def perform_regression_imputation(csv_file, column_index, outlier_indices):
    non_outlier_data = []
    non_outlier_indices = []

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i >= 12:  # Start reading from row 13 (index 12)
                value = float(row[column_index])
                if i not in outlier_indices:
                    non_outlier_data.append(value)
                    non_outlier_indices.append(i)

    X = [[index] for index in non_outlier_indices]
    y = non_outlier_data

    regression_model = LinearRegression()
    regression_model.fit(X, y)

    with open(csv_file, 'r') as file:
        data = list(csv.reader(file))
        for index in outlier_indices:
            predicted_value = regression_model.predict([[index]])
            data[index][column_index] = str(predicted_value[0])
            print(f"Outlier index: {index}, New value: {predicted_value[0]}")

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Example usage
csv_file_path = '/Users/Dominic/Desktop/2006_2020_Hawaii_State_Hourly_Demand_Weighted to be imputed.csv'
column_index = 4  # 0-based index for the 5th column

q1, q3, median, iqr, outlier_indices = find_outlier_indices(csv_file_path, column_index)
print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"Median: {median}")
print(f"IQR: {iqr}")
print("Outlier Indices:")
for index in outlier_indices:
    print(f"Index of outlier: {index}")

change_outlier_values_to_zero(csv_file_path, column_index, outlier_indices)
perform_regression_imputation(csv_file_path, column_index, outlier_indices)