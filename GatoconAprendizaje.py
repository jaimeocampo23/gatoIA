#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 00:02:04 2020

@author: jaimecalderonocampo
Materia: Inteligencia Artificial
27 de Octubre del 2020
Gato con aprendizaje
"""
import numpy as np
import Win

play = 1
while play == 1:
    Gato = np.zeros((1,9))
    VD_s = np.array([100.08,100.04,100.07,100.03,100.09,100.02,100.06,100.01,100.05], ndmin = 2)
    Turno = int(input('TURNO: (0 reinicia) (1 maquina) (2 Humano): '))
    if Turno == 0:
        caso1 = Gato
        caso2 = Gato
        caso3 = Gato
        caso4 = Gato
        caso5 = Gato
        caso6 = Gato
        caso7 = Gato
        caso8 = Gato
        caso9 = Gato
        escoger1 = VD_s
        escoger2 = VD_s
        escoger3 = VD_s
        escoger4 = VD_s
        escoger5 = VD_s
        escoger6 = VD_s
        escoger7 = VD_s
        escoger8 = VD_s
        escoger9 = VD_s
        Empate = np.array([0])
    else:
        caso1 = np.load('caso1.npy')
        escoger1 = np.load('escoger1.npy')
       
        caso2 = np.load('caso2.npy')
        escoger2 = np.load('escoger2.npy')
       
        caso3 = np.load('caso3.npy')
        escoger3 = np.load('escoger3.npy')
       
        caso4 = np.load('caso4.npy')
        escoger4 = np.load('escoger4.npy')
       
        caso5 = np.load('caso5.npy')
        escoger5 = np.load('escoger5.npy')
       
        caso6 = np.load('caso6.npy')
        escoger6 = np.load('escoger6.npy')
       
        caso7 = np.load('caso7.npy')
        escoger7 = np.load('escoger7.npy')
       
        caso8 = np.load('caso8.npy')
        escoger8 = np.load('escoger8.npy')
       
        caso9 = np.load('caso9.npy')
        escoger9 = np.load('escoger9.npy')
        
        Empate = np.load('Empate.npy') 
        
        # Tiro 1
        tiro = 1
        Val = Gato < 1
        #Val = Val.astype(np.int)
        L = np.shape(caso1)
        capa1 = 0
        sh = 0
        while sh == 0:
            if capa1 <= L[0]:       
                cs = int(np.array_equal(Gato, np.array(caso1[capa1, :], ndmin = 2)))
                if cs == 1:
                    sh = 1
            else:
                caso1 = np.row_stack((caso1, Gato))
                escoger1 = np.row_stack((escoger1, VD_s))
                sh = 1
                   
        if Turno == 1:
            np.disp('Tiro de la Maquina')
            pos1 = np.argmax(escoger1[capa1, :] * Val)
            Gato[0, pos1] = 1
            Turno = 2
        else:          
            tablero = np.array([Gato[0,0:3],Gato[0,3:6],Gato[0,6:9]])
            pos1 = int(input('Ingresa una posicion (0 - 8) '))
            while Val[0, pos1] <= 0:
                np.disp('Casilla Ocupada')
                pos1 = int(input('Ingresa una posicion (0 - 8) '))
              
            Gato[0, pos1] = 2
            Turno = 1 
         
            
        capa1 = capa1 + 1
        tablero = np.array([Gato[0,0:3],Gato[0,3:6],Gato[0,6:9]])
        np.disp(tablero)

      
        # Tiro 2
        tiro = 2
        Val = (Gato < 1)
        L = np.shape(caso2)
        capa2 = 0 
        sh = 0
        while sh == 0:
            if (capa2 <= L[0]):
                cs = int(np.array_equal(Gato, np.array(caso2[capa2, :], ndmin = 2)))
                if cs == 1:
                    sh = 1
                else:
                    caso2 = np.row_stack((caso2, Gato))
                    escoger2 = np.row_stack((escoger2, VD_s))
                    sh = 1
                
        if Turno == 1:
            np.disp('Tiro de la maquina')
            pos2 = np.argmax(escoger2[capa2, :] * Val)
            Gato[0, pos2] = 1
            Turno = 2
        else:
            pos2 = int(input('Ingres una posicion (0 - 8)'))
            while Val[0, pos2] <= 0:
                pos2 = int(input('ingresa una posicion (0 - 8)'))
            Gato[0,pos2] = 2
            Turno = 1
            
        
        capa2 = capa2 + 1
        tablero = np.array([Gato[0,0:3],Gato[0,3:6],Gato[0,6:9]])
        np.disp(tablero)
        
        
        
        # Tiro 3 
        tiro = 3
        Val = (Gato < 1)
        #Val = Val.astype(np.int)
        L = np.shape(caso3)
        capa3 = 0
        sh = 0
        while sh == 0:
            if capa3 <= L[0]:
                cs = int(np.array_equal(Gato, np.array(caso3[capa3, :], ndmin = 2)))
                if cs == 1:
                    sh = 1
                    
                else:
                    caso3 = np.row_stack((caso3, Gato))
                    escoger3 = np.row_stack((escoger3, VD_s))
                    sh = 1
                
        if Turno == 1:
            np.disp('Tiro de la Maquina')
            pos3 = np.argmax(escoger3[capa3, :] * Val)
            Gato[0, pos3] = 1
            Turno = 2
        else:
            pos3 = int(input('Ingresa posicion (0 - 8)'))
            while Val[0, pos3] <= 0:
                pos3 = int(input('Ingresa posicion (0 - 8)'))
            Gato[0, pos3] = 2
            Turno = 1
        
        capa3 = capa3 + 1
        tablero = np.array([Gato[0,0:3],Gato[0,3:6],Gato[0,6:9]])
        np.disp(tablero)
        
        # Tiro 4 
        tiro = 4 
        Val = (Gato < 1)
        #Val = Val.astype(np.int)
        L = np.shape(caso4)
        capa4 = 0
        sh = 0
        while sh == 0:
            if capa4 <= L[0]:
                cs = int(np.array_equal(Gato, np.array(caso4[capa4, :], ndmin = 2)))
                if cs == 1:
                    sh = 1
                    
                else:
                    caso4 = np.row_stack((caso4, Gato))
                    esoger4 = np.row_stack((escoger4, VD_s))
                    sh = 1
                
        if Turno == 1 :
            np.disp('Tiro de la maquina')
            pos4 = np.argmax(escoger4[capa4, : ] * Val)
            Gato[0, pos4] = 1
            Turno = 2
        else:
            pos4 = int(input('Ingresa una posicion (0 - 8)'))
            while Val[0, pos4] <= 0:
                pos4 = int(input('ingresa una posicion (0 - 8)'))
            Gato[0, pos4] = 2
            Turno = 1
    

        capa4 = capa4 + 1
        tablero = np.array([Gato[0,0:3],Gato[0,3:6],Gato[0,6:9]])
        np.disp(tablero)
        
        
        # Tiro 5
        tiro = 5
        Val = (Gato < 1)
        #Val = Val.astype(np.int)
        L = np.shape(caso5)
        capa5 = 0
        sh = 0
        while sh == 0:
            if capa5 <= L[0]:
                cs = int(np.array_equal(Gato, np.array(caso5[capa5, :], ndmin = 2)))
                if cs == 1:
                    sh = 1
                    
                else:
                    caso5 = np.row_stack((caso5, Gato))
                    escoger5 = np.row_stack((escoger5, VD_s))
                    sh = 1
                
        if Turno == 1:
            np.disp('Tiro de la maquina')
            pos5 = np.argmax(escoger5[capa5, :] * Val)
            Gato[0, pos5] = 1
            Turno = 2
        else:
            pos5 = int(input('ingresa una posicion (0 - 8)'))
            while Val[0, pos5] <= 0:
                pos5 = int(input('ingresa una posicion (0 - 8)'))
            
            Gato[0, pos5] = 2
            Turno = 1
            
        capa5 = capa5 + 1
        tablero = np.array([Gato[0,0:3],Gato[0,3:6],Gato[0,6:9]])
        np.disp(tablero)
        VWIN = Win.VWIM(Gato)
        
        if VWIN == 0:
            # Tiro 6
            tiro = 6
            Val = (Gato < 1)
            #Val = Val.astype(np.int)
            L = np.shape(caso6)
            capa6 = 0
            sh = 0
            while sh == 0:
                if capa6 <= L[0]:
                    cs = int(np.array_equal(Gato, np.array(caso6[capa6, :], ndmin = 2)))
                    if cs == 1:
                        sh = 1
                        
                    else:
                        caso6 = np.row_stack((caso6, Gato))
                        escoger6 = np.row_stack((escoger6, VD_s))
                        sh = 1
                    
            if Turno == 1:
                np.disp('Tiro de la maquina')
                pos6 = np.argmax(escoger6[capa6, :] * Val)
                Gato[0, pos6] = 1
                Turno = 2
            else:
                pos6 = int(input('ingresa posicion (0 - 8)'))
                while Val[0, pos6] <= 0:
                    pos6 = int(input('ingresa posicion (0 - 8)'))
                    
                Gato[0, pos6] = 2
                Turno = 1
       
            capa6 = capa6 + 1
            tablero = np.array([Gato[0,0:3],Gato[0,3:6],Gato[0,6:9]])
            np.disp(tablero)
            VWIN = Win.VWIM(Gato)
                
        
        if VWIN == 0:
            # Tiro 7
            tiro = 7
            Val = (Gato < 1)
            #Val = Val.astype(np.int)
            L = np.shape(caso7)
            capa7 = 0
            sh = 0
            while sh == 0:
                if capa7 <= L[0]:
                    cs = int(np.array_equal(Gato, np.array(caso7[capa7, :], ndmin = 2)))
                    if cs == 1:
                        sh = 1
                        
                    else:
                        caso7 = np.row_stack((caso7, Gato))
                        escoger7 = np.row_stack((escoger6, VD_s))
                        sh = 1
                    
            if Turno == 1:
                np.disp('Tiro de la maquina')
                pos7 = np.argmax(escoger7[capa7, :] * Val)
                Gato[0, pos7] = 1
                Turno = 2
            else:
                pos7 = int(input('ingresa posicion (0 - 8)'))
                while Val[0, pos7] <= 0:
                    pos7 = int(input('ingresa posicion (0 - 8)'))
                    
                Gato[0, pos7] = 2
                Turno = 1
            
            capa7 = capa7 + 1
            tablero = np.array([Gato[0,0:3],Gato[0,3:6],Gato[0,6:9]]) 
            np.disp(tablero)
            VWIN = Win.VWIM(Gato)
        
        
        if VWIN == 0:
            # Tiro 8
            tiro = 8
            Val = (Gato < 1)
            #Val = Val.astype(np.int)
            L = np.shape(caso8)
            capa8 = 0
            sh = 0
            while sh == 0:
                if capa8 <= L[0]:
                    cs = int(np.array_equal(Gato, np.array(caso8[capa8, :], ndmin = 2)))
                    if cs == 1:
                        sh = 1
                        
                    else:
                        caso8 = np.row_stack((caso8, Gato))
                        escoger8 = np.row_stack((escoger8, VD_s))
                        sh = 1
                    
            if Turno == 1:
                np.disp('Tiro de la maquina')
                pos8 = np.argmax(escoger8[capa8, :] * Val)
                Gato[0, pos8] = 1
                Turno = 2
            else:
                pos8 = int(input('ingresa posicion (0 - 8)'))
                while Val[0, pos8] <= 0:
                    pos8 = int(input('ingresa posicion (0 - 8)'))
                    
                Gato[0, pos8] = 2
                Turno = 1
              
            capa8 = capa8 + 1
            tablero = np.array([Gato[0,0:3],Gato[0,3:6],Gato[0,6:9]]) 
            np.disp(tablero)
            VWIN = Win.VWIM(Gato)
        
        
        if VWIN == 0:
            # Tiro 9
            tiro = 9
            Val = (Gato < 1)
            #Val = Val.astype(np.int)
            L = np.shape(caso9)
            capa9 = 0
            sh = 0
            while sh == 0:
                if capa9 <= L[0]:
                    cs = int(np.array_equal(Gato, np.array(caso9[capa9, :], ndmin = 2)))
                    if cs == 1:
                        sh = 1
                        
                    else:
                        caso9 = np.row_stack((caso9, Gato))
                        escoger9 = np.row_stack((escoger9, VD_s))
                        sh = 1
                    
            if Turno == 1:
                np.disp('Tiro de la maquina')
                pos9 = np.argmax(escoger9[capa9, :] * Val)
                Gato[0, pos9] = 1
                Turno = 2
            else:
                pos9 = int(input('ingresa posicion (0 - 8)'))
                while Val[0, pos9] <= 0:
                    pos9 = int(input('ingresa posicion (0 - 8)'))
                    
                Gato[0, pos9] = 2
                Turno = 1
              
            capa9 = capa9 + 1
            tablero = np.array([Gato[0,0:3],Gato[0,3:6],Gato[0,6:9]]) 
            np.disp(tablero)
            VWIN = Win.VWIM(Gato)

    
        if VWIN == 1:
            np.disp('Gana Maquina')
        elif VWIN == 2:
            np.disp('Gana Humano')
        else:
            np.disp('empate')
            Empate[capa9] = Empate[capa9] + 1
        
        
        ## Aprendizaje
        
        if VWIN == 0 and int(Empate[capa9]) <= 5:
            escoger1[capa1 - 1, pos1] = escoger1[capa1 - 1, pos1] + 0.0025
            escoger2[capa2 - 1, pos2] = escoger2[capa2 - 1, pos2] + 0.0025
            escoger3[capa3 - 1, pos3] = escoger3[capa3 - 1, pos3] + 0.0025
            escoger4[capa4 - 1, pos4] = escoger4[capa4 - 1, pos4] + 0.0025
            escoger5[capa5 - 1, pos5] = escoger5[capa5 - 1, pos5] + 0.0025
            if tiro >= 6:
                escoger6[capa6 - 1, pos6] = escoger6[capa6 -1, pos6] + 0.0025
                if tiro >= 7:
                    escoger7[capa7 -1, pos7] = escoger7[capa7 - 1, pos7] + 0.0025
                    if tiro >= 8 :
                        escoger8[capa8 - 1, pos8] = escoger8[capa8 - 1, pos8] + 0.0025
                        if tiro >= 9:
                            escoger9[capa9 - 1, pos9] = escoger9[capa9 - 1, pos9] + 0.0025
        
        elif VWIN == 0 and int(Empate[capa9]) > 5:
            escoger1[capa1 - 1, pos1] = escoger1[capa1 - 1, pos1] - int(0.01 / Empate[capa9])
            escoger2[capa2 - 1, pos2] = escoger2[capa2 - 1, pos2] - int(0.01 / Empate[capa9])
            escoger3[capa3 - 1, pos3] = escoger3[capa3 - 1, pos3] - int(0.04 / Empate[capa9])
            escoger4[capa4 - 1, pos4] = escoger4[capa4 - 1, pos4] - int(0.05 / Empate[capa9])
            escoger5[capa5 - 1, pos5] = escoger5[capa5 - 1, pos5] - int(0.06 / Empate[capa9])
            if tiro >= 6 :
                escoger6[capa6 - 1, pos6] = escoger6[capa6 - 1, pos6] - int(0.06 / Empate[capa9])
                if tiro >= 7:
                    escoger7[capa7 - 1, pos7] = escoger7[capa7 - 1, pos7] - int(0.05 / Empate[capa9])
                    if tiro >= 8 :
                        escoger8[capa8 - 1, pos8] = escoger8[capa8 - 1, pos8] - int(0.04 / Empate[capa9])
                        if tiro >= 9:
                            escoger9[capa9 - 1, pos9] = escoger9[capa9 - 1, pos9] - int(0.0025 / Empate[capa9])
                            
        elif tiro % 2 == 1 :
            escoger1[capa1 - 1, pos1] = escoger1[capa1 - 1, pos1] + 0.01
            escoger2[capa2 - 1, pos2] = escoger2[capa2 - 1, pos2] - 0.01
            escoger3[capa3 - 1, pos3] = escoger3[capa3 - 1, pos3] + 0.04
            escoger4[capa4 - 1, pos4] = escoger4[capa4 - 1, pos4] - 0.05
            escoger5[capa5 - 1, pos5] = escoger5[capa5 - 1, pos5] + 0.06
            if tiro >= 6 :
                escoger6[capa6 - 1, pos6] = escoger6[capa6 - 1, pos6] - 0.06
                if tiro >= 7:
                    escoger7[capa7 - 1, pos7] = escoger7[capa7 - 1, pos7] + 0.05
                    if tiro >= 8:
                        escoger8[capa8 - 1, pos8] = escoger8[capa8 - 1, pos8] - 0.04
                        if tiro >= 9:
                            escoger9[capa9 - 1, pos9] = escoger9[capa9 - 1, pos9] + 0.025
                            
                            
        
        elif tiro % 2 == 0 :
            escoger1[capa1 - 1, pos1] = escoger1[capa1 - 1, pos1] - 0.01
            escoger2[capa2 - 1, pos2] = escoger2[capa2 - 1, pos2] + 0.01
            escoger3[capa3 - 1, pos3] = escoger3[capa3 - 1, pos3] - 0.04
            escoger4[capa4 - 1, pos4] = escoger4[capa4 - 1, pos4] + 0.05
            escoger5[capa5 - 1, pos5] = escoger5[capa5 - 1, pos5] - 0.06
            if tiro >= 6 :
                escoger6[capa6 - 1, pos6] = escoger6[capa6 - 1, pos6] + 0.06
                if tiro >= 7:
                    escoger7[capa7 - 1, pos7] = escoger7[capa7 - 1, pos7] - 0.05
                    if tiro >= 8:
                        escoger8[capa8 - 1, pos8] = escoger8[capa8 - 1, pos8] + 0.04
                        if tiro >= 9:
                            escoger9[capa9 - 1, pos9] = escoger9[capa9 - 1, pos9] - 0.025
                        


    
                        
    np.save('caso1', caso1)
    np.save('escoger1', escoger1)
    
    np.save('caso2', caso2)
    np.save('escoger2', escoger2)
    
    np.save('caso3', caso3)
    np.save('escoger3', escoger3)
    
    np.save('caso4', caso4)
    np.save('escoger4', escoger4)

    np.save('caso5', caso5)
    np.save('escoger5', escoger5)

    np.save('caso6', caso6)
    np.save('escoger6', escoger6)

    np.save('caso7', caso7)
    np.save('escoger7', escoger7)

    np.save('caso8', caso8)
    np.save('escoger8', escoger8)

    np.save('caso9', caso9)
    np.save('escoger9', escoger9)    
    
    
    np.save('Empate', Empate)
    play = int(input('Quieres jugar de nuevo? (Si = 1)'))
    
                      


        


        
                
            
      
            
            
                   
           
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        