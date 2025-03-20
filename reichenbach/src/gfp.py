import random
import sys

def simulate_game(rounds=100_000):
	holmes_victories = moriarty_victories = draws = 0
	for _ in range(rounds):
		# Reinitializing all transient vars at each experiment round
		sum = holmes_last_draw = moriarty_last_draw = 0
		# Holmes' turn: he must play untils sum > 100
		while sum <= 100:
			holmes_last_draw = random.randint(1,100)
			sum += holmes_last_draw
		# Moriarty's turn: he must play until sum > 200
		while sum <= 200:
			moriarty_last_draw = random.randint(1,100)
			sum += moriarty_last_draw
		if holmes_last_draw > moriarty_last_draw:
			holmes_victories += 1
		elif holmes_last_draw < moriarty_last_draw:
			moriarty_victories += 1
		else:
			draws += 1
	return holmes_victories/rounds, moriarty_victories/rounds, draws/rounds

if __name__ == "__main__":
	rounds = int(sys.argv[1]) if len(sys.argv) > 1 else 100_000
	holmes_victory_ratio, moriarty_victory_ratio, draws_ratio = simulate_game(rounds)
	print(f"Holmes victory rate: {100 * holmes_victory_ratio:.2f}%")
	print(f"Moriarty victory rate: {100 * moriarty_victory_ratio:.2f}%")
	print(f"Draws rate: {100 * draws_ratio:.2f}%")
