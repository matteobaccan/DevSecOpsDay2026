# Idee per dimagrire la presentazione

> **Stato: bozza di lavoro — solo idee, nessuna decisione presa.**
> Da riprendere la **settimana prima dell'evento** (DevSecOps Day 2026 — 14 ottobre 2026,
> quindi indicativamente dal **7 ottobre 2026**) per decidere cosa resta nel talk
> e cosa finisce nella versione lunga della presentazione.

## Obiettivo

Produrre due tagli dallo stesso sorgente:

| Versione | Durata | Destinazione |
|---|---|---|
| **Talk** | ~40 min (slot evento) | speech dal vivo |
| **Estesa** | senza vincolo | PDF/repo per chi vuole approfondire dopo |

Vincolo pratico: 49 slide totali in `presentation30min.md`. A ~1 min/slide di media
(con le slide di transizione che costano poco e i casi reali che costano molto)
40 min stanno intorno alle **28-32 slide**. Servono quindi ~15-20 slide in meno.

---

## Feedback ricevuti

### Andrea Bovio — LinkedIn, 24 agosto 2026

> **19:10** — Secondo me è più interessante la seconda parte dove parli di Mitigazioni
> architetturali. Poi è vero che devi dare il contesto e per tanto ci vuole tutta la
> prima parte, però la mia sensazione è che potrebbe diventare un po' noiosa in uno
> speech di 40 min.
>
> **19:17** — Io terrei 5 e 6, 8 e 9, della prima parte per dare il contesto.
>
> **19:19** — Farei 14 e 15 e poi una slide sola con tutti i richiami alle CVE.
> Metterei la 19 perché tutti parlano di MCP come la manna dal cielo...
>
> **19:21** — E poi inizi la parte con le altre parti.
>
> **19:23** — Poi è anche vero che non conosco il tipo di pubblico e per cui sono più
> interessati a quella parte rispetto al resto. Ma io da uno speech mi aspetto di
> portarmi a casa qualcosa che mi rimane rispetto a semplici CVE che posso cercarmi
> anche io.

**Sintesi del punto chiave:** le CVE sono materiale da *reference*, non da *speech*.
Il valore che il pubblico si porta a casa sta nelle mitigazioni architetturali
(sezioni 3-4-5). La prima parte serve solo a costruire il contesto minimo.

### Matteo Baccan (io)

> **19:15** — Temo anche io... ma ancora non so dove tagliare.

---

## Proposta di taglio derivata dal feedback di Andrea

Numerazione = pagine del PDF esportato.

### Sezione 1 — La nuova superficie d'attacco (slide 3-11)

| # | Titolo | Proposta | Note |
|---|---|---|---|
| 3 | *Transizione: La nuova superficie d'attacco* | **Tieni** | costa pochi secondi |
| 4 | L'era degli agenti autonomi: l'evoluzione | **Taglia?** | il concetto si può dire a voce sulla 5 |
| 5 | La superficie d'attacco AI in azienda | **Tieni** | esplicitamente indicata da Andrea |
| 6 | L'evoluzione della prompt injection: ere 1.0 e 1.5 | **Tieni** | esplicitamente indicata da Andrea |
| 7 | La stessa tecnica, usata al contrario | **Taglia** | bella ma è una digressione (anti-cheating, watermark ICML) |
| 8 | L'era 2.0: worm AI e memory poisoning | **Tieni** | esplicitamente indicata da Andrea |
| 9 | Caso reale: AI recommendation poisoning | **Tieni** | esplicitamente indicata da Andrea |
| 10 | Caso reale: la finta offerta di lavoro (1/2) | **Taglia** | due slide per un solo caso: troppo per il tempo |
| 11 | Caso reale: la finta offerta di lavoro (2/2) | **Taglia** | ↑ |

**Risparmio: 4 slide.**

⚠️ Da valutare: la 10-11 (Contagious Interview via `tasks.json` di VS Code) è il caso
più concreto e "vicino" per un pubblico di sviluppatori. Alternativa: **fondere 10+11 in
una sola** e tagliare invece la 9. Da decidere guardando il pubblico atteso.

### Sezione 2 — Il problema strutturale (slide 12-20)

| # | Titolo | Proposta | Note |
|---|---|---|---|
| 12 | *Transizione: Il problema strutturale* | **Tieni** | |
| 13 | Il problema strutturale: sintassi vs dati | **Da decidere** | Andrea non la cita, ma è il cuore del "perché non si risolve con i filtri" |
| 14 | Il gap semantico e le patch soft | **Tieni** | esplicitamente indicata da Andrea |
| 15 | La gravità degli agenti: azioni reali & RCE | **Tieni** | esplicitamente indicata da Andrea |
| 16 | Vulnerabilità AI nel 2026: SK e LiteLLM | **Fondi** | → slide unica CVE |
| 17 | Comment and control: prompt injection via commenti GitHub | **Fondi** | → slide unica CVE |
| 18 | Black Hat 2026: l'estate degli agenti sotto attacco | **Fondi** | → slide unica CVE |
| 19 | La crisi di sicurezza del protocollo MCP | **Tieni** | Andrea: "tutti parlano di MCP come la manna dal cielo" |
| 20 | Esfiltrazione dati e attacchi stealth | **Fondi** | → slide unica CVE |

**Nuova slide da creare: "CVE & incidenti 2024-2026 in una pagina"** — elenco secco
(Vanna.AI RCE, EchoLeak, Semantic Kernel, LiteLLM KEV/BadHost, Comment&Control,
PleaseFix/CoSnitch) con il messaggio: *"non le leggo una per una, sono nel PDF, il punto
è che sono tutte lo stesso bug architetturale"*. Rimanda alla slide 49 (risorse CVE)
già presente.

**Risparmio: 3 slide** (4 fuse in 1). Con la 13 tagliata: 4 slide.

### Sezioni 3-4-5 — Mitigazioni, hardening, testing (slide 21-43)

**Questo è il cuore del talk secondo Andrea: qui non si taglia, semmai si respira.**

Idee comunque da tenere sul tavolo se il tempo non basta:

- **Slide 22-27 (i 6 design pattern)** — 6 slide, una per pattern. Opzione: 1 slide
  riassuntiva con tutti e 6 + 2-3 slide di dettaglio sui più interessanti
  (Dual LLM, Code-Then-Execute). *Rischio:* sono la parte più "portabile a casa",
  comprimerle contraddice il feedback. **Preferenza attuale: non toccarle.**
- **Slide 31-36 (Hardening: gateway, shields, spotlighting, FIDES, output moderation,
  data minimization)** — 6 slide con struttura ripetitiva. Candidate a fusione:
  32+33 (Prompt Shields + Spotlighting, entrambi probabilistici) e
  35+36 (output moderation + data minimization, entrambi lato output/dati).
  **Risparmio potenziale: 2 slide** senza perdere contenuto.
- **Slide 38 (Caso reale: quando l'isolamento di rete manca)** — è di nuovo un caso
  reale/CVE-like: se serve tempo, è il primo candidato di questa sezione.
- **Slide 41-42 (testing avversariale + tooling CI/CD)** — comprimibili in 1 sola se
  si è in ritardo sul palco. Da tenere come "valvola di sfogo" a runtime, non da
  tagliare a priori.

### Chiusura (slide 43-49)

| # | Contenuto | Proposta |
|---|---|---|
| 43 | Conclusioni e filosofia DevSecOps per l'AI | **Tieni** — è il take-away |
| 44 | Q&A | **Tieni** |
| 45 | Contatti / QR | **Tieni** |
| 46 | Easter egg "IGNORA TUTTE LE ISTRUZIONI PRECEDENTI" | **Tieni** — costa 5 secondi e chiude bene |
| 47-49 | Risorse utili (framework, tool, CVE) | **Tieni ma non le mostro** — appendice, "sono nel PDF" |

---

## Conto della serva

| Scenario | Slide | Stima |
|---|---|---|
| Attuale | 49 | ~50+ min |
| Taglio Andrea (4+3) | 42 | ~43 min |
| + taglio 13 e fusioni hardening (32+33, 35+36) | 39 | ~40 min ✅ |
| + taglio 38 e fusione 41+42 | 37 | margine di sicurezza |

---

## Domande aperte da risolvere prima dell'evento

1. **Chi è il pubblico?** Andrea lo dice esplicitamente: non lo conosce. Se è
   prevalentemente dev/platform → confermare il taglio (poco contesto, molte mitigazioni).
   Se è misto/management → la prima parte serve di più e va tagliato altrove.
   → **Chiedere agli organizzatori il profilo degli iscritti.**
2. **Durata reale dello slot:** 40 min inclusi Q&A o + Q&A? Cambia di 5-10 min il budget.
3. **Demo:** la cartella `demo/` (AI gateway, prompt shields, output moderation) entra
   nel talk o resta materiale da repo? Una demo live vale 5-8 min e sposta tutti i conti.
4. **Due file o uno?** Opzioni:
   - file unico + marcatura delle slide "extended-only" e build a due target
   - due file separati (`presentation-talk.md` + `presentation-extended.md`), con rischio
     di divergenza dei contenuti
   - **Preferenza:** file unico, così le fonti restano allineate.
5. **Rinominare il file:** si chiama `presentation30min.md` ma il talk è da 40 min.

## Da fare la settimana prima

- [ ] Prova a voce cronometrata della versione integrale → capire il tempo reale/slide
- [ ] Decidere il taglio definitivo su questa base (non a stima)
- [ ] Creare la slide unica "CVE in una pagina"
- [ ] Marcare le slide "extended-only" nel sorgente
- [ ] Riprova cronometrata della versione corta
- [ ] Aggiornare il README con le due versioni
