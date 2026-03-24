def two_body_problem(t, mu, y):
    r = y[0:3]
    v = y[3:6]
    r_norm = (r[0]**2 + r[1]**2 + r[2]**2)**0.5
    a = (-mu/(r_norm**3)) * r
    return [v[0], v[1], v[2], a[0], a[1], a[2]]