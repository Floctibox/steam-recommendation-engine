import pandas as pd 

game_stat = pd.read_csv("../data/game_stat.csv")
df = pd.read_csv(
    "../data/steam-200k.csv",
    header=None,
    names=["id_player","game","buy?","playtime","unused"]
)

def recommend_popular_game(player_id,game_stat,n=10,metric="owner",min_players=50):

    stat = game_stat.copy()
    if(metric == "mean_playtime"):
        stat=stat[stat["players"] >= min_players]
    
    return(
        stat
        .sort_values(metric,ascending=False)
        .head(n)
        .to_string(index=False)
    )