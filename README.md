# Developers lab - Django kurs domaci

Domaci za Django kurs

## Mini informacioni sistem

### Tabele

- Davalac
- Primalac
- Krv

#### Davalac

- Argumenti za konstruisanje su redom: jmbg, ime, prezime, telefon, adresa, datum donacije, krvna grupa
- Nakon class konstruktora, vaseg davaoca mozete sacuvati funkcijom: ".sacuvaj()"
- Kada donator donira, u tabeli se moze zamijeniti vrijednost kolone datum donacije funkcijom: ".donirao(datum)"
- Ako zelite da promijenite datum donacije odredjenog Davaoca koristite fukciju: ".donirao(datum, jmbg)"
- Nadji Davaoca iz tabele: ".nadji(jmbg)"
- Izbrisati Davaoca: ".izbrisi(jmbg)"

### Primalac

- Argumenti za konstruisanje su redom: jmbg, ime, prezime, datum primanja, krvna grupa
- Sacuvavanje Primaoca u tabelu sa funkcijom: ".sacuvaj()"
- Ako Pacijent primi krv datum posljednjeg primanja krvi se mijenja: ".primio(datum)"
- Ako zelite odredjenog pacijenca onda koristite funkciju: ".primio(datum, jmbg)"
- Ako zelite da izbrisete pacienta iz tabele koristite funkciju: ".izbrisi()" || ".izbrisi(jmbg)"

### Krv

- Da nadjete Davaoce za odredjenu krvnu grupu: "nadji_donatora(krvna grupa)"
