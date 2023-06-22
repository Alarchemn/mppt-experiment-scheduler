import pandas as pd


def transfor_data(hour_forecast):
    """
    Transform the hour forecast data into a pandas DataFrame.

    Args:
        hour_forecast (list): List of forecasted hours.

    Returns:
        pandas.DataFrame: Transformed data with columns:
            - 'Hour': Hour value.
            - 'Temperature': Temperature value.
            - 'UV Radiation': UV radiation value.
            - 'Clouds': Cloud coverage value.
            - 'Condition': Condition text.
            - 'Rain Probability': Chance of rain value.
            - 'Will rain': "Will it rain" value.
    """
    
    # Initialize empty lists to store the data
    hours = []
    temp = []
    uv = []
    cloud = []
    condition = []
    rain_prob = []
    will_rain = []

    # Iterate through each hour in the hour_forecast
    for hour in hour_forecast:
        # Extract the data
        hours.append(hour['time'].split()[1])
        temp.append(hour['temp_c'])
        uv.append(hour['uv'])
        cloud.append(hour['cloud'])
        condition.append(hour['condition']['text'])
        rain_prob.append(hour['chance_of_rain'])
        will_rain.append(hour['will_it_rain'])
        
    # Create a dictionary with the collected data
    data = {
        'Hour':hours,
        'Temperature': temp,
        'UV Radiation': uv,
        'Clouds': cloud,
        'Condition': condition,
        'Rain Probability': rain_prob,
        'Will rain': will_rain
    }
    
    # Convert the dictionary into a pandas DataFrame and return it
    return pd.DataFrame(data=data)\
    


def generate_message(clean_forecast):
    """
    Generate an experiment schedule based on the provided clean forecast data.

    Args:
        clean_forecast (pandas.DataFrame): Cleaned forecast data with the following columns:
            - 'Hour': Hour value.
            - 'Temperature': Temperature value.
            - 'UV Radiation': UV radiation value.
            - 'Clouds': Cloud coverage value.
            - 'Condition': Condition text.
            - 'Rain Probability': Chance of rain value.
            - 'Will rain': "Will it rain" value.

    Prints:
        Experiment schedule information including:
            - Ideal conditions experiments schedule: hours, max temperature, max UV radiation.
            - Partly cloudy experiments schedule: hours, max temperature, max UV radiation.
            - Worst condition experiments schedule: hours.
            - Rain is expected at: hours.
    """
    # Filter the clean forecast for effective UV radiation (greater than 1)
    efective = clean_forecast[clean_forecast['UV Radiation'] > 1]
    
    # Filter for partly cloudy, ideal, worst (full cloudy) and rain conditions
    partly = efective[(efective['Clouds'] > 20) & (efective['Clouds'] < 70)]
    ideal = efective[(efective['Clouds'] < 10) & (efective['UV Radiation'] > 8)]
    full = efective[efective['Clouds'] > 70]
    rain = efective[efective['Rain Probability'] > 65]
    
    # Extract necessary information for ideal case
    ideal_hours = f'{ideal["Hour"].min()} to {ideal["Hour"].max()}'
    ideal_temp = ideal['Temperature'].max()
    ideal_uv = ideal['UV Radiation'].max()
    
    # Not every day is cloudy or rainy
    if len(partly["Hour"]) == 0:
        partly_caption = 'Non-scheduled'
    else:
        part_hour = partly["Hour"].values
        part_temp = partly["Temperature"].max()
        part_uv = partly["UV Radiation"].max()
        partly_caption = f'{part_hour}, max temp: {part_temp}, max UV: {part_uv}'
    
    if len(full["Hour"]) == 0:
        full_caption = 'Non-scheduled'
    else:
        full_hour = f'{full["Hour"].min()} to {full["Hour"].max()}'
        full_temp = full["Temperature"].max()
        full_uv = full["UV Radiation"].max()
        full_caption = f'{full_hour}, max temp: {full_temp}, max UV: {full_uv}'
        
    if len(rain["Hour"]) == 0:
        rain_hours = 'Non-expected'
    else:
        rain_hours = f'{rain["Hour"].min()} to {rain["Hour"].max()}'
    
    # Print the experiment schedule information
    message = f'''*Ideal conditions experiments schedule*: {ideal_hours}, max temp: {ideal_temp}, max UV: {ideal_uv}
    
*Partly cloudy experiments schedule*: {partly_caption}
    
*Worst condition experiments schedule*: {full_caption}
    
*Rain is expected at*: {rain_hours}'''
    
    return message