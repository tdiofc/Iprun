import requests
from colorama import init, Fore


blanco = Fore.WHITE
celeste = Fore.CYAN
violeta = Fore.MAGENTA
amarillo = Fore.YELLOW

print(f"""
{celeste}


██╗██████╗░  ██████╗░██╗░░░██╗███╗░░██╗
██║██╔══██╗  ██╔══██╗██║░░░██║████╗░██║
██║██████╔╝  ██████╔╝██║░░░██║██╔██╗██║
██║██╔═══╝░  ██╔══██╗██║░░░██║██║╚████║
██║██║░░░░░  ██║░░██║╚██████╔╝██║░╚███║
╚═╝╚═╝░░░░░  ╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝
               {violeta}[{violeta}{celeste}+{celeste}{violeta}]{violeta}{blanco} Obtener informacion de una direccion ip""")




ip = input("Introduce una ip : ")
url = f"http://ip-api.com/{ip}"
respuesta = requests.get(url)

print(f"La Informacion de {ip} es: {respuesta.text}")
