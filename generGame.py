def get_game_suggestions():
    # Game database structure
    games_db = {
        "action": {
            "pc": ["Doom Eternal", "Cyberpunk 2077", "Devil May Cry 5"],
            "playstation": ["God of War", "Spider-Man: Miles Morales", "Ghost of Tsushima"],
            "xbox": ["Halo Infinite", "Gears 5", "Forza Horizon 5"]
        },
        "rpg": {
            "pc": ["The Witcher 3", "Elden Ring", "Divinity: Original Sin 2"],
            "playstation": ["Final Fantasy VII Remake", "Horizon Forbidden West", "Persona 5 Royal"],
            "xbox": ["Fable Anniversary", "Lost Odyssey", "Tales of Arise"]
        },
        "adventure": {
            "pc": ["Red Dead Redemption 2", "Assassin's Creed Valhalla", "Subnautica"],
            "playstation": ["Uncharted 4", "The Last of Us Part II", "Ratchet & Clank: Rift Apart"],
            "xbox": ["Sea of Thieves", "Ori and the Will of the Wisps", "Psychonauts 2"]
        },
        "strategy": {
            "pc": ["Civilization VI", "XCOM 2", "Total War: Warhammer III"],
            "playstation": ["XCOM 2 Collection", "Into the Breach", "Valkyria Chronicles 4"],
            "xbox": ["Halo Wars 2", "Gears Tactics", "Age of Empires II: Definitive Edition"]
        }
    }

    # Get user input
    print("Welcome to Game Suggestor!")
    print("Available genres: action, rpg, adventure, strategy")
    genre = input("Enter your preferred genre (or press Enter to skip): ").lower()
    platform = input("Enter your platform (pc/playstation/xbox or press Enter to skip): ").lower()

    # Filter games
    suggestions = []
    if genre:
        if genre in games_db:
            if platform:
                if platform in games_db[genre]:
                    suggestions = games_db[genre][platform]
                else:
                    return f"No games found for {platform} platform in {genre} genre"
            else:
                # All platforms for specified genre
                suggestions = [game for platform_games in games_db[genre].values() for game in platform_games]
        else:
            return "Genre not found. Please try with a different genre."
    else:
        # Show all games if no genre specified
        if platform:
            suggestions = [game for genre in games_db.values() for game in genre.get(platform, [])]
        else:
            suggestions = [game for genre in games_db.values() for platform_games in genre.values() for game in platform_games]

    # Format output
    if not suggestions:
        return "No games found matching your criteria."

    result = "\nHere are some game suggestions for you:\n"
    for i, game in enumerate(suggestions, 1):
        result += f"{i}. {game}\n"
    
    return result

# Run the program
print(get_game_suggestions())
