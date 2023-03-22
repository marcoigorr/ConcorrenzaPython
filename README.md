# ConcorrenzaPython

Esercizi in python per TPSIT | Gestione concorrenza thread

### ReadersWriters
Il primo è conosciuto come problema di lettori e scrittori. Supponete che una risorsa (ad esempio, un database) deve essere condivisa tra diversi processi concorrenti. Alcuni di questi processi devono fare solo operazioni di lettura (i lettori) mentre altri processi possono agire sia in scrittura che in lettura (scrittori). Ci sono chiaramente dei vincoli: 
- Se almeno un lettore sta leggendo dalla risorsa, nessun processo può agire in scrittura finchè il lettore non ha terminato. Più lettori possono leggere contemporaneamente dalla risorsa.
- Se uno scrittore sta scrivendo, nessun altro processo può nè leggere nè scrivere dalla risorsa finchè lo scrittore non ha terminato.

### BarberShop
Il secondo problema (più complicato) è il problema del barbiere addormentato. Immaginate il negozio di un barbiere, con una singola sedia per il taglio e una sala di attesa con n sedie. Vengono applicate le seguenti regole:
- Se non ci sono clienti, il barbiere si addormenta.
- Quando arriva un cliente, se il barbiere sta dormendo deve essere svegliato (dal cliente).
- Se un cliente arriva mentre il barbiere sta lavorando, se nella sala d'attesa c'è almeno una sedia libera si siede ed aspetta, altrimenti esce dal negozio.
- Quando il barbiere finisce il taglio, ispeziona la sala d'attesa per vedere se ci sono clienti in attesa. Se non ce ne sono si addormenta, altrimenti procede con un altro cliente.

## Contributori 

Stefani Emanuele
