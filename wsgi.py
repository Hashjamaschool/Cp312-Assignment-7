import nbformat
from nbconvert import PythonExporter
import importlib.util
import sys

# Load the notebook
with open('main.ipynb', 'r', encoding='utf-8') as f:
    notebook = nbformat.read(f, as_version=4)

# Convert to Python
exporter = PythonExporter()
source, _ = exporter.from_notebook_node(notebook)

# Save to a temporary module
module_name = "notebook_app"
spec = importlib.util.spec_from_loader(module_name, loader=None)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
exec(source, module.__dict__)

# Get the server variable from the executed notebook
application = module.server