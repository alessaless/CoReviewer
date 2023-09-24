<div align = "center">
<img src="https://i.imgur.com/SvIwWAN.png" alt="logo" width="400"/>
<h2>Università degli Studi di Salerno</h2>
Progetto Tesi Triennale </strong>
</div>

<br><br>

<h2>Introduzione</h2>

CoReviewer è un'estensione per Web Browser che permette di velocizzare il processo di Code Review, nello specifico il reviewer otterrà un summary delle modifiche effettuate alla codebase nell'ultimo commit.

<h2>Ambito del progetto</h2>

**CoReviewer** è un'estensione che permette di ottenere un breve summary delle modifiche fatte ad una codebase semplicemente mediante il link alla repository. La generazione di un summary permette al reviewer di velocizzare le attività di code review, avendo a disposizione l'elenco delle modifiche e degli effetti di queste sul codice che si sta analizzando. <br>
La generazione del summary è affidata al modello linguistico LLaMA 2 di Meta. Per l'ambito del progetto è stata utilizzata la versione a 7 miliardi di parametri.

<h2>Tecnlogie utilizzate</h2>

* **TypeScript + React JS**  - Per lo sviluppo dell'estensione         

* **Python 3 + Flask**       - Per la realizzazione del web server

* **LLaMA 2**                - [Repository ufficiale di LLaMA 2](https://github.com/facebookresearch/llama) [Repository per installazione su Apple Silicon](https://github.com/ggerganov/llama.cpp)
