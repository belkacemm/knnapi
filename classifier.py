from sklearn.neighbors import KNeighborsClassifier

from fastapi import FastAPI
app = FastAPI()

@app.get("/knn/create")
def create_classifier(neighbors: int, p: int):
    if (p==1):
        return {'distance' : 'Manhattan', 'classifier' : KNeighborsClassifier(n_neighbors=neighbors, metric='minkowski', p=1)}
    else:
        if (p==2):
            return {'distance' : 'Euclidean', 'classifier' : KNeighborsClassifier(n_neighbors=neighbors, metric='minkowski', p=2)}
        else:
            return {'distance' : 'Minkowski', 'classifier' : KNeighborsClassifier(n_neighbors=neighbors)}