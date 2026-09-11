def celsius_to_fahrenheit(c):
    result= round((c * 9/5) + 32, 1)
    return result

def fahrenheit_to_celsius(f):
    result= round((f - 32) * 5/9, 1)
    return result

gr=0
result_c=celsius_to_fahrenheit(gr)
print (f'{gr}°C = {result_c}°F')
gr=100
result_c=celsius_to_fahrenheit(gr)
print (f'{gr}°C = {result_c}°F')
gr=72
result_f=fahrenheit_to_celsius(gr)
print (f'{gr}°F = {result_f}°C')
