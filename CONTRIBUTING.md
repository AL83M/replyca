# Contribuire a replYca

Grazie per l'interesse verso replYca. Accogliamo segnalazioni, correzioni, documentazione, proposte di luoghi e miglioramenti al sito.

## Prima di proporre un luogo

Raccogli nome, posizione verificata, descrizione, eventuali riferimenti storici e link a fotografie, panorami o modelli 3D. Specifica sempre l'origine dei materiali e se hai il diritto di condividerli. Non pubblicare coordinate o informazioni che possano esporre beni fragili, luoghi privati o persone a rischi.

## Proposte tramite il sito

Utilizza [il modulo dedicato](https://replyca.art/admin.html). Il modulo invia i dati a un backend esterno; controlla che la scheda sia poi effettivamente presente sulla [mappa](https://replyca.art/map.html).

## Modifiche al repository

1. Apri un'issue per discutere cambiamenti strutturali importanti.
2. Crea un branch con una modifica circoscritta.
3. Per il catalogo, segui [la guida di aggiornamento](docs/AGGIORNARE_LUOGHI.md).
4. Esegui `python3 scripts/validate_luoghi.py` e controlla la pagina con `python3 -m http.server 8000`.
5. Apri una pull request descrivendo cosa cambia, come è stato verificato e quali contenuti sono stati autorizzati.

## Convenzioni

- Testi e documentazione preferibilmente in italiano, chiari e verificabili.
- Evita modifiche non richieste ai percorsi pubblici, ai file `CNAME`, `luoghi.json` e agli asset.
- Mantieni i dati JSON compatibili con il frontend esistente; non aggiungere campi che richiedono nuove funzionalità senza documentarle.
- Non includere password, token, dati di accesso, dati personali non necessari o contenuti senza permesso.
- Non assumere che un invio riuscito a Google Apps Script equivalga a una pubblicazione automatica su GitHub Pages.

## Diritti

Il repository non contiene attualmente una licenza generale esplicita. Una pull request non concede automaticamente il diritto di riutilizzare fotografie, scansioni, modelli 3D o altri materiali di terzi. Specifica la provenienza e chiedi autorizzazione quando necessario.
