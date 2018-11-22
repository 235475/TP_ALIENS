
        
       responsable de classe :
        def  __init__ ( self , NoAllee , Nom ):
                auto .NoAllee = NoAllee
                auto .Nom = Nom
                
 
classe  Miam :
        def  __init__ ( self , NomAlien , Aliment ):
                auto .NomAlien = NomAlien
                auto .Aliment = Aliment
                
 
 agent de classe :
        def  __init__ ( self , Nom , Ville ):
                auto .Nom = Nom
                auto .Ville = Ville
                
 
classe  Gardien :
        def  __init__ ( self , Nom , NoCabine ):
                auto .Nom = Nom
                auto .NoCabine = NoCabine
                
 
classe  Alien :
        def  __init__ ( self , Nom , Sexe , Planete , NoCabine ):
                auto .Nom = Nom
                self .Sexe = Sexe
                auto .Planete = Planete
                auto .NoCabine = NoCabine
                
 
classe  Cabine :
        def  __init__ ( self , NoCabine , NoAllee ):
                auto .NoCabine = NoCabine
                auto .NoAllee = NoAllee
                
 
BaseResponsables = {Responsable ( ' 1 ' , ' Seldon ' ), Responsable ( ' 2 ' , ' Pelorat ' )}
 
BaseMiams = {Miam ( ' Zorglub ' , ' Bortsch ' ), Miam ( ' Blorx ' , ' Bortsch ' ), Miam ( ' Urxiz ' , ' Zoumise ' ), Miam ( ' Zbleurdite ' , ' Bortsch ' ), Miam ( ' Darneurane ' , ' Schwanstucke ' ), Miam ( ' Mulzo ' , 'Kashpir ' ), Miam (« Zzzzzz » , « Kashpir » ), Miam ( « Arghh » , « Zoumise » ), Miam ( « Joranum » , « Bortsch » )}
 
BaseAgents = {Agent ( ' Branno ' , ' Terminus ' ), Agent ( ' Darell ' , ' Terminus ' ), Agent ( ' Demerzel ' , ' Uco ' ), Agent ( ' Seldon ' , ' Terminus ' ), Agent ( ' Dornick ' , ' Kalgan ' ), agent ( ' Hardin ' , 'Terminus ' ), Agent (' Trevize ' , ' Hesperos ' ), agent ( ' Pelorat ' , ' Kalgan ' ), agent ( ' Riose ' , ' Terminus ' )}
 
BaseGardiens = {Gardien ( ' Branno ' , ' 1 ' ), Gardien ( ' Darell ' , ' 2 ' ), Gardien ( ' Demerzel ' , ' 3 ' ), Gardien ( ' Seldon ' , ' 4 ' ), Gardien ( ' Dornick ' , ' 5 ' ), Gardien ( ' Hardin ' , ' 6 ' ),Gardien ( 'Trevize ' , ' 7 ' ), Gardien ( ' Pelorat ' , ' 8 ' ), Gardien ( ' Riose ' , ' 9 ' )}
 
BaseAliens = {Alien ( ' Zorglub ' , ' M ' , ' Trantor ' , ' 1 ' ), Alien ( ' Blorx ' , ' M ' , ' Euterpe ' , ' 2 ' ), Alien ( ' Urxiz ' , ' M ' , ' Aurora ' , ' 3 ' ), Alien ( 'Zbleurdite ', ' F ' , ' Trantor ' , ' 4 ' ), Alien ( ' Darneurane ' , ' M ' , ' Trantor ' , ' 4 ' ), Alien ( ' Mulzo ' , ' M ' , ' Helicon ' , ' 6 ' ), Alien ( ' Zzzzzz ' , ' F ' ,' Aurora ', ' 7 ' ), Alien ( ' Arghh ' , ' M ' , ' Nexon ' , ' 8 ' ), Alien ( ' Joranum ' , ' F ' , ' Euterpe ' , ' 9 ' )}
