from easysnmp import *
import subprocess

def main():

        choose = input("""
Main menu

        1: Conectar ao servidor de Musica
        2: Sair
                
Write the option: """)

        if choose == 1 :
                print('')
                print("Digite o IP ou nome do servidor:")
                print('')
                ip = raw_input()
                vlc = "/usr/bin/vlc"
                session = Session(hostname=ip, community='public', version=2)

                musica5=".1.3.6.1.2.1.25.3.8.1.3.1.1.1.1.1"
                musica55 = "/home/motta/Documents/musicas/anos90/Hiphop90/artista5/musica5.mp3"

                musica6=".1.3.6.1.2.1.25.3.8.1.3.1.1.2.1.1"
                musica66 = "/home/motta/Documents/musicas/anos90/Rock90/artista6/musica6.mp3"

                musica3=".1.3.6.1.2.1.25.3.8.1.3.1.2.1.1.1"
                musica33 = "/home/motta/Documents/musicas/anos2000/Hiphop2000/artista3/musica3.mp3"

                musica4=".1.3.6.1.2.1.25.3.8.1.3.1.2.2.1.1"
                musica44 = "/home/motta/Documents/musicas/anos2000/Rock2000/artista4/musica4.mp3"
                
                print('')
                print("Digite o opcao do Ano:")
                
                choose = input("""
        Main menu

                1: 90s
                2: 2000
         
        Write the option: """)
                if choose == 1 :
                        print("Digite o opcao do Estilo:")
                        choose = input("""

                Main menu

                        1: HipHop
                        2: Rock
         
                Write the option: """)
                        if choose == 1 :
                                print("Digite o opcao do Artista:")
                                choose = input("""
                        Main menu

                                1: Artista1
                                2: Naotem
                
                        Write the option: """)
                                if choose == 1 :
                                        print("Digite o opcao da Musica:")
                                        choose = input("""
                                Main menu

                                        1: Musica
                                        2: Naotem
                                
                                Write the option: """)

                                        if choose == 1 :
                                                print('')
                                                musica11 = session.get([musica5])
                                                print(musica11)
                                                subprocess.call([vlc, musica55])
                        if choose == 2 :
                                print("Digite o opcao do Artista:")
                                choose = input("""
                        Main menu

                                1: Artista1
                                2: Naotem
                
                        Write the option: """)
                                if choose == 1 :
                                        print("Digite o opcao da Musica:")
                                        choose = input("""
                                Main menu

                                        1: Musica
                                        2: Naotem
                                
                                Write the option: """)

                                        if choose == 1 :
                                                print('')
                                                musica11 = session.get([musica6])
                                                print(musica11)
                                                subprocess.call([vlc, musica66])

                if choose == 2 :
                        print("Digite o opcao do Estilo:")
                        choose = input("""

                Main menu

                        1: HipHop
                        2: Rock
         
                Write the option: """)
                        if choose == 1 :
                                print("Digite o opcao do Artista:")
                                choose = input("""
                        Main menu

                                1: Artista1
                                2: Naotem
                
                        Write the option: """)
                                if choose == 1 :
                                        print("Digite o opcao da Musica:")
                                        choose = input("""
                                Main menu

                                        1: Musica
                                        2: Naotem
                                
                                Write the option: """)

                                        if choose == 1 :
                                                print('')
                                                musica11 = session.get([musica3])
                                                print(musica11)
                                                subprocess.call([vlc, musica33])
                        if choose == 2 :
                                print("Digite o opcao do Artista:")
                                choose = input("""
                        Main menu

                                1: Artista1
                                2: Naotem
                
                        Write the option: """)
                                if choose == 1 :
                                        print("Digite o opcao da Musica:")
                                        choose = input("""
                                Main menu

                                        1: Musica
                                        2: Naotem
                                
                                Write the option: """)

                                        if choose == 1 :
                                                print('')
                                                musica11 = session.get([musica4])
                                                print(musica11)
                                                subprocess.call([vlc, musica44])


        elif choose == 2 :
                print('\nFechando!!!!!!')
        else:
                print('\nERROR \n')

if __name__== "__main__":
    main()
