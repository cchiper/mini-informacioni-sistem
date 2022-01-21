import sqlite3

def execute(query):
    conn = sqlite3.connect('baza.db')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()

def get_execute(query):
    conn = sqlite3.connect('baza.db')
    c = conn.cursor()
    c.execute(query)
    podaci = c.fetchall()
    conn.commit()
    conn.close()
    return podaci

def set_table():
    conn = sqlite3.connect('baza.db')

    conn.execute("""
        CREATE TABLE IF NOT EXISTS Donator(
            JMBG char(13) PRIMARY KEY,
            Ime varchar(15) NOT NULL,
            Prezime varchar(15) NOT NULL,
            Br_telefona char(9) NOT NULL,
            Adresa varchar(10) NOT NULL,
            Datum_donacije varchar(8) NOT NULL
        );
        """
    )

    conn.execute("""
        CREATE TABLE IF NOT EXISTS Primalac(
            JMBG char(13) PRIMARY KEY,
            Ime varchar(15) NOT NULL,
            Prezime varchar(15) NOT NULL,
            Datum_primanja varchar(8) NOT NULL
        );
        """
    )

    conn.execute("""
        CREATE TABLE IF NOT EXISTS Krv(
            Grupa char(2) NOT NULL,
            Donator_JMBG char(9) DEFAULT NULL,
            Primalac_JMBG char(9) DEFAULT NULL,
            FOREIGN KEY(Donator_JMBG) REFERENCES Donator(JMBG)
            FOREIGN KEY(Primalac_JMBG) REFERENCES Primalac(JMBG)
        );
        """
    )

    conn.commit()
    conn.close()


class Donator:
    def __init__(self, jmbg, ime, prezime, telefon, adresa, datum_donacije, grupa):
        self.jmbg = jmbg
        self.ime = ime
        self.prezime = prezime
        self.telefon = telefon
        self.adresa = adresa
        self.datum_donacije = datum_donacije
        self.grupa = grupa

    def sacuvaj(self):
        execute(f"INSERT INTO Donator (JMBG, Ime, Prezime, Br_telefona, Adresa, Datum_donacije) VALUES ('{self.jmbg}', '{self.ime}', '{self.prezime}', '{self.telefon}', '{self.adresa}', '{self.datum_donacije}')")
        execute(f"INSERT INTO Krv (Grupa, Donator_JMBG) VALUES ('{self.grupa}', {self.jmbg})")

    def donirao(self, datum, jmbg=None):
        if(jmbg == None):
            jmbg = self.jmbg

        execute(f"UPDATE Donator SET datum_donacije = '{datum}' WHERE JMBG = '{jmbg}'")

    def nadji(self, jmbg=None):
        if(jmbg == None):
            jmbg = self.jmbg

        return get_execute(f"SELECT * FROM Donator WHERE JMBG = '{jmbg}'")

    def izbrisi(self, jmbg=None):
        if(jmbg == None):
            jmbg = self.jmbg

        execute(f"DELETE FROM Donator WHERE JMBG = '{jmbg}'")
        execute(f"DELETE FROM Krv WHERE Donator_JMBG = '{jmbg}'")


class Primalac:
    def __init__(self, jmbg, ime, prezime, primanje, grupa):
        self.jmbg = jmbg
        self.ime = ime
        self.prezime = prezime
        self.primanje = primanje
        self.grupa = grupa

    def sacuvaj(self):
        execute(f"INSERT INTO Primalac (JMBG, Ime, Prezime, Datum_primanja) VALUES ('{self.jmbg}', '{self.ime}', '{self.prezime}', '{self.primanje}')")
        execute(f"INSERT INTO Krv (Grupa, Primalac_JMBG) VALUES ('{self.grupa}', {self.jmbg})")

    def primio(self, datum, jmbg=None):
        if(jmbg == None):
            jmbg = self.jmbg

        execute(f"UPDATE Primalac SET datum_primanja = '{datum}' WHERE JMBG = '{jmbg}'")

    def izbrisi(self, jmbg=None):
        if(jmbg == None):
            jmbg = self.jmbg

        execute(f"DELETE FROM Primalac WHERE JMBG = '{jmbg}'")
        execute(f"DELETE FROM Krv WHERE Primalac_JMBG = '{jmbg}'")

class Krv:
    def nadji_donatora(self, grupa):
        jmbgs = get_execute(f"SELECT * FROM Krv WHERE Grupa = '{grupa}'")

