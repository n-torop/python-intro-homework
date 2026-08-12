def celsius_to_fahrenheit(c):
    result= round((c * 9/5) + 32, 1)
    ans= f'{c}°C = {result}°F'

    return ans

def fahrenheit_to_celsius(f):
    result= round((f - 32) * 5/9, 1)
    ans= f'{f}°F = {result}°C'
    return ans

def printing (gr, res):
    
    print (f'{gr}°C = {celsius_to_fahrenheit(res)}°F')
gr=0
print (celsius_to_fahrenheit(gr))
gr=100
print (celsius_to_fahrenheit(gr))
gr=72
print (fahrenheit_to_celsius(gr))
