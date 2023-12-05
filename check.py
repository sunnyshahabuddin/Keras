def add_today_values(predictions, today_values):
    # loop through the predictions
    for prediction in predictions:
        # get the metric name from the prediction
        metric_name = prediction['metric_name']
        # get the today value from the today_values dictionary
        today_value = today_values[metric_name]
        # add the today value to the prediction
        prediction['today_value'] = today_value
    
    for prediction in predictions:
        # add a new key threshold to the prediction which is plus minus 5% of the today value in the format [0.95, 1.05]]
        prediction['threshold'] = [prediction['today_value'] * 0.95, prediction['today_value'] * 1.05]
        # now add a new key called exception which will have value 'Yes' if the prediction value is outside the threshold and 'No' if it is within the threshold
        if prediction['value'] < prediction['threshold'][0] or prediction['value'] > prediction['threshold'][1]:
            prediction['exception'] = 'Yes'
        else:
            prediction['exception'] = 'No'
    # return the predictions
    return predictions
