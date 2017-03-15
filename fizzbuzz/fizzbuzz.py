#def fizzbuzz(number):
#    <code here operates on number>
#    return <something>

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'fizzbuzz'
    elif number % 3 == 0: # % means remainder after dividing by the following number
        return 'fizz'
    elif number % 5 == 0: # remainder from number/5 is zero
        return 'buzz'
    else:
        return number
