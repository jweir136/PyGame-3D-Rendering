import display

if __name__ == "__main__":
    window = display.Display(1000, 1000)
    window._addWireframe("cube", "examples/big_cube.json")
    window.run()