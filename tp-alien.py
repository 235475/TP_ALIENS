#-*- coding: utf-8 -*-
from Mabase_MIB import *
###question 1
les_gardiens={gardien.Nom for gardien in Basegardiens}
print("les gardiens sont:", les_gardiens)
###question 2
les_villes_agents={agent.Ville for agent in BaseAgents}
print("les agents vivent dans les villes de ",les_villes_agents)
###question 3
triples={(alien.NoCabine, alien.Nom, gardien.Nom) for alien in BaseAliens for gardien in Basegardiens if gardien.NoCabine== alien.NoCabine}
print(triples)
###question 4
couples_aliens_allee={(alien.Nom, Cabine.NoAllee)for alien in BaseAliens for Cabine in BaseCabines if alien.NoCabine==Cabine.NoCabine}
print("les couples aliens/allees sont ",couples_aliens_allee)
###question 5
allee2={(alien.Nom) for alien in BaseAliens for Cabine in BaseCabines if (Cabine.NoCabine==alien.NoCabine) and (Cabine.NoAllee=="2")}
print( "les cabines de l'allee 2 sont ", allee2)
#####question 6
planete_pair={(alien.Planete)for alien in BaseAliens if alien.NoCabine=="2" or alien.NoCabine=="4" or alien.NoCabine=="6" or alien.NoCabine=="8"}
print("les planete des aliens qui sont dans des cabines a No pairs sont ",planete_pair)
###question 7
terminus_gardien={(alien.Nom)for alien in BaseAliens for Agent in BaseAgents for gardien  in Basegardiens  if (alien.NoCabine==gardien.NoCabine) and (gardien.Nom==Agent.Nom) and (Agent.Ville=="Terminus")}
print("les gardiens venant de terminus sont ",terminus_gardien)
###question 8
F_bortsch={(gardien.Nom) for gardien in Basegardiens for alien in BaseAliens for Miam in BaseMiams if (gardien.NoCabine==alien.NoCabine) and (alien.Sexe=="F") and (alien.Nom==Miam.NomAlien) and (Miam.Aliment=="Bortsch")}
print(F_bortsch)
###question 9
terminus_F={(Cabine.NoCabine) for Cabine in BaseCabines for gardien in Basegardiens for Agent in BaseAgents for alien in BaseAliens if ((alien.NoCabine==gardien.NoCabine) and ((gardien.Nom==Agent.Nom) and (Agent.Ville=="Terminus"))) or (alien.Sexe=="F")}
print(terminus_F)
###question 10
nom_aliens_miam={(True or False)for Miam in BaseMiams for  gardien in Basegardiens for alien in BaseAliens if (gardien.Nom[0]==Miam.Aliment[0]) and (gardien.NoCabine==alien.NoCabine)}
print(nom_aliens_miam)
###question 11
euterpe_alien={(True or False) for alien in BaseAliens if alien.Planete=="Euterpe"}
print(euterpe_alien)
###question 12
nom_alien_x={(True or False)for alien in BaseAliens   for i in range(len(alien.Nom)) if (all((alien.Nom[i]=="x") or (alien.Nom[i]=="X")))}
print(nom_alien_x)
###question 13
x_terminus={(True or False) for alien in BaseAliens for gardien in Basegardiens for Agent in BaseAgents for j in range(len(alien.Nom)) if ((alien.Nom[j]=="x") or (alien.Nom[j]=="X")) and ((alien.NoCabine==gardien.NoCabine) and (gardien.Nom==Agent.Nom) and (Agent.Ville=="Terminus"))}
print(x_terminus)
###question 14
bortsch_or_terminus={(True or False)for alien in BaseAliens for gardien in Basegardiens for Agent in BaseAgents for Miam in BaseMiams if (alien.Sexe=="M") and (alien.Planete=="Trantor") and ((Miam.NomAlien==alien.Nom) and (Miam.Aliment=="Bortsch")) or ((alien.NoCabine==gardien.NoCabine) and (gardien.Nom==Agent.Nom) and (Agent.Ville=="Terminus"))}
print("q 14 ",bortsch_or_terminus)
