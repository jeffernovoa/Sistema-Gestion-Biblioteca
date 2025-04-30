import pickle
import os

def save_data(data, filename):
    """Guarda los datos en un archivo usando pickle."""
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_data(filename):
    """Carga los datos de un archivo usando pickle. Si no existe, devuelve una lista vacía."""
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        # Crear un archivo vacío si no existe o está vacío
        with open(filename, 'wb') as f:
            pickle.dump([], f)
    with open(filename, 'rb') as f:
        return pickle.load(f)
