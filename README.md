# Cloud_deployment
Repository to deploy a simple model for cloud class.

This model will calculate how many bycicles you will need to have in order to satisfy demand for a particular hour in a particular day.

To run this repository you will need to install sklearn 0.23.2 and have file timeseries.csv on data folder. Remember to change azureml folder for .azureml so all code can work correctly.

Steps

1. Run 01-create-workspace and 02-create-compute to create azure workspace and configure virtual machine.
2. Run 04-add-missing-values and 05-create-mean to complete all missing values from original CSV file and create a new feature.
3. Run demand-model to create model.pkl file to register.
4. Run 07-model-registration-azure to register your model in Azure.
5. Deploy model with 08-deploy-azure-model-aci.

To post you will need following parameters and ranges:

hr: 0-23\
season: 1-4\
holiday: 0-1\
weekday: 0-6\
weeks_mean: float with any number of bicycles from last week.

Post must be JSON format.

You can use 06-upload-dataset to upload your dataset to Azure and 03-test-workspace-remote to test it. Please remember to configure your owen JSON to have your tenant and ID, if you avoid this step this repository will not work as intended.

Remember to shut your endpoint after finalizing all tests.
