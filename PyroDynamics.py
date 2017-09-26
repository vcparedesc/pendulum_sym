class PyroDynamics:
	M = 1
	l = 1
	m = 1
	I = 1
	g = 1
	
	def get_fx(x):
	x1 = x[0]
	x2 = x[1]
	xd1 = x[2]
	xd2 = x[3]
	
	return np.matrix([[xd1], 
	[xd2], 
	[1.0*l*m*(I*xd2**2 + g*l*m*cos(x2) + l**2*m*xd2**2)*sin(x2)/(I*M + I*m + M*l**2*m + l**2*m**2*sin(x2)**2)], 
	[1.0*l*m*(g*(1.0*M + m) + l*m*xd2**2*cos(x2))*sin(x2)/(l**2*m**2*cos(x2)**2 - (I + l**2*m)*(1.0*M + m))]])

	def get_gx(x):
	x1 = x[0]
	x2 = x[1]
	xd1 = x[2]
	xd2 = x[3]
	
	return np.matrix([[0, 0], 
	[0, 0], 
	[1.0*l**2*m**2*cos(x2)**2/((1.0*M + m)*(-l**2*m**2*cos(x2)**2 + (I + l**2*m)*(1.0*M + m))) + 1/(1.0*M + m), -1.0*l*m*cos(x2)/(-l**2*m**2*cos(x2)**2 + (I + l**2*m)*(1.0*M + m))], 
	[-1.0*l*m*cos(x2)/(-l**2*m**2*cos(x2)**2 + (I + l**2*m)*(1.0*M + m)), 1.0*(1.0*M + m)/(-l**2*m**2*cos(x2)**2 + (I + l**2*m)*(1.0*M + m))]])
