# Piano di riorganizzazione a rischio minimo

## Applicato in questa proposta

- README aggiornato con struttura, architettura e istruzioni.
- Documentazione tecnica in `docs/`.
- Guida per contribuire in `CONTRIBUTING.md`.
- Template pull request in `.github/`.
- Validatore dati in `scripts/`, eseguibile manualmente e senza dipendenze esterne.

**Nessun file utilizzato dal sito viene spostato o modificato.** Non vengono modificati HTML, immagini, `luoghi.json`, `CNAME` o il backend.

## Evoluzione proposta (NON applicata)

Una volta predisposto un ambiente di anteprima e verificati tutti i riferimenti:

```text
/
├── index.html, map.html, admin.html, guida.html, missione.html
├── luoghi.json
├── CNAME
├── assets/
│   ├── branding/        # Logo e immagini istituzionali
│   ├── ui/              # Immagini della homepage
│   └── panoramas/       # Foto 360° locali
├── docs/
├── scripts/
└── .github/
```

**Attenzione:** la migrazione delle immagini richiede aggiornamenti atomici a `index.html`, `map.html`, `admin.html` e ai percorsi referenziati da `luoghi.json`, seguiti da test del viewer 360°. Non rinominare o spostare i file solo per rendere l'albero più ordinato.

## Migliorie successive da valutare

1. Documentare e, se possibile, versionare separatamente il backend Google Apps Script (senza credenziali).
2. Chiarire se l'Apps Script sincronizza `luoghi.json` e come si gestiscono conflitti o approvazioni.
3. Aggiungere un'anteprima GitHub Pages e test automatizzati di link e asset prima di spostare file.
4. Valutare se separare CSS e JavaScript dalle pagine HTML, mantenendo invariato il comportamento.
5. Aggiungere un file LICENSE solo dopo aver scelto espressamente le condizioni di riutilizzo del codice; gestire separatamente i diritti di immagini e modelli.
