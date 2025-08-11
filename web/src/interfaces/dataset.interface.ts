export interface Dataset {
    id: number,
    name: string,
    status: string,
    created_at: string,
}

export interface DatasetFeature {
    id: number,
    name: string,
}

export interface DatasetProduct {
    id: number,
}

export interface DatasetValue {
    id: number,
    product_id: number,
    feature_id: number
    value: string
}
