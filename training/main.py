from state import State
from player import BotPlayer
from configs import Configs

if __name__ == "__main__":
    configs = Configs()

    # play/train between bots

    p1 = BotPlayer("player_1")

    st = State(p1)
    st.playGame(configs.training_epoch)