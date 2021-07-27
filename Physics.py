import math
import requests #test

def ask_variables():
    global angle, mass, distance, time, acceleration, force
    angle = float(input('Angle: '))
    mass = float(input('Mass (kg): '))
    distance = float(input('Ramp size (m): '))
    time = float(input('Time (s): '))
    force = float(input('Force (N): '))
    acceleration = distance/(time*time)

def ask_variables_repeat():
    global angle, mass, distance, time, acceleration, force
    angle = float(input('Angle: '))
    mass = float(input('Mass (kg): '))
    distance = float(input('Ramp size (m): '))

def calculation():
    global angle, mass, distance, time, acceleration, force
    print('\n')
    print('g = a × d / sin(θ) =', acceleration*distance/math.sin(math.radians(angle)))
    print('g = F / m =', force/mass)
    print('g = F / (m × sin(θ)) =', force/(mass*math.sin(math.radians(angle))))
    print('g = F × sin(θ) / m =', force*math.sin(math.radians(angle))/mass)
    print('g = F × s^2 / m^2 =', force*distnace*distance/(mass*mass))
    print('F = (0.5 × m × v^2) / s =', (0.5*mass*acceleration*time)/distance)
    print('Done')


repeat = True
while repeat == True:
    method = input('What method would you like?\n\n1 for Single Calculation\n2 for Repeatable Calculations\nSTOP to Stop\n\n')
    print('\n')
    if method == '1':
        ask_variables()
        calculation()
        repeat = False
        print('\n')

    if method == '2':
        repeatV2 = ''
        ask_variables_repeat()
        while repeatV2 != 'N':
            time = float(input('Time (s): '))
            force = float(input('Force (N): '))
            acceleration = distance/(time*time)
            calculation()
            repeatV2 = input('Repeat? (Y/N) ' )
            print('\n')

    if method == 'STOP':
        repeat = False



input('Press ENTER to Exit\n')