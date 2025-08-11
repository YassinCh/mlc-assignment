# MLC Developer Assessment
## Prerequisites
Dit assessment vereist dat je de volgende componenten hebt geïnstalleerd op jouw machine:

Windows:
<ul>
    <li><a href="https://learn.microsoft.com/en-us/windows/wsl/install">WSL</a></li>
    <li><a href="https://docs.docker.com/desktop/install/windows-install/">Docker desktop</a></li>
</ul>
Linux:
<ul>
    <li><a href="https://docs.docker.com/engine/">Docker Engine</a></li>
</ul>
Mac OS:
<ul>
    <li><a href="https://docs.docker.com/desktop/install/mac-install/">Docker Desktop</a> of <a href="https://orbstack.dev/">Orbstack</a></li>
</ul>

## Getting started
Maakt een kopie van alle `.env.example` bestanden en hernoem deze naar `.env`. In deze bestanden staan de omgevingsvariabelen. Je hoeft niks extra hier aan toe te voegen.

Dit is een docker compose project, wat betekent dat je naast Docker niks extra hoeft te installeren.
In de root van het project staat een `docker-compose.yml`, navigeer naar de folder waar dit bestand in zit in je terminal, Je kan het project daarna starten door het volgende commando aan te roepen: 
> docker compose up -d 

Als je de logs wil inzien kan je dat doen met de volgende commando's
> docker compose logs

> docker compose logs \<service naam\>

> docker compose logs \<service naam\> -f