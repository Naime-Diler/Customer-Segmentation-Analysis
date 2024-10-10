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
Um das Projekt lokal auszuführen, befolgen Sie die folgenden Schritte:
1. Klonen Sie das Repository von GitHub.
   ```bash
git clone https://github.com/Naime-Diler/Customer-Segmentation-Analysis.git

```
2. Installieren Sie die erforderlichen Abhängigkeiten aus der Datei `requirements.txt`.
      ```bash
pip install -r requirements.txt


```

3. Verwenden Sie das Dockerfile, um das Projekt in einem Docker-Container zu starten.

## Dockerfile  
Im Projekt wurde die Datei `Segmentierungsmodell.py`, die sich im Verzeichnis `.src/` befindet, über das Dockerfile schichtweise aufgebaut.


## GitHub Actions
Im Verzeichnis `.github/workflows` sind Automatisierungsszenarien für GitHub Actions hinterlegt. Die Datei `docker-image.yml` beschreibt einen Workflow, der den Prozess des Erstellens und Veröffentlichens eines Docker-Images automatisiert. Mehr Details dazu unter GitHub Wiki: https://github.com/Naime-Diler/Customer-Segmentation-Analysis/wiki



## Nutzung
Um die EDA-Skripte auszuführen, verwenden Sie die folgenden Befehle:
```bash
python src/eda.py
python src/Segmentierungsmodell.py
```

## Beitrag
Das Projekt ist Open Source und steht für Beiträge offen. Sie können über GitHub Pull Requests einreichen, um das Projekt zu verbessern. Weitere Details finden Sie in der GitHub-Wiki.

## Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert.
