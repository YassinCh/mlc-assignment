export interface Dataset {
    id: string,
    name: string,
    status: string,
    created_at: string,
}

export interface Feature {
    id: string,
    dataset_id: string,
    name: string,
}

export interface Product {
    id: string,
    dataset_id: string,
}

export interface Value {
    id: string,
    product_id: string,
    feature_id: string,
    value: string
}
