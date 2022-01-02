const { SlippiGame } = require("@slippi/slippi-js")

const game = new SlippiGame("/home/beastman/Projects/Slippi-Dash/data/test_data/Game_20211201T051930.slp");

const stats = game.getStats();
console.log(stats)