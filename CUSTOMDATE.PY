from datetime import datetime

def custom_date_formatter(input_date, current_format, target_format):
    # Parse the input date according to the given current format
    date_obj = datetime.strptime(input_date, current_format)
    
    # Convert the date object to the desired format
    formatted_date = date_obj.strftime(target_format)
    return formatted_date


input_date = "2024-10-20"
current_format = "%Y-%m-%d"  # yyyy-mm-dd
target_format = "%d-%m-%Y"   # dd-mm-yyyy

formatted_date = custom_date_formatter(input_date, current_format, target_format)
print("Formatted date:", formatted_date)  
