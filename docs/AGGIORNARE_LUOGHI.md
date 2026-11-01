# Aggiornare i luoghi

Questa guida distingue **proposta tramite interfaccia** e **aggiornamento del catalogo statico**. Non presumere che siano automaticamente sincronizzati.

## Percorso A — Proporre o aggiornare dall'interfaccia

1. Apri [Proponi un luogo](https://replyca.art/admin.html).
2. Inserisci nome, categoria, posizione e descrizione; seleziona la tipologia di contenuto.
3. Inserisci il collegamento Sketchfab oppure la risorsa panoramica secondo le indicazioni del modulo.
4. Invia il modulo. `admin.html` trasmette un payload JSON a Google Apps Script esterno e legge la risposta.
5. **Verifica separatamente** che il luogo compaia in `luoghi.json` pubblicato e sulla mappa. Se non compare, la sincronizzazione del backend verso GitHub Pages deve essere controllata dal manutentore.

Non pubblicare password, token o dati personali nel repository o nelle issue.

## Percorso B — Modificare `luoghi.json` con una pull request

1. Crea un branch e modifica **solo** il record necessario in `luoghi.json`, conservando tutti gli altri.
2. Mantieni la struttura di array JSON e i campi esistenti. Per le coordinate usa numeri decimali WGS84, con `lat` tra -90 e 90 e `lon` tra -180 e 180.
3. Per Sketchfab usa `piattaforma: "sketchfab"` e `modello` con l'ID del modello (32 caratteri esadecimali). Per Luma, usa il link effettivamente compatibile con l'iframe corrente.
4. Per i panorami 360°, usa `tipo: "panorama360"` e `foto360` con una risorsa accessibile al visualizzatore. Verifica URL assoluti e CORS/HTTPS; un semplice nome di file relativo potrebbe non funzionare quando caricato da un viewer esterno.
5. Esegui `python3 scripts/validate_luoghi.py`. I warning vanno controllati, non necessariamente corretti modificando i dati storici.
6. Avvia `python3 -m http.server 8000`, visita `http://localhost:8000/map.html` e verifica marker, ricerca e viewer.
7. Apri una pull request con fonte, autorizzazione dei materiali, descrizione del cambiamento e prove dei controlli.

### Esempio di scheda (fotogrammetria)

```json
{
  "nome": "Esempio dimostrativo (non pubblicare)",
  "localita": "Località di esempio",
  "provincia": "Provincia",
  "regione": "Regione",
  "lat": 38.0,
  "lon": 14.5,
  "categoria": "Ponte",
  "anno_scansione": 2026,
  "piattaforma": "sketchfab",
  "modello": "0123456789abcdef0123456789abcdef",
  "descrizione": "Descrizione e fonti verificabili",
  "foto": ""
}
```

Il record è **solo un esempio**: non aggiungerlo a `luoghi.json`.

## Checklist editoriale

- Nome, coordinate e località controllati.
- Provenienza e diritti d'uso di immagini/modelli verificati.
- Nessuna posizione sensibile o privata pubblicata senza valutazione.
- Link 3D/360° aperti e verificati.
- Nessuna modifica non intenzionale ad altri record.
- Anteprima locale e, dopo il merge, controllo del sito online.

## Osservazioni sull'archivio attuale

- I due record esistenti condividono il valore `foto360` che punta a `pontedeininfi360.JPG`. Verificare se è intenzionale, senza correggere automaticamente.
- La radice contiene `image1.png` di soli 2 byte: potrebbe essere un segnaposto; non eliminarlo senza verifica.
- Il campo `foto360` non implica che la mappa apra il panorama: il codice verifica anche `tipo === "panorama360"`.

## Ruolo del manutentore

Prima di dichiarare aggiornato un luogo, confronta il JSON sul branch pubblicato con il risultato del modulo e con il sito live. Se l'Apps Script effettua una sincronizzazione automatica, documentarne in futuro trigger, autorizzazioni e gestione degli errori, senza esporre segreti.
