def cleverStuff():
    try:
        pass
    # best opractice - handle specific errors first
    except FileExistsError as fe:
        print('the file already exists')
    except FileNotFoundError as fnf:
        print('the file cannot be found')
    except TimeoutError as toe:
        print('too slow')
    # ...then always end yup with a generic handler
    except Exception as err:
        print('something else went wrong')