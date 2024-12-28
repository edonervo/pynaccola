# Pynaccola
Un semplice gioco ispirato alla *Pinnacola* italiana, scritto in Python.

## Descrizione del gioco

La Pinnacola si gioca con due mazzi di carte standard più quattro carte Jolly. Ogni mazzo standard contiene 52 carte e 2 Jolly, per un totale di 54 carte. I ranghi delle carte includono i numeri dal 2 al 10, il Jack, la Regina, il Re e l’Asso. 
Ogni mazzo ha quattro semi: Cuori, Quadri, Fiori e Picche.

Il gioco può essere giocato individualmente o in coppie. Il numero minimo di giocatori è 2 (1 contro 1), mentre non vi è un limite massimo consigliato, anche se si consiglia di non superare gli 8 giocatori.

L'obiettivo del gioco è totalizzare 1500 punti. Il primo giocatore o team che raggiunge 1500 punti vince il *gioco*.

Un *gioco* di Pinnacola è composto da un numero indefinito di *partite*. Ogni *partita* è un sotto-match del *gioco*, in cui i giocatori si sfidano per accumulare punti.

Una *partita* termina quando il primo giocatore o team effettua una *chiusura*. Durante le *partite*, l'obiettivo dei giocatori è ottenere il maggior numero di punti possibile.

## Partita

Per determinare chi inizia a distribuire le carte, ogni giocatore pesca una carta dal mazzo: chi pesca la carta più bassa inizia. Nelle mani successive, il giocatore alla destra (giro antiorario) del precedente mazziere distribuirà le carte.

Ogni giocatore riceve 13 carte, mentre una carta viene piazzata accanto al mazzo formando la pila degli *scarti*.

L'obiettivo della partita è *chiudere*, ma è anche importante accumulare punti. Dopo aver distribuito le carte, inizia il *turno*.

### Turno

All'inizio del turno, il giocatore ha due opzioni:
1. Pescare una carta dal mazzo.
2. Pescare dalla pila degli *scarti*.

Dopo aver pescato una carta, il giocatore può calare una *combinazione* di carte sul *tavolo*, se ne ha una valida. Tuttavia, non è obbligato a farlo se la carta è stata pescata dal mazzo.

Alla fine del turno, il giocatore deve scartare una carta che non possa migliorare le combinazioni già presenti sul tavolo. Questa regola non si applica se il giocatore, scartando, effettua una *chiusura*.

La *chiusura* avviene quando un giocatore scarta l'ultima carta dalla propria mano, rimanendo senza carte e chiudendo così la partita.

Regole aggiuntive:
- Se si pesca dagli *scarti*, è obbligatorio calare la carta pescata in una combinazione valida.
- Pescare dagli *scarti* implica raccogliere anche tutte le carte scartate successivamente a quella pescata e tenerle in mano.
- Le carte nella pila degli *scarti* devono essere disposte in modo visibile e in ordine cronologico.
- Il Jolly ha regole speciali descritte in una sezione dedicata.

### Combinazioni di Pinnacola

Il giocatore può calare una combinazione di carte scegliendo una delle seguenti opzioni:
1. **Tris**: una combinazione di 3 carte dello stesso valore, ma di semi diversi.
2. **Scala minima di 3**: una sequenza di almeno 3 carte consecutive dello stesso seme. L'ordine è il seguente: 
   Asso (1) - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 - Jack - Regina - Re - Asso (1).
3. **Poker**: le 4 carte dello stesso valore, ciascuna con un seme diverso, come nel poker.

Il giocatore può inoltre migliorare combinazioni già esistenti, trasformando un Tris in un Poker o prolungando una Scala.

Nota: i giocatori possono migliorare solo le proprie combinazioni o quelle del proprio compagno di squadra, mai quelle degli avversari.

### Conteggio dei punti

Come indicato nell'introduzione, lo scopo del gioco è raggiungere 1500 punti. Il conteggio dei punti avviene a ogni *chiusura*. 

Il punteggio di ciascun giocatore viene calcolato come segue:
- Somma del valore delle carte calate sul tavolo meno la somma del valore delle carte rimaste in mano (per chi non ha chiuso).
- Somma del valore delle carte calate sul tavolo più il bonus *chiusura* di 100 punti (per il giocatore che ha chiuso).

**Valore delle carte:**
- 2-5: 5 punti
- 6-10, Jack, Regina, Re: 10 punti
- Asso: 15 punti
- Jolly: 25 punti

**Punti delle combinazioni:**
- Tris o Scala con meno di 7 carte: somma dei punti delle singole carte.
- Poker: il valore delle carte è raddoppiato.

*Valore dei Poker:*
- Poker di 2-5: 40 punti
- Poker di 6-10, Jack, Regina, Re: 80 punti
- Poker di Assi: 120 punti
- Poker di Jolly: 400 punti

Se si forma una *Pinnacola* (Scala composta da almeno 7 carte), il valore delle carte è raddoppiato. Una *Pinnacola* completa (da Asso a Asso) vale 1000 punti.

Nota: è possibile che il punteggio di un giocatore o team vada in negativo.

### Chiusura in mano

Una *chiusura* in *mano* si effettua quando la chiusura avviene senza aver calato nessuna combinazione sul tavolo. In questo caso, il valore di tutte le combinazioni è raddoppiato.

Se un giocatore subisce una chiusura senza aver calato combinazioni sul tavolo, il giocatore *paga* doppio, sottraendo il doppio del valore delle sue carte dalla sommatoria.

### Jolly

Il Jolly può essere utilizzato per sostituire qualsiasi carta, seguendo queste regole:
- Non può essere usato per formare Poker o Pinnacole.
- Può essere "rubato" da un altro giocatore che possiede la carta che sostituisce. Il Jolly rubato deve essere immediatamente calato in una combinazione valida o utilizzato per migliorare una combinazione.
- Se il Jolly sostituisce una carta non univoca (ad esempio in un Tris), il giocatore che lo cala deve dichiarare quale carta sta sostituendo.
