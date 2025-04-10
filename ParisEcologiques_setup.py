import os

def create_directory_structure():
    # Structure principale
    directories = [
        "00 - Setup",
        "01 - Data/01 - Data Sources",
        "01 - Data/02 - Raw Data",
        "01 - Data/03 - Cleaned Data",
        "01 - Data/04 - Processed Data",
        "02 - Analytics",
        "03 - Visualisations",
        "04 - Documentation"
    ]

    # Sous-catégories de données
    data_categories = [
        "01 - Habitat",
        "02 - Transport",
        "03 - Population",
        "04 - Air Quality",
        "05 - Energie"
    ]

    # Création des répertoires principaux
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Créé: {directory}")

    # Création des sous-catégories dans chaque dossier de données
    data_folders = ["02 - Raw Data", "03 - Cleaned Data", "04 - Processed Data"]
    for data_folder in data_folders:
        for category in data_categories:
            path = os.path.join("01 - Data", data_folder, category)
            os.makedirs(path, exist_ok=True)
            print(f"Créé: {path}")

    # Création de fichiers .gitkeep pour conserver la structure dans Git
    for root, dirs, files in os.walk("."):
        if not files and not dirs:
            with open(os.path.join(root, ".gitkeep"), "w") as f:
                pass

if __name__ == "__main__":
    create_directory_structure() 