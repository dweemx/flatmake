import { Dim } from "./src/flatmake/idl/ts/main_generated";
import { flatbuffers } from "flatbuffers";

function toByteBuffer(bytes: ArrayBufferLike) {
    const data = new Uint8Array(bytes);
    return new flatbuffers.ByteBuffer(data);
}

export function getFloat32Array(bytes: ArrayBufferLike) {
    const e = Dim.Float32Array.getRootAsFloat32Array(toByteBuffer(bytes));
    return {
        values: e.dataArray(),
    };
}

type LabeledIndexSet = {
    name: string;
    indices: Uint32Array;
};

export function getLabeledIndexSetByNameFromSuperSet(bytes: ArrayBufferLike, name: string): LabeledIndexSet {
    const e = Dim.LabeledIndexSuperSet.getRootAsLabeledIndexSuperSet(toByteBuffer(bytes));
    const superSetName = e.name();
    const setIndex = [...new Array(e.setsLength()).keys()].filter((index) => {
        return e.sets(index).name() === name;
    });
    if (setIndex.length !== 1) return null;
    const set = e.sets(setIndex[0]);
    return {
        name: set[0].name(),
        indices: set[0].indices(),
    };
}

type LabeledIndexSuperSet = {
    name: string;
    sets: {
        name: string;
        indices: Uint32Array;
    }[];
};

export function getLabeledIndexSuperSet(bytes: ArrayBufferLike): LabeledIndexSuperSet {
    const e = Dim.LabeledIndexSuperSet.getRootAsLabeledIndexSuperSet(toByteBuffer(bytes));
    const name = e.name();
    const sets = [...new Array(e.setsLength()).keys()].map((index) => {
        const set = e.sets(index);
        return {
            name: set.name(),
            indices: set.indices().dataArray(),
        };
    });
    return {
        name: name,
        sets: sets,
    };
}

export function getCoordinates2D(bytes: ArrayBufferLike) {
    const e = Dim.Coordinates2D.getRootAsCoordinates2D(toByteBuffer(bytes));
    const x = e.x();
    const y = e.y();
    return x === null || y === null
        ? null
        : {
              x: x.dataArray(),
              y: y.dataArray(),
          };
}

type ColorArray1D = {
    color: Uint8Array | null;
};

export function getColorArray1D(bytes: ArrayBufferLike): ColorArray1D {
    const e = Dim.ColorArray1D.getRootAsColorArray1D(toByteBuffer(bytes));
    const color = e.color();
    return color === null
        ? {
              color: null,
          }
        : {
              color: color.dataArray(),
          };
}
