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
print("les triples sont:",triples)
###question 4
couples_aliens_allee={(alien.Nom, Cabine.NoAllee)for alien in BaseAliens for Cabine in BaseCabines if alien.NoCabine==Cabine.NoCabine}
print(couples_aliens_allee)
###question 5
allee2={(alien.Nom) for alien in BaseAliens for Cabine in BaseCabines if (Cabine.NoCabine==alien.NoCabine) and (Cabine.NoAllee=="2")}
print(allee2)
###question 6

###question 7
terminus_gardien={(alien.Nom)for alien in BaseAliens for Agent in BaseAgents for gardien  in Basegardiens  if (alien.NoCabine==gardien.NoCabine) and (gardien.Nom==Agent.Nom) and (Agent.Ville=="Terminus")}
print(terminus_gardien)
###question 8
F_bortsch={(gardien.Nom) for gardien in Basegardiens for alien in BaseAliens for Miam in BaseMiams if (gardien.NoCabine==alien.NoCabine) and (alien.Sexe=="F") and (Miam.NomAlien=="Bortsch")}
print(F_bortsch)
###question 9
terminus_F={(Cabine.NoCabine) for Cabine in BaseCabines for gardien in Basegardiens for Agent in BaseAgents for alien in BaseAliens if (gardien.NoCabine==alien.NoCabine) and (((gardien.Nom==Agent.Nom) and (Agent.Ville=="Terminus")) or (alien.Sexe=="F"))}
print(terminus_F)
