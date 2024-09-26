
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemons_name = {}
pokemons_id = {}
for i in range(1, N+1):
    pokemon = input().strip()
    pokemons_id[i] = pokemon
    pokemons_name[pokemon] = i


for j in range(M):
    s = input().strip()
    if s.isdigit():
        print(pokemons_id[int(s)])
    else:
        print(pokemons_name[s])


