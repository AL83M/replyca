# Architettura tecnica di replYca

## Panoramica

replYca è attualmente un sito statico ospitato da GitHub Pages. Non ci sono manifest di pacchetti, bundler o script di compilazione nel repository: le pagine HTML includono CSS e JavaScript direttamente. Il file `CNAME` collega il dominio personalizzato `replyca.art`.

| Componente | File/servizio | Funzione |
| --- | --- | --- |
| Homepage | `index.html` | Navigazione e presentazione |
| Mappa | `map.html` | Leaflet, ricerca, marker e viewer |
| Archivio pubblicato | `luoghi.json` | Array JSON dei luoghi letto dal browser |
| Interfaccia luoghi | `admin.html` | Inserimento/modifica e invio via POST |
| Backend | Google Apps Script esterno | Riceve il payload del modulo; codice non incluso |
| Contenuti 3D | Sketchfab / Luma | Modelli referenziati dal catalogo |
| Panorami | Pannellum | Viewer per i record `tipo: "panorama360"` |
| Immagini | `images/` e file nella radice | Risorse referenziate da percorsi relativi |

## Flusso di lettura

```text
Browser -> map.html -> fetch("luoghi.json")
                         -> marker Leaflet
                         -> popup -> Sketchfab / Luma / Pannellum
```

Anche `admin.html` legge `luoghi.json` per selezionare luoghi esistenti.

## Flusso di scrittura

```text
Utente -> admin.html -> POST JSON a Google Apps Script
                                      |
                                      v
                               Risposta success/error
```

Il frontend mostra un messaggio di successo sulla base della risposta del backend e torna alla mappa. **Non si può dedurre dal solo codice presente qui** che il backend aggiorni direttamente il file GitHub `luoghi.json`. Occorre verificare il processo di sincronizzazione prima di considerare pubblicata una modifica.

## Contratto dati minimo

Il catalogo è un array JSON. Campi utilizzati:

- `nome` (stringa), `lat` e `lon` (numeri in gradi decimali): essenziali per marker e ricerca.
- `localita`, `provincia`, `regione`, `categoria`, `descrizione`: metadati testuali.
- `anno_scansione`: anno della documentazione.
- `piattaforma`: `sketchfab` oppure `luma`; `modello`: ID Sketchfab o URL del viewer Luma.
- `tipo: "panorama360"` e `foto360`: abilitano il viewer panoramico; un campo `foto360` da solo **non** basta se il record resta di tipo fotogrammetria.
- `foto`: campo opzionale già presente nel catalogo e nel modulo.

I record storici non devono essere normalizzati o rinominati senza verificare tutti i punti di lettura.

## Percorsi da mantenere

- `CNAME` **nella radice** per GitHub Pages.
- `index.html`, `map.html`, `admin.html`, `guida.html`, `missione.html` **nella radice**, salvo migrazione controllata.
- `luoghi.json` **nella radice**: i due frontend lo richiedono con `fetch("luoghi.json")`.
- `images/*` e i panorami `*.JPG` già referenziati: uno spostamento richiede aggiornare i percorsi nelle pagine e nei dati.

## Controlli prima della pubblicazione

1. Verificare JSON con `python3 scripts/validate_luoghi.py`.
2. Avviare un server statico locale, per esempio `python3 -m http.server 8000`, e aprire `http://localhost:8000/`. L'apertura diretta di `map.html` con `file://` può bloccare `fetch`.
3. Controllare homepage, menu, mappa, ricerca, popup e viewer 3D/360°.
4. Controllare link alle immagini e l'eventuale invio al backend **solo in un ambiente di test autorizzato**, per evitare inserimenti reali accidentali.
5. Verificare la pubblicazione GitHub Pages e il dominio `replyca.art`.

Non sono incluse credenziali o codice del backend; non aggiungerli a questa repository pubblica.
