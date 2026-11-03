# On étudie un ballon lancé dans les airs avec une certaine vitesse initiale et un certain angle.
#On suppose que :
#- Le ballon est assimilé à un point matériel.
#- Les frottements de l'air sont négligés.
#- La seule force exercée sur le ballon dans les airs est son poids.
#- Le champ de pesanteur est uniforme.
#- Le ballon qui est le système est en chute libre
#Pour étudier le mouvement, on choisit un repère cartésien :
#- Origine : projection verticale du point de lancement sur le sol.


import math
import matplotlib.pyplot as plt
g = 9.81 # accéleration de pesanteur
dt = 0.1 # pas de temps en secondes

v0 = float(input("Entrez la vitesse initiale (m/s): "))
angle = float(input("Entrez l'angle de votre trajectoire (degré): "))
y0 = float(input("Entrez la hauteur initiale (m): "))
while y0 < 0:
    print("La hauteur initiale ne peut pas être négative. Veuillez entrer une valeur positive.")
    y0 = float(input("Entrez la hauteur initiale (m): "))
alpha = math.radians(angle)

ax = 0
ay = -(g)
az = 0

vx = v0*math.cos(alpha)
vy = v0*math.sin(alpha)
vz = 0

x0 = 0

z0 = 0

t = 0
y = y0

positions_x = []
positions_y = []
while y >= 0:
    
    vx = v0*math.cos(alpha)
    vy = -g*t+v0*math.sin(alpha)
    vz = 0

    x = v0*math.cos(alpha)*t+x0
    y = y0+v0*math.sin(alpha)*t+(1/2)*ay*t**2
    z = z0

    positions_x.append(x)
    positions_y.append(y)
    
    t = t + dt

plt.plot(positions_x, positions_y) #Trace une courbe à partir de coordonnées.
plt.xlabel("Distance effectuée par le ballon (m)")
plt.ylabel("Hauteur (m)")
plt.title("Lancer d'un ballon")
plt.grid()	
plt.show()


#hauteur maximale atteinte par le ballon
h_max = max(positions_y)
print(f"La hauteur maximale atteinte par le ballon est de environ {h_max:.2f} m.")

#temps de vol du ballon
t_vol = (v0*math.sin(alpha)+math.sqrt((v0*math.sin(alpha))**2+2*g*y0))/g
print(f"Le temps de vol du ballon est de environ {t_vol:.2f} s.")

#distance horizontale parcourue par le ballon
d_horizontale = positions_x[-1]     
