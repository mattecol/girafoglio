# girafoglio

Progetto Python per girare spartiti con movimenti della testa.

## Avvio rapido

Esegui la demo in modalità simulata:

```bash
python main.py --simulate
```

Inserisci un angolo di yaw (in gradi) per ogni riga:

- valori positivi alti (es. `30`) => pagina successiva
- valori negativi bassi (es. `-30`) => pagina precedente
- torna vicino a `0` per riarmare il trigger del movimento successivo

Termina con `Ctrl+D` (Linux/macOS) o `Ctrl+Z` (Windows).
