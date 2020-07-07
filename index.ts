import { Dim } from './src/flatmake/idl/ts/main_generated'
import { flatbuffers } from 'flatbuffers'

function toByteBuffer(bytes: ArrayBufferLike) {
    const data = new Uint8Array(bytes);
    return new flatbuffers.ByteBuffer(data);
}

export function getCoordinates2D(bytes: ArrayBufferLike) {
    const e = Dim.Coordinates2D.getRootAsCoordinates2D(
        toByteBuffer(bytes)
    );
    const x = e.x()
    const y = e.y()
    return x === null || y === null ?
        {
            x: null,
            y: null
        } : {
            x: x.dataArray(),
            y: y.dataArray()
        }
}

export function getColorArray1D(bytes: ArrayBufferLike) {
    const e = Dim.ColorArray1D.getRootAsColorArray1D(
        toByteBuffer(bytes)
    );
    const color = e.color()
    return color === null ?
        {
            color: null
        } : {
        color: color.dataArray(),
        }
}

export function getFloat32Array(bytes: ArrayBufferLike) {
    const e = Dim.Float32Array.getRootAsFloat32Array(
        toByteBuffer(bytes)
    );
    return {
        values: e.dataArray(),
    }
}

