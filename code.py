


# DT Cross-validation --------- Behzad Amanpour -------------------------

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

model = DecisionTreeClassifier()
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy') # scoring='recall' 
print("cross-val accuracy:", np.mean(scores))




# Regularization (Pruning) ---- Behzad Amanpour ------------------------

model = DecisionTreeClassifier()
model.fit(X, y)
model.get_depth()
model.get_n_leaves()

model = DecisionTreeClassifier(max_depth=3, min_samples_leaf=2, max_leaf_nodes=10)
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print("cross-val accuracy:", np.mean(scores))




# Grid Search ----------------  Behzad Amanpour ------------------------- 

from sklearn.model_selection import GridSearchCV
param_grid = {
    'max_depth': [2, 3, 5],
    'min_samples_leaf': [1, 2, 5],
    'max_leaf_nodes': [5, 10, 20]}
model = DecisionTreeClassifier()
gs = GridSearchCV(model, param_grid, scoring='accuracy', cv=5)
gs.fit(X, y)
print("best params:", gs.best_params_)
print("best score:", gs.best_score_)