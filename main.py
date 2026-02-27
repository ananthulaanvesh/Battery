from cad.freecad.freecad_adapter import generate_cell

def main():

    diameter = 18
    height = 65

    output_file = "outputs/MyBatteryCell.FCStd"

    generate_cell(diameter, height, output_file)

if __name__ == "__main__":
    main()