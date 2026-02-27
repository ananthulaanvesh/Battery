import subprocess
import os

FREECAD_CMD_PATH = r"C:\Program Files\FreeCAD 1.0\bin\FreeCADCmd.exe"


def generate_cell(diameter, height, output_file):
    
    script_content = f"""
import FreeCAD
import Part

doc = FreeCAD.newDocument("Cell")

radius = {diameter} / 2
height = {height}

cylinder = Part.makeCylinder(radius, height)
part_obj = doc.addObject("Part::Feature", "Cell")
part_obj.Shape = cylinder

doc.recompute()
doc.saveAs(r"{output_file}")

FreeCAD.closeDocument("Cell")
"""

    temp_script = "temp_freecad_script.py"

    with open(temp_script, "w") as f:
        f.write(script_content)

    subprocess.run([FREECAD_CMD_PATH, temp_script], check=True)

    os.remove(temp_script)