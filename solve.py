from board import Board

def solve(game_map):
    board = Board(game_map)
    


game_maps = ( "+------------+\n"
            + "|RGY         |\n"
            + "|            |\n"
            + "|     **     |\n"
            + "|     **     |\n"
            + "|            |\n"
            + "|         rgy|\n"
            + "+------------+",

                "+------------+\n"
            + "|R           |\n"
            + "|G           |\n"
            + "|Y    **     |\n"
            + "|     **    r|\n"
            + "|           g|\n"
            + "|           y|\n"
            + "+------------+",

                "+------------+\n"
            + "|R           |\n"
            + "|G    **     |\n"
            + "|Y    **     |\n"
            + "|            |\n"
            + "|     **    r|\n"
            + "|     **    g|\n"
            + "|           y|\n"
            + "+------------+",

                "+------------+\n"
            + "|R    *******|\n"
            + "|G    *******|\n"
            + "|Y    *******|\n"
            + "|            |\n"
            + "|           r|\n"
            + "|******     g|\n"
            + "|******     y|\n"
            + "+------------+",

                "+------------+\n"
            + "|R     ** ***|\n"
            + "|G     ** ***|\n"
            + "|Y           |\n"
            + "|            |\n"
            + "|            |\n"
            + "|            |\n"
            + "|           g|\n"
            + "|** ***     r|\n"
            + "|** ***     y|\n"
            + "+------------+" )
