import nbformat
from nbconvert import PythonExporter
import sys
import os

with open('main.ipynb', 'r', encoding='utf-8') as f:
    notebook = nbformat.read(f, as_version=4)
exporter = PythonExporter()
source, _ = exporter.from_notebook_node(notebook)
source = source.replace('app = dash.Dash(__name__', 'app = dash.Dash("dashboard"')
namespace = {}
exec(source, namespace)
server = namespace.get('server')
if server is None and 'app' in namespace:
    server = namespace['app'].server
