import os

print("Using pip or pip3")
value = "pip"
value = input()
if value in ["pip", "pip3"]:
    print("Installing Packages...")
else:
    print("Please enter a valid package installer")
    exit(0)

command = "{package} install {package_name}"

package_names = ["PyQt5", "numpy", "sympy", "matplotlib", "pyqtgraph", "PyOpenGL", "PyOpenGL_accelerate"]

for x in package_names:
    print("Installing {x}".format(x=x))
    os.system(command.format(package=value, package_name=x))
