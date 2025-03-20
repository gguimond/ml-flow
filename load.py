import mlflow
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split

mlflow.set_tracking_uri(uri="http://127.0.0.1:6001")

# Load the model back for predictions as a generic Python Function model
loaded_model = mlflow.pyfunc.load_model('runs:/87d1368fa3c146f0a6eba66327d97112/iris_model')

# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

predictions = loaded_model.predict(X_test)

iris_feature_names = datasets.load_iris().feature_names
print(X)
result = pd.DataFrame(X_test, columns=iris_feature_names)
result["actual_class"] = y_test
result["predicted_class"] = predictions

print(result[:4])