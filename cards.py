// Tariff Tantrum Digital Card Deck
// A simple array of cards for random selection in online play

const tariffDeck = [
  "Country X slaps a 25% tariff on steel from Country Y!",
  "Trade deficit scandal! Everyone drinks 2.",
  "Currency manipulation accusations fly. Roll a die. If even, you retaliate; if odd, you must apologize and drink.",
  "Your prime minister tweets angrily. Random country drinks 1.",
  "Global summit failure! Everyone drinks.",
  "You impose a tariff, but forget to tell your allies. They drink 3 out of spite.",
  "You blink first! Lose 1 export token and drink 2.",
  "Domestic lobby pressures you to raise tariffs. Choose a neighbor to punish.",
  "Sudden economic downturn! Lose 2 tokens or drink 4.",
  "Free trade agreement backfires. Give 1 token to another player.",
  "WTO rules against you. Skip your next turn and drink 3.",
  "Foreign embargo! Can't speak for 1 round or drink 2.",
  "You accuse a player of dumping! They roll a die — 1-3: pay a tariff (drink), 4-6: you pay instead.",
  "Election year! No one can impose tariffs for 1 round.",
  "You reach a shaky bilateral deal. Choose two players to toast and drink 1 each.",
  "Strategic reserves depleted! Drink until someone offers you a token.",
  "Sanction swap! Trade 1 token with the player of your choice.",
  "Mega tariff war! Everyone drinks 2 and throws 1 token into the middle.",
  "You win a trade dispute. Take 1 token from anyone of your choice.",
  "Sudden peace talks! Everyone passes a token to the left."
];

// Function to draw a random card
function drawCard() {
  const index = Math.floor(Math.random() * tariffDeck.length);
  return tariffDeck[index];
}

// Example usage in browser console:
// console.log(drawCard());

export { drawCard, tariffDeck };
