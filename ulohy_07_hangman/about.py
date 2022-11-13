def about_game():
    filename = "about.txt"
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
            print(contents)
    except OSError:
        print(f'Soubor {filename} bohužel nelze nalézt.')
