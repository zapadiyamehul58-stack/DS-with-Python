from pgmpy.model import DiscreteBaysianNetwork
from pgmpy.factors.discrete import TablulerCPD
from pgmpy.interence import variableElimination
model=DiscreteBaysianNetwork([['rain','trafic']])
cpdrain=TablulerCPD('rain',2,[[0.7],[0.3]])
cpdtrafic=TablulerCPD(
                        variable='trafic',
                        variable_card=2,
                        values:[[0.6,0.7],
                                 [0.4,0.3]],
                        evidance=['rain'],
                        evidance_card=[2]
                        )
model.add_card(cpdrain,cpdtrafic)
print ('model ok?:',model.check_model())
inter=variableElimination(model)
res=inter.query(['trafic'],evidance={'rain':1})
print(res)
