import { Dim } from './src/flatmake/idl/js/main_generated'
import { flatbuffers } from 'flatbuffers'

function toByteBuffer(bytes) {
    const data = new Uint8Array(bytes);
    return new flatbuffers.ByteBuffer(data);
}

function getCoordinates2D(bytes) {
    const e = Dim.Coordinates2D.getRootAsCoordinates2D(
        toByteBuffer(bytes),
        null
    );
    return {
        x: e.x().dataArray(),
        y: e.y().dataArray()
    }
}

module.exports = {
    getCoordinates2D
}
