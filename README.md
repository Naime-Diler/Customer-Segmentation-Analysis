# Customer-Segmentation-Analysis

## Überblick
Ziel dieses Projekts ist es, mithilfe der Kundendaten aus dem `MallCustomer.csv`-Datensatz eine Kundensegmentierung durchzuführen. Durch explorative Datenanalyse (EDA) und Segmentierungsmodelle werden die Kunden in verschiedene Gruppen eingeteilt, um gezielte Marketingstrategien zu entwickeln und den Kundenservice zu optimieren.

## Datensatz
Der `MallCustomer.csv`-Datensatz enthält Kundenmerkmale wie Kunden-ID, Geschlecht, Alter, Jahreseinkommen und Ausgaben-Score.

## Dateistruktur
Alle relevanten Skripte befinden sich im Ordner **`src/`**: 
- **`eda/`**: Explorative Datenanalyse des MallCustomer-Datensatzes.
- **`Segmentierungsmodell/`**: Entwicklung und Validierung von Kundensegmentierungsmodellen.

## Explorative Datenanalyse (EDA)
Die EDA umfasst:
1. Datenanalyse
2. Datenvisualisierung
3. Statistische Auswertung

## Segmentierungsmodell
Das Segmentierungsmodell wird unter Anwendung von Clustering-Methoden entwickelt. Der Prozess umfasst:
1. Merkmalsauswahl: Identifikation relevanter Merkmale für die Segmentierung.
2. Modellauswahl: Evaluation verschiedener Clustering-Algorithmen wie K-Means oder hierarchisches Clustering.

## Einrichtung
Folgen Sie diesen Schritten, um das Projekt lokal auszuführen:
1. Klonen Sie das Repository:
   ```bash
   git clone https://github.com/Naime-Diler/Customer-Segmentation-Analysis.git
   ```
2. Installieren Sie die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```
3. Starten Sie das Projekt mit Docker:
   Verwenden Sie das bereitgestellte Dockerfile, um das Projekt in einer isolierten Umgebung auszuführen. Weitere Informationen finden Sie im [GitHub Wiki](https://github.com/Naime-Diler/Customer-Segmentation-Analysis/wiki).

## Nutzung
Um die EDA-Skripte auszuführen, verwenden Sie die folgenden Befehle:
```bash
python src/eda.py
python src/Segmentierungsmodell.py
```

## GitHub Actions
Automatisierungsskripte für GitHub Actions befinden sich im Verzeichnis `.github/workflows`. Die Datei `docker-image.yml` beschreibt den Workflow zum Erstellen und Veröffentlichen eines Docker-Images. Mehr Informationen dazu finden Sie im [GitHub Wiki](https://github.com/Naime-Diler/Customer-Segmentation-Analysis/wiki).


## Beitrag
Das Projekt ist Open Source und steht für Beiträge offen. Sie können über GitHub Pull Requests einreichen, um das Projekt zu verbessern. Weitere Details finden Sie im [GitHub Wiki](https://github.com/Naime-Diler/Customer-Segmentation-Analysis/wiki).

## Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert.
