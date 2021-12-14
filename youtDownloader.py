
from pytube import YouTube
from pytube.cli import on_progress

# Control variable
control = 0

# Loop to download more than 1 video
while control == 0 :

    # user entry "URL"
    print("Digite ou cole a URL do video no youtube que deseja baixar:")
    link = input()

    # set the URL
    yt = YouTube(link, on_progress_callback = on_progress)

    # user interface
    print("Titulo = ", yt.title)
    print("Baixando...")

    # get the video with the best resolution available
    ys = yt.streams.get_highest_resolution()

    # download the video
    ys.download()

    # user interface to loop the program
    print("Download 100% concluído.")
    print("O seu arquivo encontra-se na mesma pasta deste programa.")
    print("Você deseja fazer mais um download?")
    print("sim/nao")

    # control variable
    choice = input()

    # it will finish the program if the entry above was different of "sim"
    if choice != "sim" :
        control = choice
        print("Obrigado por usar o YoutDownloader")