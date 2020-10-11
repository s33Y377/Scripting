import traceback

try:
    raise Exception("This is the error message.")
except BaseException as es:
    errorFile = open("errorInfo.txt", "w")
    errorFile.write(traceback.format_exc())
    errorFile.write(str(es))
    errorFile.close()
    print("The traceback info was written to errorInfo.txt.")
