"""
SESSION 6: Probability Basics
"""
print("="*60)
print("TASK 1: Sample Space of Die Roll + Coin Flip")
print("="*60)
die_faces = [1, 2, 3, 4, 5, 6]
coin_faces = ['H', 'T']
sample_space = [(d, c) for d in die_faces for c in coin_faces]
print(f"Total Outcomes: {len(sample_space)}")
print(f"Sample Space (Ordered Pairs): {sample_space}
")

print("="*60)
print("TASK 2: Classical Probability of Even Card (Cards 1 to 10)")
print("="*60)
cards = list(range(1, 11))
even_cards = [c for c in cards if c % 2 == 0]
prob_even = len(even_cards) / len(cards)
print(f"Deck: {cards}")
print(f"Favorable Outcomes (Even): {even_cards} (Total = {len(even_cards)})")
print(f"P(Even) = {len(even_cards)} / {len(cards)} = {prob_even:.2f} (50%)
")

print("="*60)
print("TASK 3: Spotify Playlist Probability (Complement Rule)")
print("="*60)
total_songs = 8
arijit_songs = 3
prob_arijit = arijit_songs / total_songs
prob_not_arijit = 1 - prob_arijit
print(f"Total Songs = {total_songs} | Arijit Singh Songs = {arijit_songs}")
print(f"P(Arijit) = {arijit_songs}/{total_songs} = {prob_arijit:.4f}")
print(f"P(NOT Arijit) = 1 - {prob_arijit:.4f} = {prob_not_arijit:.4f} ({prob_not_arijit*100:.1f}%)
")

print("="*60)
print("TASK 4: Addition Rule for Zomato Pizza / Burger Orders")
print("="*60)
p_pizza = 0.3
p_burger = 0.4
p_both = 0.1
p_either = p_pizza + p_burger - p_both
print(f"P(Pizza) = {p_pizza} | P(Burger) = {p_burger} | P(Pizza and Burger) = {p_both}")
print(f"P(Pizza OR Burger) = P(Pizza) + P(Burger) - P(Both) = {p_pizza} + {p_burger} - {p_both} = {p_either:.2f}
")

print("="*60)
print("TASK 5: Conditional Probability Interpretation (Flipkart)")
print("="*60)
print("Base Probability: P(Add Phone to Cart) = 0.20 (20%)")
print("Conditional Probability: P(Add Phone | Interested in Mobiles) = 0.50 (50%)")
print("Explanation: Prior knowledge of customer intent acts as an information filter. When targeting users who actively browse mobile categories, conversion intent increases by 2.5x (from 20% to 50%).")
