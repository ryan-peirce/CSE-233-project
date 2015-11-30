import cx_Freeze


cx_Freeze.setup(
    name = "Python Game" ,
    version = "0.1" ,
    description = "Ryan Peirce, CES-233" ,
    options= {"build_exe": {"packages":["pygame"],
                            "include_files" : [...]}},
    executables = [cx_Freeze.Executable("main.py")]
    )
