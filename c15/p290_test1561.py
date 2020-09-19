import threading

threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Forgs'], kwargs={'sep': ' & '})
threadObj.start()

"""
Cats & Dogs & Forgs
"""
