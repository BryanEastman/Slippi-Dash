const { SlippiGame } = require("@slippi/slippi-js")

const game = new SlippiGame("/home/beastman/Projects/Slippi-Dash/data/test_data/Game_20211201T051930.slp");


const metadata = game.getMetadata();
console.log(metadata)

const stats = game.getStats();
console.log(stats)


let fs = require('fs'),
path = require('path')

let walk = function (dir) {
    fs.readdir(root,(e,items) => {
        items.forEach((item) => {
            let itemPath = path.join(dir, item);
            fs.stat(itemPath, (e, stats) => {
                console.log(itemPath);
                if (stats.isDirectory()) {
                    walk(itemPath)
                }
            });
        });
    });
}
walk(process.cwd())