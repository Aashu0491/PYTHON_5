def extract_numerical_data(input_data):
    # Filter only numerical characters from the string
    numerical_data = ''.join(filter(str.isdigit, input_data))
    return numerical_data

input_data = "abcd12ef23"
result = extract_numerical_data(input_data)
print("Numerical data:", result)  
