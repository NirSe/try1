
import load
import mlrun


def run_direct():

    load.load_data('Toyota')
    train.train_data()


def run_file():
    load_func = mlrun.code_to_function(name='load',
                                       project='tst',
                                       kind='job',
                                       image='mlrun/mlrun',
                                       filename='load.py'
                                        )
    load_func.run(local=False)

def run_mult_files():
    load_func = mlrun.new_function(name='load',
                                   project='tst',
                                   kind='job',
                                   image='mlrun/mlrun',
                                   command='load.py',
                                   source='git://github.com/NirSe/try1.git'
                                        )
    load_func.run(local=False)

#run_direct()
print ('start')
load.load_data()
print ('end')
