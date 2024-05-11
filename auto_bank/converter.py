import os, glob
BASE_DIR = os.path.abspath(os.curdir)
def converter():
    UI_DIR          = os.path.join(BASE_DIR, "design/ui")
    PY_DIR          = os.path.join(BASE_DIR, "design/py")

    if os.path.isdir(UI_DIR):
        UI_FILES = glob.glob(os.path.join(UI_DIR, "*.ui"))
        if isinstance(UI_FILES, list) and len(UI_FILES) > 0:
            for ui_file in UI_FILES:
                os.system("pyside6-uic.exe \"{inputFile}\" -o \"{outputFile}\"".format(inputFile=ui_file, outputFile=os.path.join(PY_DIR, "{basename}.py".format(basename=str(os.path.basename(ui_file)).split(".")[0]))))
    else:
        os.makedirs(UI_DIR)
        converter()

if __name__ == "__main__":
    try:
        converter()
    except Exception as Error:
        print(Error)