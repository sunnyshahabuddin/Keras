Models = ["m1", "m2", "m3"]
RMSE = [10.0, 5.0, 7.0]
MAPE = [2.0, 1.0, 3.0]

model_data = [{'model': model, 'RMSE': rmse, 'MAPE': mape, 'rank': 0} for model, rmse, mape in zip(Models, RMSE, MAPE)]
sorted_model_data = sorted(model_data, key=lambda x: (x['RMSE'], x['MAPE']))
for rank, data in enumerate(sorted_model_data, start=1):
    data['rank'] = rank
print(sorted_model_data)
