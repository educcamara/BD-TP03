import nbformat
from nbformat.v4 import new_notebook
import sys
import uuid

def load_notebook(path):
    """Carrega notebook usando nbformat, que lida corretamente com binários."""
    return nbformat.read(path, as_version=4)

def unique_cell_id():
    """Gera IDs únicos para evitar colisões ao juntar notebooks."""
    return str(uuid.uuid4())

def concatenate_notebooks(output_path, *input_paths):
    merged = new_notebook()
    merged_cells = []
    merged_metadata = {}

    for path in input_paths:
        nb = load_notebook(path)

        # Mescla metadados de forma simples
        merged_metadata.update(nb.get("metadata", {}))

        # Clona e ajusta cells
        for cell in nb.cells:
            new_cell = cell.copy()

            # Notebook antigos podem não ter ID; e IDs podem colidir
            new_cell["id"] = unique_cell_id()

            merged_cells.append(new_cell)

    merged["metadata"] = merged_metadata
    merged["cells"] = merged_cells

    nbformat.write(merged, output_path)
    print(f"Notebooks concatenados em: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Uso: python concat_notebooks.py output.ipynb input1.ipynb input2.ipynb [...])")
        sys.exit(1)

    output = sys.argv[1]
    inputs = sys.argv[2:]
    concatenate_notebooks(output, *inputs)