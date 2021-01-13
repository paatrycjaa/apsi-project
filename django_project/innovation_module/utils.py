
def handle_exception(e):
    print('error occured when editing data')
    if hasattr(e, 'message'):
        print(e)
        print(e.message)
        return e.message
    else:
        print(e)
        return e.__str__()
