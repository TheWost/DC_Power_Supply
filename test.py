import pyvisa
print(pyvisa.__version__)
rm = pyvisa.ResourceManager()
print("Backend:", rm)
print("Resources:", rm.list_resources())
print("Resources (with ASRL query):", rm.list_resources("?*"))
