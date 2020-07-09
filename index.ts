import { Dim } from "./src/flatmake/idl/ts/main_generated";
import { flatbuffers } from "flatbuffers";

export type LabeledIndexSet =
    | {
          name: string | null;
          indices: Uint32Array | null;
      }
    | null
    | undefined;

export type LabeledIndexSuperSet = {
    name: string | null;
    sets: LabeledIndexSet[];
};

export type Coordinates2D = {
    x: Float32Array | null;
    y: Float32Array | null;
} | null;

export type ColorArray1D = {
    color: Uint8Array | null;
} | null;

function toByteBuffer(bytes: ArrayBufferLike) {
    const data = new Uint8Array(bytes);
    return new flatbuffers.ByteBuffer(data);
}

export function getFloat32bArray(bytes: ArrayBufferLike) {
    const e = Dim.Float32bArray.getRootAsFloat32bArray(toByteBuffer(bytes));
    return {
        values: e.dataArray(),
    };
}

export function getLabeledIndexSetByNameFromSuperSet(bytes: ArrayBufferLike, name: string): LabeledIndexSet {
    const e = Dim.LabeledIndexSuperSet.getRootAsLabeledIndexSuperSet(toByteBuffer(bytes));
    const setIndex = [...new Array<number>(e.setsLength())].filter((index) => {
        const set = e.sets(index);
        if (set === null) return false;
        return set.name() === name;
    });
    if (setIndex.length !== 1) return;
    const set = e.sets(setIndex[0]);
    if (set === null)
        return {
            name: null,
            indices: null,
        };
    const indices = set.indices();
    if (indices !== null)
        return {
            name: set.name(),
            indices: indices.dataArray(),
        };
}

export function getLabeledIndexSuperSet(bytes: ArrayBufferLike): LabeledIndexSuperSet {
    const e = Dim.LabeledIndexSuperSet.getRootAsLabeledIndexSuperSet(toByteBuffer(bytes));
    const name = e.name();
    const sets = [...new Array(e.setsLength()).keys()].map((index) => {
        const set = e.sets(index);
        if (set === null) return null;
        const indices = set.indices();
        if (set !== null && indices !== null)
            return {
                name: set.name(),
                indices: indices.dataArray(),
            };
    });
    return {
        name: name,
        sets: sets,
    };
}

export function getCoordinates2D(bytes: ArrayBufferLike): Coordinates2D {
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

export function getColorArray1D(bytes: ArrayBufferLike): ColorArray1D {
    const e = Dim.ColorArray1D.getRootAsColorArray1D(toByteBuffer(bytes));
    const color = e.color();
    return color === null
        ? null
        : {
              color: color.dataArray(),
          };
}
