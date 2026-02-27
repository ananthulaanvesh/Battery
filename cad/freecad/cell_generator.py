import sys
import os

# Ensure FreeCAD modules are available
import FreeCAD as App
import Part


def create_cell(diameter, height, filename):

    doc = App.newDocument("BatteryCell")

    cell = doc.addObject("Part::Cylinder", "Cell")
    cell.Radius = diameter / 2
    cell.Height = height

    doc.recompute()

    # Ensure output directory exists
    output_path = os.path.abspath(filename)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    doc.saveAs(output_path)

    print(f"Cell saved at {output_path}")


if __name__ == "__main__":

    diameter = float(sys.argv[1])
    height = float(sys.argv[2])
    filename = sys.argv[3]

    create_cell(diameter, height, filename)