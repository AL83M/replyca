# replYca

**Archivio digitale del patrimonio attraverso fotogrammetria 3D e panorami a 360°.**

[Visita replyca.art](https://replyca.art/) · [Esplora la mappa](https://replyca.art/map.html) · [Guida alla fotogrammetria](https://replyca.art/guida.html)

replYca è un progetto indipendente per documentare e rendere esplorabili luoghi, opere e testimonianze del patrimonio culturale meno conosciuto. Ponti, architetture rurali, monumenti minori e reperti possono essere geolocalizzati e associati a ricostruzioni 3D o fotografie panoramiche.

> **Stato:** progetto in evoluzione. La presenza di una scheda nell'archivio non equivale a una certificazione storico-scientifica. I contenuti vengono verificati prima della pubblicazione.

## Esplora il progetto

- **[Mappa](https://replyca.art/map.html):** luoghi geolocalizzati e relativi contenuti 3D/360°.
- **[Fotogrammetria](https://replyca.art/guida.html):** guida introduttiva alla tecnica.
- **[Missione](https://replyca.art/missione.html):** finalità culturali e approccio.
- **[Proponi un luogo](https://replyca.art/admin.html):** interfaccia di inserimento e aggiornamento dei luoghi.

## Architettura in breve

Il frontend è un **sito statico HTML/CSS/JavaScript** pubblicato con GitHub Pages e dominio personalizzato `replyca.art`. La mappa usa **Leaflet** e legge l'elenco dei luoghi da **`luoghi.json`**, nella radice pubblica. I contenuti esterni possono essere visualizzati tramite **Sketchfab**, **Luma** e un visualizzatore panoramico basato su **Pannellum**. L'interfaccia `admin.html` invia le proposte e gli aggiornamenti a un **Google Apps Script esterno**; la logica di quel backend non è presente in questa repository.

**Importante:** l'invio del modulo al backend e la pubblicazione effettiva dei dati letti dalla mappa sono passaggi distinti. Non è verificabile da questa repository se, e con quale procedura, il backend aggiorni automaticamente `luoghi.json`. Consultare [il flusso di aggiornamento](docs/AGGIORNARE_LUOGHI.md) prima di modificare l'archivio.

## Struttura della repository

```text
/
├── index.html             # Homepage
├── map.html               # Mappa pubblica; legge luoghi.json
├── admin.html             # Modulo luoghi; comunica con Apps Script
├── guida.html             # Guida alla fotogrammetria
├── missione.html          # Presentazione della missione
├── luoghi.json            # Catalogo attualmente pubblicato
├── CNAME                  # Dominio replyca.art (non spostare)
├── images/                # Immagini e grafica utilizzate dalle pagine
├── *.JPG                  # Panorami storicamente collocati nella radice
├── docs/
│   ├── ARCHITETTURA.md
│   ├── AGGIORNARE_LUOGHI.md
│   └── RIORGANIZZAZIONE.md
├── scripts/
│   └── validate_luoghi.py
├── .github/
│   └── pull_request_template.md
└── CONTRIBUTING.md
```

I file pubblicati restano volutamente nelle posizioni originarie: diversi collegamenti e riferimenti a immagini sono relativi. Non è previsto un sistema di build o una modifica al deployment.

## Aggiornare o proporre un luogo

1. Raccogli nome, località, coordinate WGS84, descrizione e collegamento a un contenuto 3D/360° utilizzabile.
2. Consulta **[Aggiornare i luoghi](docs/AGGIORNARE_LUOGHI.md)** per i due percorsi: interfaccia di proposta o modifica controllata di `luoghi.json`.
3. Prima di proporre una modifica al catalogo, esegui il controllo locale:
   ```bash
   python3 scripts/validate_luoghi.py
   ```
4. Verifica la mappa e l'apertura del visualizzatore in un'anteprima locale, prima di pubblicare.

## Contribuire

Segnalazioni, correzioni documentali, fotografie e proposte di nuovi luoghi sono benvenute. Leggi **[CONTRIBUTING.md](CONTRIBUTING.md)** per criteri, formato e controlli. Evita di caricare materiale di terzi senza autorizzazione o di pubblicare coordinate di siti sensibili.

## Tecnologie e dipendenze

HTML · CSS · JavaScript · Leaflet · OpenStreetMap · GitHub Pages · Sketchfab · Luma · Pannellum · Google Apps Script (backend esterno).

## Obiettivo

**Preservare digitalmente ciò che rischia di essere dimenticato.**

© 2026 replYca. La presenza dei contenuti nel repository non implica automaticamente una licenza di riutilizzo delle immagini o dei modelli di terzi.
