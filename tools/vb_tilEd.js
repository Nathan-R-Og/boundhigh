//tool for Tiled tilemap editor

var vbMapFormat = {
    name: "Virtual Boy Tiles",
    extension: "bin",

    read: function(fileName) {
        const file = new BinaryFile(fileName, BinaryFile.ReadOnly);
        const bytes = new Uint16Array(file.readAll());
        file.close();

        var size = tiled.prompt("Width, Height?", "Width, Height", "yeah").split(",")
        const width = parseInt(size[0]);
        const height = parseInt(size[1]);

        const map = new TileMap();
        map.setSize(width, height);
        var t_size = tiled.prompt("Tile Width, Height?", "Tile Width, Height", "yeah").split(",")
        const t_width = parseInt(t_size[0]);
        const t_height = parseInt(t_size[1]);
        map.setTileSize(t_width, t_height);

        //if a tileset is already open, add that to the tilemap
        let tileset = tiled.activeAsset && tiled.activeAsset.isTileset ? tiled.activeAsset : null;

        if (tileset) {
            map.addTileset(tileset);
        }

        const layer = new TileLayer("Tiles");
        const edit = layer.edit();
        for (let i = 0; i < Math.min(bytes.length, width*height); i++) {
            const x = i % width;
            const y = Math.floor(i / width);
            const tileId = bytes[i];

            if (tileset && tileId > 0) {
                const tile = tileset.tile(tileId);
                if (tile) edit.setTile(x, y, tile);
            }
        }

        //commit
        edit.apply();
        map.addLayer(layer);

        //open in editor
        tiled.activeAsset = map;
    },

    write: function(map, fileName) {
        var tiles = [];
        for (var i = 0; i < map.layerCount; ++i) {
            var layer = map.layerAt(i);
            if (layer.isTileLayer) {
                for (y = 0; y < layer.height; ++y) {
                    for (x = 0; x < layer.width; ++x) {
                        const tileId = layer.cellAt(x, y).tileId;
                        tiles.push(tileId);
                    }
                }
            }
        }

        var file = new BinaryFile(fileName, TextFile.WriteOnly);
        var bytes = new Uint16Array(tiles);
        file.write(bytes.buffer);
        file.commit();
    },
}

tiled.registerMapFormat("virtual boy", vbMapFormat)