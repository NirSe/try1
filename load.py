def load_data(car: str = 'Toyota'):
    print ('loading')
    my_file_handle = open("~/test.txt", 'w')
    my_file_handle.write(car)

