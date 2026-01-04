import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination


data = pd.read_csv('aa.csv')
model = BayesianNetwork([('rain', 'traffic')])


model.fit(data, estimator=MaximumLikelihoodEstimator)

print('Model ok?:', model.check_model())

inference_engine = VariableElimination(model)

result = inference_engine.query(variables=['traffic'], evidence={'rain': 1})

print("\nPrediction for Traffic given Rain=1:")
print(result)
