#!/usr/bin/python
# It is No.5 problem in HW 1

# initialization
SPHERE_t_calc = []
SPHERE_t_setup = []
CUBE_t_calc = []
CUBE_t_setup = []

# set the counter to count lines
counter = 1;   

# read all the t_setup & t_calc
for line in open('input.dat', 'r'):       
	if ord(list(line)[0]) == 32:
		item = str.split(line)
		if counter <= 14*5:
			SPHERE_t_setup.append(float(item[7]));
			SPHERE_t_calc.append(float(item[8]));
		else:
			CUBE_t_setup.append(float(item[7]));
			CUBE_t_calc.append(float(item[8]));
		counter = counter + 1

# calculation for t_calc
# ((t_calc for CUBE) - (t_calc for SPHERE))/(t_calc for SPHERE)
calc_taylor4 = []
calc_taylor6 = []
calc_taylor8 = []
calc_taylor10 = []
calc_taylor12 = []
for i in range(70):
	if i <= 13:
		calc_taylor4.append(int(round((CUBE_t_calc[i] - SPHERE_t_calc[i])*100/(SPHERE_t_calc[i]))));
	elif i <= 27:
		calc_taylor6.append(int(round((CUBE_t_calc[i] - SPHERE_t_calc[i])*100/(SPHERE_t_calc[i]))));
	elif i <= 41:
		calc_taylor8.append(int(round((CUBE_t_calc[i] - SPHERE_t_calc[i])*100/(SPHERE_t_calc[i]))));
	elif i <= 55:
		calc_taylor10.append(int(round((CUBE_t_calc[i] - SPHERE_t_calc[i])*100/(SPHERE_t_calc[i]))));
	elif i <= 69:
		calc_taylor12.append(int(round((CUBE_t_calc[i] - SPHERE_t_calc[i])*100/(SPHERE_t_calc[i]))));

# calculation for t_setup
# ((t_setup for CUBE) - (t_setup for SPHERE))/(t_calc for SPHERE)
setup_taylor4 = []
setup_taylor6 = []
setup_taylor8 = []
setup_taylor10 = []
setup_taylor12 = []
for i in range(70):
	if i <= 13:
		setup_taylor4.append(int(round((CUBE_t_setup[i] - SPHERE_t_setup[i])*100/(SPHERE_t_calc[i]))));
	elif i <= 27:
		setup_taylor6.append(int(round((CUBE_t_setup[i] - SPHERE_t_setup[i])*100/(SPHERE_t_calc[i]))));
	elif i <= 41:
		setup_taylor8.append(int(round((CUBE_t_setup[i] - SPHERE_t_setup[i])*100/(SPHERE_t_calc[i]))));
	elif i <= 55:
		setup_taylor10.append(int(round((CUBE_t_setup[i] - SPHERE_t_setup[i])*100/(SPHERE_t_calc[i]))));
	elif i <= 69:
		setup_taylor12.append(int(round((CUBE_t_setup[i] - SPHERE_t_setup[i])*100/(SPHERE_t_calc[i]))));

# output to file
f = open('Myoutput.dat', 'w+')
for i in range(14):
	f.write(str(calc_taylor4[i]).rjust(4))
	f.write(str(calc_taylor6[i]).rjust(5))
	f.write(str(calc_taylor8[i]).rjust(5))
	f.write(str(calc_taylor10[i]).rjust(5))
	f.write(str(calc_taylor12[i]).rjust(5))
	f.write('\n')
f.write('\n')
for i in range(14):
	f.write(str(setup_taylor4[i]).rjust(4))
	f.write(str(setup_taylor6[i]).rjust(5))
	f.write(str(setup_taylor8[i]).rjust(5))
	f.write(str(setup_taylor10[i]).rjust(5))
	f.write(str(setup_taylor12[i]).rjust(5))
	f.write('\n')
f.close()







