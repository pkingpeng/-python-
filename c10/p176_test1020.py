import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('../resource/txt/errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    print('The traceback info was written to errorInfo.txt')
    errorFile.close()

    message = open('../resource/txt/errorInfo.txt').read()
    print('\nThe message are: \n\n' + message)

