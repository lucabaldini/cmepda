class Clocking:
    """ Context manager for time measurment."""
    def __enter__(self):
        import time
        self.start_time = time.clock()
        self.elapsed_time = 0.
        return self # What you return here is assigned to 'as'
    
    def __exit__(self, exc_type, exc_value, traceback):
        """ Exit method. It gets notice of any exception raised in the body of the
        with block. If no exception is raised, the arguments are all set to None """
        import time
        self.elapsed_time = time.clock() - self.start_time # Update the time
        print('Exception type: {}, exception value: {}'.format(exc_type, exc_value))
        # If you do nothing, any exception will propagate to the rest of the code. 
        # To stop that from happening you have to return True -- though you should
        # do that only if it actually make sense to manage the exception here!
        if exc_type is not None:
            print('Exception handled succesfully.')
            return True
        
with Clocking() as clock:
    squares_list = [n**2 for n in range(1000000)]
    raise RuntimeError('Let\'s see what happens!')
print('With block runned in {:.8f} seconds'.format(clock.elapsed_time))
