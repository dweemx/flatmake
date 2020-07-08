type LabeledIndexSet = {
    name: string;
    indices: Uint32Array;
};

type LabeledIndexSuperSet = {
    name: string;
    sets: LabeledIndexSet[];
};

type Coordinates2D = {
    x: Float32Array;
    y: Float32Array;
};

type ColorArray1D = {
    color: Uint8Array | null;
};
