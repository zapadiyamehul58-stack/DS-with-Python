from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([('rain', 'traffic')])

cpd_rain = TabularCPD(variable='rain', variable_card=2, values=[[0.7], [0.3]])

cpd_traffic = TabularCPD(
    variable='traffic',
    variable_card=2,
    values=[[0.6, 0.7], [0.4, 0.3]], 
    evidence=['rain'],
    evidence_card=[2]
)

model.add_cpds(cpd_rain, cpd_traffic)

print('model ok?:', model.check_model())

inference = VariableElimination(model)

res = inference.query(['traffic'], evidence={'rain': 1})

print(res)
