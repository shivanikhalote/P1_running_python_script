import arcpy

#setting the workspace environment
arcpy.env.workspace = r"C:\Users\shiva\Documents\programming_iii\P1_running_python_script\Practical_1_ProProject\Practical_1_ProProject\01_Running_Python_Scripts.gdb"

arcpy.analysis.Buffer("Wilson_Schools","wilson_school_buffer","500 meters")
print("process complete")