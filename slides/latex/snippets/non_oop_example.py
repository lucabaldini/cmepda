# Non OOP example

def create_television(owner):
    television = {'model' : 'Sv32X-553T',
                  'owner' : owner}
    return television
                  
def print_info(television):
    message = 'This is television model {}, owned by {}'
    print(message.format(television.get('model'), television.get('owner')))

my_tv = create_television('Alberto')
print_info(my_tv)
